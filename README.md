
# CYPLAN 101 at UC Berkeley - Measuring Accessibility for San Francisco Students: A Geospatial Analysis of Parks, Transit, and School Environments

This repository contains the full reproducible workflow for analyzing public and private school accessibility in San Francisco, including proximity to parks, walkshed modeling, and spatial equity comparisons. All data processing, geospatial cleaning, and analysis steps are implemented using Python, GeoPandas, OSMnx, and a Makefile-based automation pipeline.

---

## Project Website

An interactive version of this analysis—including maps, figures, and full results—is available on GitHub Pages:

**[https://daniimurphy.github.io/cyplan101-proj-group26/]**

The website contains:
- Interactive park accessibility maps
- PTAL visualizations across time periods
- Local Indicators of Spatial Association (LISA) cluster maps
- Full results and discussion

## Repository Structure

cyplan101-project/

├── data/ # raw, interim, processed datasets (untracked large files)

├── notebooks/ # exploratory + analysis notebooks

├── scripts/ # reusable scripts for data cleaning, processing

├── index.html/ # html for Github Pages project writeup

├── requirements.txt # reproducible environment

└── README.md

## Data Sources

### Schools (Public & Private)
School location and attribute data are obtained via **FEMA’s Resilience Analysis and Planning Tool (RAPT)**, which aggregates infrastructure datasets sourced from the **Homeland Infrastructure Foundation-Level Data (HIFLD)** database.

The dataset includes:
- Geospatial locations of public and private schools in San Francisco  
- Enrollment counts  
- Grade spans and facility metadata  

Public and private school datasets are cleaned, standardized, and harmonized using:


scripts/clean_schools.py

### Parks & Recreation
Parks and open space data are sourced from **San Francisco Open Data**, containing polygon geometries and metadata for all park properties within the city. These data are used to compute **park accessibility within 15-minute walking isochrones** around each school.

---

### Transit
Public transit accessibility is derived from **static GTFS schedule data**, sourced from:

- **511 Bay Area Open Transit Data (regional GTFS feed)**

The GTFS feed aggregates schedules across all Bay Area transit agencies, enabling consistent computation of **stop-level service frequency** and accessibility measures.

---

### Street Network
Pedestrian networks are derived from **OpenStreetMap** using **OSMnx**, enabling walkable catchment (isochrone) modeling for each school.

---

## Analysis Overview

Key analytical components include:
- **15-minute walking isochrones** for each school  
- **Park accessibility**, measured as the number of parks reachable within each isochrone  
- **Enrollment-normalized park access** (parks per 100 students)  
- **Public Transit Accessibility Level (PTAL)**–style scores incorporating walk time and service frequency  
- **Spatial autocorrelation analysis**, including:
  - Global Moran’s I
  - Local Indicators of Spatial Association (LISA)

These methods allow us to identify **neighborhood-scale clustering of accessibility advantages and disadvantages**, revealing spatial inequities in transit and park access around schools.

---

## Notebooks

Notebooks in the `notebooks/` directory support both exploratory analysis and the core modeling workflow.

- **`main_analysis.ipynb`**  
  Contains the primary end-to-end workflow for:
  - Generating 15-minute walking isochrones using OSMnx  
  - Computing park accessibility metrics  
  - Constructing PTAL-style public transit accessibility scores  
  - Performing spatial autocorrelation analysis (Moran’s I and LISA)  
  - Producing figures and interactive visualizations used in the final report
    
- **`schools_plot_basic_isochrones.ipynb`**
  Demonstrates plotting of basic walking isochrones around schools.
  
- **`load_clean_school_data.ipynb`**  
  Demonstrates how the cleaned and harmonized school dataset is loaded for downstream analysis.



---

## Makefile Workflow

This project uses a **Makefile** to ensure that data processing steps are reproducible and easy to run across machines.

### Available Targets

### `make` or `make all`
Runs the full school-cleaning pipeline:
- Ensures required directory structure exists  
- Loads public and private school datasets  
- Cleans and standardizes fields  
- Filters schools to San Francisco city and county  
- Outputs a unified dataset at:

data/processed/sf_schools.geojson

yaml
Copy code

---

### `make setup`
Creates the expected directory structure:

data/raw/
data/processed/

yaml

---

### `make schools`
Runs only the school-cleaning step:

```bash
python3 scripts/clean_schools.py \
  data/raw/private_schools.geojson \
  data/raw/public_schools.geojson \
  data/processed/sf_schools.geojson
```

###  `make clean`
Removes processed datasets:

``` bash
rm -f data/processed/*.geojson
```

## Reproducible Environment
Install dependencies using pip:

```bash
pip install -r requirements.txt
```
Or using conda:

```bash
conda create -n cyplan101 python=3.10
conda activate cyplan101
pip install -r requirements.txt
```

## License & Attribution
Raw data sources include:

FEMA / HIFLD — Public and Private Schools

San Francisco Open Data — Parks & Recreation

OpenStreetMap contributors — Street network data (via OSMnx)

511 Bay Area (2025) — Regional GTFS Transit Data

