TODO

## Repository Structure

cyplan101-project/
├── data/ # raw, interim, processed datasets (untracked large files)

├── notebooks/ # exploratory + analysis notebooks
├── src/ # reusable scripts for cleaning, processing, modeling
├── report/ # project writeup
├── requirements.txt # reproducible environment
└── README.md

## Data

Schools (Public & Private):
Obtained via FEMA’s Resilience Analysis and Planning Tool (RAPT), which provides infrastructure datasets sourced from the Homeland Infrastructure Foundation-Level Data (HIFLD) database.
The dataset includes geospatial locations of all public and private schools in San Francisco, as well as attributes such as enrollment, grade range, and facility type.
We clean and standardize these fields using the scripts in src/.

See `data/README.md` for instructions on how to download and store data locally.
