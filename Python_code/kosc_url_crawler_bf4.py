# Based on python2

import urllib.request as urllib
import os
import satellite, year, month, day, t

# Example file path : 
# http://222.236.46.45/nfsdb/MODISA/2011/09/01/L2/MYDOCBOX.2011.0901.0413.aqua-1.hdf.zip
# http://222.236.46.45/nfsdb/MODIST/2011/09/01/L2/MODOCBOX.2011.0901.0235.terra-1.hdf.zip
# http://222.236.46.45/nfsdb/MODISA/2015/07/11/L2/MYDOCT.2015.0711.0457.aqua-1.hdf.zip
# http://222.236.46.45/nfsdb/MODIST/2011/09/03/L2/MODOCT.2011.0903.0222.terra-1.hdf.zip
full_url = 'http://222.236.46.45/nfsdb/MODISA/2011/09/01/L2/MYDOCT.2011.0901.0413.aqua-1.hdf.zip'

save_dir_name = '../../downloads/'
if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)

filename_el = full_url.split("/")
filename = filename_el[-1]

filename_s = filename.split(".")

satelite = [0, 1]

for i in satelite:
    if i == 0:
        filename_el[4] = 'MODISA'
        filename_s[0] = 'MYDOCT'
        filename_s[4] = 'aqua-1'
    else:
        filename_el[4] = 'MODIST'
        filename_s[0] = 'MODOCT'
        filename_s[0] = 'terra-1'
    
    urllib.urlretrieve(full_url, '{0}{1}'.format(save_dir_name, filename))