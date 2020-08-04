'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Created on Sat Nov  3 20:34:47 2018
@author: guitar79
created by Kevin 
#Open hdf file
ModuleNotFoundError: No module named 'pyhdf'
conda install -c conda-forge pyhdf
#basemap
conda install -c conda-forge basemap-data-hires
conda install -c conda-forge basemap
'''

from pyhdf.SD import SD, SDC

base_dr = "../../downloads/"
filename = "MYDOCT.2018.1227.1740.aqua-1.hdf"
hdf = SD("{}{}".format(base_dr, filename), SDC.READ)

# Read SST dataset.
#DATAFIELD_NAME='Optical_Depth_Land_And_Ocean'
#hdf_raw = hdf.select(DATAFIELD_NAME)
#aod_data = hdf_raw[:,:]
#scale_factor = hdf_raw.attributes()['scale_factor']
#add_offset = hdf_raw.attributes()['add_offset']
#aod = aod_data * scale_factor + add_offset
#aod[aod < 0] = np.nan
#aod = np.asarray(aod)

# Read geolocation dataset.
#lat = hdf.select('Latitude')
#latitude = lat[:,:]
#lon = hdf.select('Longitude')
#longitude = lon[:,:]