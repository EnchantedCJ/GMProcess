# PEER ground motions processor

## How to use

 `PEER_GMs_Process.py` should be put in the same directory as the ground motions.

Choose the number of directions (spectral ordinates):

- 1 ---- H1
- 2 ---- SPSS

Choose if scale or not:

- y ---- scaling (`_SearchResults.csv` must exist to provide scale factors)
- n ---- no scaling

Get results in `/output/`