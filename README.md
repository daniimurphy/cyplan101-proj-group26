IN PROGRESS

# CYPLAN 101 at UC Berkeley - Measuring Accessibility for San Francisco Students: A Geospatial Analysis of Parks, Transit, and School Environments

This repository contains the full reproducible workflow for analyzing public and private school accessibility in San Francisco, including proximity to parks, walkshed modeling, and spatial equity comparisons. All data processing, geospatial cleaning, and analysis steps are implemented using Python, GeoPandas, OSMnx, and a Makefile-based automation pipeline.

---


## Repository Structure

cyplan101-project/

├── data/ # raw, interim, processed datasets (untracked large files)

├── notebooks/ # exploratory + analysis notebooks

├── scripts/ # reusable scripts for cleaning, processing, modeling

├── report/ # project writeup

├── requirements.txt # reproducible environment

└── README.md

## Data

Schools (Public & Private):
Obtained via FEMA’s Resilience Analysis and Planning Tool (RAPT), which provides infrastructure datasets sourced from the Homeland Infrastructure Foundation-Level Data (HIFLD) database.
The dataset includes geospatial locations of all public and private schools in San Francisco, as well as attributes such as enrollment, grade range, and facility type.

These fields are cleaned, standardized, and harmonized using the script:

scripts/clean_schools.py

See `data/README.md` for instructions on how to download and store data locally.

## Notebooks
Use load_clean_school_data.ipynb to download our cleaned school dataset.

## Makefile Workflow

This project uses a **Makefile** to ensure that key steps in the pipeline are reproducible, simple, and consistent across machines.

### Available Targets

#### **1. `make` or `make all`**
Runs the full school-cleaning pipeline:
- Ensures required directories exist  
- Loads public + private school datasets  
- Cleans and standardizes fields  
- Filters schools to San Francisco  
- Outputs a unified dataset at:

data/processed/sf_schools.geojson


#### **2. `make setup`**
Creates the expected directory structure:

data/raw/
data/processed/

#### **3. `make schools`**
Runs only the school-cleaning script:

python3 scripts/clean_schools.py
data/raw/private_schools.geojson
data/raw/public_schools.geojson
data/processed/sf_schools.geojson


#### **4. `make clean`**
Removes processed datasets:

rm -f data/processed/*.geojson


---

## Reproducible Environment

Install dependencies using:

```bash
pip install -r requirements.txt
```

Or with conda:
```bash
conda create -n cyplan101 python=3.10
conda activate cyplan101
pip install -r requirements.txt
```

## License & Attribution

Raw data is sourced from:

FEMA / HIFLD (Public and Private Schools)

SF Open Data (Parks & Recreation)

OpenStreetMap (Street network via OSMnx)

GTFS Transit Data (https://www.sfmta.com/reports/gtfs-transit-data)

511 SF Bay (2025), Open Transit Data — GTFS Feed Download, retrieved from 511.org

See report/index.md for full APA citations.

