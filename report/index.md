# San Francisco School Access & Facilities Analysis

## Authors
Group 26
CYPLAN 101 — Fall 2025  
University of California, Berkeley

---

## 1. Introduction

### 1.1 Problem and Motivation

This project investigates how middle school and high school students across San Francisco experience access to key urban resources. Specifically, we analyze how access to parks and recreation facilities, privately owned public open spaces, and transit varies throughout the city, and whether meaningful differences emerge between public and private schools.  
Our goal is to understand how the built environment and public infrastructure shape student experience, opportunity, and spatial equity.

To conduct this analysis, we integrate multiple geospatial datasets, including public and private school locations sourced from the Homeland Infrastructure Foundation-Level Data (HIFLD) repository via FEMA’s RAPT tool (Oak Ridge National Laboratory, 2025), OpenStreetMap pedestrian street networks processed through OSMnx for walkability modeling, San Francisco Recreation & Parks assets for green-space accessibility, San Francisco Planning’s 2023 Land Use dataset, and demographic context from the U.S. Census American Community Survey (ACS) 5-Year Estimates. All datasets were projected, cleaned, and integrated using GeoPandas to support reproducible spatial analysis and visualization.

### 1.2 Transit Accessibility Framework

“Transit accessibility” has no single agreed-upon definition, and a wide range of methodologies exist for evaluating it. As reviewed in Chung et al. (2020), accessibility metrics generally fall into three broad classes:

- **Distance-based methods**, such as the Public Transport Accessibility Level (PTAL) metric widely applied in the UK. PTAL incorporates average waiting time, service frequency, and reliability, providing more insight than simply counting nearby transit stops.
- **Gravity-based methods**, which weight destinations based on attractiveness, impedance, or travel cost.
- **Utility-based methods**, which estimate accessibility using a utility function accounting for traveler preferences and urban opportunities.

Given the complexity, data requirements, and modeling assumptions of gravity-based and utility-based approaches, we adopt **PTAL** as a reasonable, interpretable, frequency-adjusted metric for evaluating transit accessibility in San Francisco. By integrating wait times and service reliability, PTAL offers a more meaningful comparison across school environments than raw stop counts.

---

## 2. Data Sources

This analysis uses publicly available geospatial datasets. Only processed files are stored in the repository; raw data must be downloaded separately.

### 2.1 Schools (Public and Private)
Public and private school locations were obtained from **FEMA’s Resilience Analysis and Planning Tool (RAPT)**, which aggregates infrastructure datasets from the **Homeland Infrastructure Foundation-Level Data (HIFLD)** repository.  
Attributes include unique facility IDs, enrollment, grade ranges, and basic administrative metadata.

### 2.2 Parks & Recreation
Park boundaries and facility attributes were downloaded from the **San Francisco Recreation and Park Department** dataset on **SF Open Data**.

### 2.3 Street Network
The pedestrian network for walkability modeling was downloaded from **OpenStreetMap**, accessed through the **OSMnx** Python package.

---

## 3. Methods

### 3.1 Data Cleaning
School records were harmonized and standardized using `src/clean_schools.py`. Steps included:
- Converting all geometries to a common CRS (EPSG:4326)
- Cleaning invalid enrollment values
- Mapping grade ranges into four categories: Elementary, Middle, High, Combined
- Filtering to schools located within San Francisco County

### 3.2 Walkshed / Isochrone Generation
Using OSMnx and NetworkX, 15-minute walking isochrones were generated for each school:
- Street network downloaded in pedestrian mode
- Each school mapped to its nearest street node
- Ego-graphs computed with time-based edge cost
- Isochrone polygons created with a convex hull + buffer approach

### 3.3 Park Accessibility Join
Isochrones were spatially joined with park boundaries to estimate:
- Number of parks accessible within 15 minutes
- Total accessible park area
- Overlap ratios (percentage of the walkshed covered by recreational space)

### 3.4 Aggregation & Analysis
Indicators were computed for:
- School-level park access
- Neighborhood-level comparisons
- Spatial equity assessments

Maps and results were created in the `notebooks/` directory using GeoPandas and Folium.

---

## 4. Results

TODO  
Present maps, figures, and descriptive findings here:
- Choropleth maps of isochrones  
- Distribution of park access  
- Accessibility differences across neighborhoods  
- Enrollment vs. access comparisons  

(Embed images into this section using `report/figures/`.)

---

## 5. Limitations

TODO
- HIFLD datasets may have inconsistent completeness across regions  
- OSM routing accuracy varies by neighborhood  
- Isochrone convex hull approximation overestimates reach in some cases  
- Enrollment values may lag behind current academic year  
- Only walking mode was considered; multimodal access not included  

---

## 6. Conclusions

Summarize key insights:
- Which schools have low or high access to parks?  
- Are certain neighborhoods disadvantaged?  
- What implications exist for planning or equity-based interventions?  

---

## 7. References

Chung, Y. S., Hong, Y., & Yoon, S. Y. (2020). *Transit accessibility: A review of metrics, methods, and approaches*. Retrieved from https://ira.lib.polyu.edu.hk/bitstream/10397/92556/1/EE-0265_Chung_Review_Transit_Accessibility.pdf

City and County of San Francisco. (2024). *Recreation and Park Department Properties* [Data set]. SF Open Data. https://data.sfgov.org

U.S. Department of Homeland Security, Homeland Infrastructure Foundation-Level Data (HIFLD). (2024). *Schools (Public and Private)* [Data set]. Accessed via FEMA’s Resilience Analysis and Planning Tool (RAPT). https://fema.gov/rapt
