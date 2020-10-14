# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


#excute
runfile('/mnt/14TB1/MODIS_SST/DRnE_19039/Python_code/SST_Lv3_01.py', 'daily', wdir='/mnt/14TB1/MODIS_SST/DRnE_19039/Python_code')


hdf file
MODOCT.2012.0815.0204.terra-1.hdf

"""

from glob import glob
import numpy as np
from datetime import datetime
import calendar
import os
from pyhdf.SD import SD, SDC
import sys
from sys import argv

'''
# Input L3_perid : 'daily', 'weekly', 'monthly' 
script, L3_perid = argv 
if L3_perid == 'daily' or L3_perid == 'weekly' or L3_perid == 'monthly' :
    print(L3_perid, 'processing started')
else :
    print('input amoing the daily weekly monthly')
    sys.exit()
'''

L3_perid = 'daily'

#Set lon, lat, resolution
Llon, Rlon = 90, 150
Slat, Nlat = 10, 60
resolution = 0.25

#set dir name
base_dir_name = '../../'

save_dir_name = "{}{}_{}_{}_{}_{}_{}/".format(base_dir_name, 
                           str(Llon), str(Rlon), 
                           str(Slat), str(Nlat), 
                           str(resolution), L3_perid)
# dir name 
data_dir_name = "downloads/"
filename = "MODOCT.2018.1210.0140.terra-1.hdf"

print ("save_dir_name: {}".format(save_dir_name))

#create folder if not exist
if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)
    print ('*'*80)
    print (save_dir_name, 'is created')
else :
    print ('*'*80)
    print (save_dir_name, 'is exist')


#for checking time
cht_start_time = datetime.now()

print ("cht_start_time: {}".format(cht_start_time))


def print_working_time():
    working_time = (datetime.now() - cht_start_time) #total days for downloading
    return print('working time ::: %s' % (working_time))

print (print_working_time())

print ("save_dir_name: {}".format(save_dir_name))

#for modis hdf file, filename = 'DAAC_MOD04_3K/H28V05/MOD04_3K.A2014003.0105.006.2015072123557.hdf'
def MODIS_SST_L2_filename_to_datetime(filename):
    fileinfo = filename.split('.')
    #print('fileinfo', fileinfo)
    return datetime(int(fileinfo[1]), int(fileinfo[2][0:2]), int(fileinfo[2][2:4]),
                    int(fileinfo[3][0:2]), int(fileinfo[3][2:4]))

print(MODIS_SST_L2_filename_to_datetime(filename))

# make empty array
ni = np.int((Rlon-Llon)/resolution+1.00)
nj = np.int((Nlat-Slat)/resolution+1.00)
lon_array = []
lat_array = []
data_array = []
for i in range(ni):
    lon_line = []
    lat_line = []
    data_line = []
    for j in range(nj):
        lon_line.append(Llon+resolution*i)
        lat_line.append(Nlat-resolution*j)
        data_line.append([])
    lon_array.append(lon_line)
    lat_array.append(lat_line)
    data_array.append(data_line)
lat_array = np.array(lat_array)
lon_array = np.array(lon_array)
print('grid arrays are created...........\n')

print('lon_array: {}'.format(lon_array))
print('lat_array: {}'.format(lat_array))
print('data_array: {}'.format(data_array))

'''
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='cyl', resolution='l', llcrnrlat=10, urcrnrlat = 60, llcrnrlon=100, urcrnrlon = 160)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90, 90., 10.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 180., 15.), labels=[0, 0, 0, 1])
x, y = m(longitude, latitude)
m.pcolormesh(x, y, sst, vmin=0,vmax=20)
plt.title('MODIS SST')

#plt.colorbar()
plt.colorbar(cmap='rainbow', extend='max')

#plt.savefig('current{}.pdf'.format(time), bbox_inches='tight', dpi = 300)
#plt.savefig(f_name+'.png', bbox_inches='tight', dpi = 300)
'''
# read HDF file
base_dr = "../../downloads/"
filename = "MODOCT.2018.1210.0140.terra-1.hdf"
hdf = SD("{}{}".format(base_dr, filename), SDC.READ)

print (hdf.datasets())

DATAFIELD_NAME = 'sst'

sst_raw = hdf.select(DATAFIELD_NAME)
sst_attri = sst_raw.attributes()
sst_slope = sst_attri['slope']
sst_intercept = sst_attri['intercept']
sst = sst_raw.get()
sst = sst * sst_slope + sst_intercept
sst[sst < 0] = np.nan

#####
# Read geolocation dataset.
lat = hdf.select('latitude')
print(lat.attributes())
latitude = lat[:,:]
latitude1 = lat.get()
print(latitude == latitude1)

lon = hdf.select('longitude')
longitude = lon[:,:]
print(lon.attributes())

#plt.savefig('current{}.pdf'.format(time), bbox_inches='tight', dpi = 300)
#plt.savefig(f_name+'.png', bbox_inches='tight', dpi = 300)

# fill data array
lon_cood = np.array(((longitude-Llon)/resolution*100//100), dtype=np.uint16)
lat_cood = np.array(((Nlat-latitude)/resolution*100//100), dtype=np.uint16)
data_cnt = 0
for i in range(np.shape(lon_cood)[0]) :
    for j in range(np.shape(lon_cood)[1]) :
        if int(lon_cood[i][j]) < np.shape(lon_array)[0] \
            and int(lat_cood[i][j]) < np.shape(lon_array)[1] \
                and not np.isnan(sst[i][j]) :
                    data_cnt += 1 #for debug
                    data_array[int(lon_cood[i][j])][int(lat_cood[i][j])].append(sst[i][j])
                  #  print("({}/{}, {}/{}) data inserting...".format(i, np.shape(lon_cood)[0], j, np.shape(lon_cood)[1]))
                    print("{}% data inserting...\n".format((i*(np.shape(lon_cood)[0])+j)/(np.shape(lon_cood)[0]*np.shape(lon_cood)[1])*100))
        
        





