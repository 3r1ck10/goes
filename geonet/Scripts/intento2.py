#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from netCDF4 import Dataset

from mpl_toolkits.basemap import Basemap 
import numpy as np 

path = '/home/usuario/Escritorio/BELEN/geonet/GOES_16_Samples/OR_ABI-L2-CMIPF-M3C13_G16_s20183532145334_e20183532156112_c20183532156189.nc'
 
nc = Dataset(path)
 

data = nc.variables['CMI'][:] 
 
bmap = Basemap(projection='geos', lon_0=-75.0, lat_0=0.0, satellite_height=35786023.0, ellps='GRS80')
 
bmap.imshow(data, origin='upper', vmin=170, vmax=378, cmap='Greys')
 
bmap.drawcoastlines(linewidth=0.3, linestyle='solid', color='black')
bmap.drawcountries(linewidth=0.3, linestyle='solid', color='black')
bmap.drawparallels(np.arange(-90.0, 90.0, 10.0), linewidth=0.1, color='white')
bmap.drawmeridians(np.arange(0.0, 360.0, 10.0), linewidth=0.1, color='white')
 
bmap.colorbar(location='bottom', label='Brightness Temperature [K]')
 
DPI = 300
plt.savefig('/home/usuario/Escritorio/BELEN/geonet/Output/pTutorial2GOES_16_Ch13.png', dpi=DPI, bbox_inches='tight', pad_inches=0)
 
plt.show()


# In[ ]:




