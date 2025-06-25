# RADCAT (Radio Analysis of Duplicates CATalogue)

`RADCAT` is an amulgimation of existing catalogues in literature where the usage of the Vertex Cover Heuristc is employed to remove duplicate sources during catalogue compilation. Furthermore, `RADCAT` is comprised out of  radio sources that have been observed not only in the __FIRST__ and __NVSS__ surveys, but also the __LoTSS__ survey. 

`RADCAT` was used to construct six dataset (that can be found on [Zenodo](https://zenodo.org/records/14718007)), and as such its purpose is to facilitate various machine learning models that can leverage multi-modal survey inputs to enhance classification accuracy. This includes testing different transfer learning approaches across surveys with varying resolution and sensitivity, as well as exploring cross-survey image generation techniques. The six datasets that depict the sources catalogued in `RADCAT` are:

1) `RADCAT-F` (Image dataset with fixed pixel resolution across surveys).
1) `RADCAT-Fc` (RADCAT-F with sigma clipping applied).
1) `RADCAT-V` (Image dataset with varying pixel resolution across surveys).
1) `RADCAT-Vc` (RADCAT-V with sigma clipping applied).
1) `RADVIS `(Reverse engineered visibilities dataset).
1) `RADVISc` (RADVIS with sigma clipping applied to the images before reverse engineering visibilities).

## Column Headings of `RADCAT.csv`:
- Index           - The source identifier associated with the fits filename. 
- RAh             - Hour part of the right ascension.
- RAm            - Minute part of the right ascension.
- RAs              - Second part of the right ascension.
- DECsign      - Positive or negative sign for declination.
- DECd           - Magnitude of degree part of declination.
- DECm          - Arcminute part of declination.
- DECs           - Arcsecond part of declination.
- Catalog       - Radio source origin.
- Type            - `RADCAT` morphological label.
- RA/deg       - Right ascension in degrees.
- DEC/deg     - Declination in degrees.
- Divergence - Morphological labels of source as per the constituent catalogues of `RADCAT`.
- Original       - Morphological label of source as per the source's original catalogue.   

## Additionally, supplemental files are provided which are described below.
1) _data_excluded.zip_                  - All sources excluded during the construction of the final RADCAT, due to reasons titled in the filenames.
1) _graph_theory_approach.py_   - The noval approach to radio astronomy at removing duplicate sources.  
1) _read_augmentations.ipynb_   - An example of how to read the augmentations files inside the dataset zip files an how to use them.
1) _source_ids_test.txt_                - The source ids that correspond to a RADCAT row entry that were used in the test set during research.
1) _source_ids_val_train.txt_        - The source ids that correspond to a RADCAT row entry that were used in the training set during research.
1) _Catalogue References.txt_     - The references used in the paper to compile `RADCAT`.
1) _threshold_search.csv_            - The source pairs and their distances that fell between the interval [0.005, 0.072] degrees. The 'same' or 'diff' tag was manually assigned upon visual inspection. This aided in obtaining a threshold. 