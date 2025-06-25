import numpy as np

def _create_neighbourhoods(distances_df, threshold):
    """
    Identify and group sources into neighbourhoods based on haversine distance thresholds.
    This function iterates over a symmetric distance matrix (distances_df) and, for each pair of sources
    whose distance is less than or equal to the specified threshold (excluding self-pairs), groups them
    into neighbourhoods (sets of sources). If either source is already present in an existing neighbourhood,
    both are added to that neighbourhood; otherwise, a new neighbourhood is created. Non-neighbour pairs
    have their corresponding distances set to NaN in the DataFrame.
    Parameters
    ----------
    distances_df : pandas.DataFrame
        A symmetric DataFrame where both the index and columns are identical and represent sources, and each cell contains
        the haversine distance between the corresponding pair of sources.
    threshold : float
        The maximum distance for two sources to be considered part of the same neighbourhood.
    Returns
    -------
    neighbourhoods : list of set
        A list where each element is a set containing the sources that form a neighbourhood.
    """
    
    sources = distances_df.index
    neighbourhoods = []
    
    for i in range(len(sources)):
        for j in range(i, len(sources)):
            
            if distances_df.iloc[i, j] <= threshold and i != j:
                
                s1 = sources[i]
                s2 = sources[j]
                
                neigh_exists = False
                for neigh in neighbourhoods:
                    if s1 in neigh or s2 in neigh:
                        neigh.add(s1)
                        neigh.add(s2)
                        neigh_exists = True
                        break
                    
                if not neigh_exists:
                    neighbourhoods.append({s1, s2})
            
            else: # Set non-edge to NaNs
                distances_df.iloc[i, j] = np.nan
                distances_df.iloc[j, i] = np.nan
                    
    return neighbourhoods



def vertex_cover_heuristic(distances_df, threshold = 0.03):
    """
    Heuristic algorithm to compute a vertex cover for a graph represented by a haversine distance DataFrame.
    The input DataFrame should be square (same index and columns), where each entry [i, j] contains
    the distance between source i and source j. An edge exists between two sources if their distance
    is less than or equal to the specified threshold. The function removes a subset of sources such that
    all edges are covered, using a greedy heuristic.
    
    Parameters
    ----------
    distances_df : pandas.DataFrame
        A square DataFrame where both the index and columns represent sources, and each cell contains
        the haversine distance between the corresponding sources.
    threshold : float, optional
        The maximum distance for two sources to be considered connected by an edge. Defaults to 0.03.
    
    Returns
    -------
    pandas.DataFrame
        A filtered version of the input DataFrame, with rows corresponding to the removed sources (vertex cover) excluded.
    """
    
    cover_of_removed_sources = set()
    neighbourhoods = _create_neighbourhoods(distances_df, threshold)
    
    for n, neigh in enumerate(neighbourhoods):
        
        distances_of_neighs = distances_df.loc[list(neigh), [str(x) for x in neigh]]
        
        num_of_edges_if_fully_connected = len(neigh) * (len(neigh) - 1) // 2
        actual_num_of_edges = distances_of_neighs.count().sum() // 2 # Recall that '_create_neighbourhoods' set non-edges to np.nan
        
        if num_of_edges_if_fully_connected == actual_num_of_edges:
            source_to_stay = int(distances_of_neighs.sum(axis=1).idxmin())
            removed_sources = set(neigh) - {source_to_stay}
            cover_of_removed_sources.update(removed_sources)
            
        else:
            while actual_num_of_edges > 0:
                
                edge_counts = distances_of_neighs.count()
                sources_with_most_edges = edge_counts[edge_counts == edge_counts.max()].index.astype(int)
                vertex = int(distances_of_neighs.loc[sources_with_most_edges].sum(axis=1).idxmin())
                cover_of_removed_sources.add(vertex)
                
                distances_of_neighs = distances_of_neighs.drop(index=vertex, columns=str(vertex))
                actual_num_of_edges = distances_of_neighs.count().sum()
                
    return distances_df[~distances_df.index.isin(cover_of_removed_sources)]