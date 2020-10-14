# Based on python2

import urllib.request as urllib
import os

# Example file path : 
# http://222.236.46.45/nfsdb/MODISA/2011/09/01/L2/MYDOCBOX.2011.0901.0413.aqua-1.hdf.zip
# http://222.236.46.45/nfsdb/MODIST/2011/09/01/L2/MODOCBOX.2011.0901.0235.terra-1.hdf.zip
# http://222.236.46.45/nfsdb/MODISA/2015/07/11/L2/MYDOCT.2015.0711.0457.aqua-1.hdf.zip
# http://222.236.46.45/nfsdb/MODIST/2011/09/03/L2/MODOCT.2011.0903.0222.terra-1.hdf.zip
# http://222.236.46.45/nfsdb/MODISA/2012/01/02/L2/MYDOCT.2012.01.02.0510.aqua-1.hdf.zip
#full_url = 'http://222.236.46.45/nfsdb/MODISA/2019/01/01/L2/MYDOCT.2019.0101.0000.aqua-1.hdf.zip'

save_dir_name = '../../downloads/'
if not os.path.exists(save_dir_name):
    os.makedirs(save_dir_name)



url1 = 'http://222.236.46.45/nfsdb/MODISA'
url2 = 'aqua-1.hdf.zip'

full_urls = []

for Yr in range(2019, 2020) :
    for Mo in range(1, 13) :
        for Da in range(1, 32) :
            for Ho in range(0, 24) :
                for Mi in range(0, 60) :
                    full_urls.append("{0}/{1:04d}/{2:02d}/{3:02d}/L2/MYDOCSST.{1:04d}.{2:02d}{3:02d}.{4:02d}{5:02d}.{6}"\
                                         .format(url1, Yr, Mo, Da, Ho, Mi, url2))
                
for full_url in full_urls : 
    filename_el = full_url.split("/")
    filename = filename_el[-1]

    if not os.path.exists(filename) :
        try :
            urllib.urlretrieve(full_url, '{0}{1}'.format(save_dir_name, filename))
            print ('Trying {0}'.format(full_url), '{0}{1}\n'.format(save_dir_name, filename))
        except Exception as e: 
            print('error {0} : {1}\n'.format(e, filename))
    else :
        print ('{0} already exists\n'.format(filename))
        