#!/usr/bin/env python3
"""
Clean and merge private and public school data for San Francisco.
This script standardizes public & private school datasets by:
- converting CRS to EPSG:4326,
- cleaning enrollment values,
- harmonizing schemas,
- mapping school levels,
- filtering to San Francisco County, and
- writing a unified GeoJSON output.

Usage:
    python clean_schools.py \
        data/raw/private_schools.geojson \
        data/raw/public_schools.geojson \
        data/processed/sf_schools.geojson
"""

import sys
import pandas as pd
import geopandas as gpd
import numpy as np

# ================================================================
# Mapping dictionaries
# ================================================================
priv_level_map = {
    1: "Elementary",
    2: "High",
    3: "Combined"
}

pub_level_map = {
    "ELEMENTARY": "Elementary",
    "PREKINDERGARTEN": "Elementary",
    "MIDDLE": "Middle",
    "HIGH": "High",
    "SECONDARY": "Combined",
    "OTHER": "Combined",
    "UNGRADED": "Combined",
    "NOT REPORTED": None,
    "NOT APPLICABLE": None,
    "ADULT EDUCATION": None,
}


# ================================================================
# Cleaning helpers
# ================================================================
def clean_level_private(df):
    return df["level_"].map(priv_level_map)


def clean_level_public(df):
    return df["level_"].str.upper().map(pub_level_map)


def clean_enrollment(df):
    df["enrollment"] = df["enrollment"].astype(float)
    df.loc[df["enrollment"] < 0, "enrollment"] = np.nan
    return df


def filter_to_san_francisco(gdf):
    return gdf[
        gdf["city"].str.contains("San Francisco", case=False, na=False)
        | gdf["county"].str.contains("San Francisco", case=False, na=False)
    ]


# ================================================================
# MAIN PIPELINE
# ================================================================
def process_school_data(private_raw, public_raw):
    """
    Cleans and merges private & public school datasets.
    Returns a GeoDataFrame of all SF schools with harmonized schema.
    """

    # ------------------------------------------------------------
    # Normalize CRS
    # ------------------------------------------------------------
    if private_raw.crs is None or public_raw.crs is None:
        raise ValueError("Both input GeoDataFrames must have a CRS.")

    private = private_raw.to_crs("EPSG:4326").copy()
    public = public_raw.to_crs("EPSG:4326").copy()

    # ------------------------------------------------------------
    # Standardize column names
    # ------------------------------------------------------------
    private.columns = private.columns.str.lower()
    public.columns = public.columns.str.lower()

    # ------------------------------------------------------------
    # Level cleaning
    # ------------------------------------------------------------
    private["level_clean"] = clean_level_private(private)
    public["level_clean"] = clean_level_public(public)

    # ------------------------------------------------------------
    # Enrollment cleanup
    # ------------------------------------------------------------
    private = clean_enrollment(private)
    public = clean_enrollment(public)

    # ------------------------------------------------------------
    # Restrict to San Francisco
    # ------------------------------------------------------------
    private_sf = filter_to_san_francisco(private)
    public_sf = filter_to_san_francisco(public)

    # ------------------------------------------------------------
    # Harmonize schemas
    # ------------------------------------------------------------
    needed_cols = sorted(set(private_sf.columns) | set(public_sf.columns))

    for col in needed_cols:
        if col not in private_sf.columns:
            private_sf[col] = None
        if col not in public_sf.columns:
            public_sf[col] = None

    private_sf = private_sf[needed_cols]
    public_sf = public_sf[needed_cols]

    # ------------------------------------------------------------
    # Concatenate
    # ------------------------------------------------------------
    schools_sf = pd.concat([private_sf, public_sf], ignore_index=True)

    # Add unique ID
    schools_sf["school_id"] = schools_sf.index.astype(int)

    # Make sure it's a GeoDataFrame
    return gpd.GeoDataFrame(schools_sf, geometry="geometry", crs="EPSG:4326")


# ================================================================
# CLI SUPPORT
# ================================================================
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean_schools.py private.geojson public.geojson output.geojson")
        sys.exit(1)

    private_file, public_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]

    print("Loading input files...")
    private_raw = gpd.read_file(private_file)
    public_raw = gpd.read_file(public_file)

    print("Processing...")
    schools_clean = process_school_data(private_raw, public_raw)

    print(f"Saving cleaned dataset to: {out_file}")
    schools_clean.to_file(out_file, driver="GeoJSON")

    print("Done!")
