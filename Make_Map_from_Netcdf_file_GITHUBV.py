from netCDF4 import Dataset as NetCDFFile 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

nc = NetCDFFile('ON_Paper_Total_Feedstock_Dataset.nc', mode='r')

lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
Feedstock = nc.variables['FW_Manure'][:]
nc.close()




# How much to zoom from coordinates (in degrees)
zoom_scale = 0

# Setup the bounding box for the zoom and bounds of the map
bbox = [np.min(lat)-zoom_scale,np.max(lat)+zoom_scale,\
        np.min(lon)-zoom_scale,np.max(lon)+zoom_scale]

plt.figure(figsize=(12,6))
# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
            llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution='i')
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full

m.drawcoastlines()
m.drawstates()
m.drawcountries()

m.drawlsmask(land_color='Linen', ocean_color='#CCFFFF') # can use HTML names or codes for colors
m.drawcounties() # you can even add counties (and other shapefiles!)

#m.plot(*m(lon, lat), marker=None, color='m')
#m.plot(lon, lat, color="r", linewidth=0.5, latlon=True)


lons, lats = np.meshgrid(lon, lat)
xi, yi = m(lons, lats)
cs = m.pcolormesh([xi, yi],Feedstock, latlon = True)
plt.show()
