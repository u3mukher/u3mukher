# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:23:03 2024

@author: Ushnik
"""

import geopandas as gpd
import pandas as pd
#import netCDF4 as nc4 
import shapely.geometry
from shapely.geometry import Polygon, Point




# Read the shapefile
gdf = gpd.read_file("Non_Clipped_Grid_with_Results_4326_dropna.shp")
df = gdf.filter(['FW_Manure', 'geometry'])






df["lon"] = df.centroid.x
df["lat"] = df.centroid.y

df = df.filter(['FW_Manure', 'lat', 'lon'])

df_new = df.to_xarray()
df_new.to_netcdf('ON_Paper_Total_Feedstock_Dataset.nc')

