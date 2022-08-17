
"""
Author: @pythonistabr
contact: gustavo.oceanografia@gmail.com

"""
#import urllib3

import wget
import sys
sys.path.append("..")

from src.links_generator import Hycom_Link_Creator

    
with open('hycom-url.txt','r') as file:
    file = file.readlines()

url = ''.join(file)

mylist = Hycom_Link_Creator(url, '2016-12-01', '2017-01-31', 7)
mylist.create_dates()
mylist.generate_urls()

counter = 1

for ii in mylist:

    print()
    print('Downloading data...')
    wget.download(ii,'/home/gus/Downloads/'+\
        'outputs_122016a012017/hycom_uv{:02d}.nc4'.format(counter))

    counter+=1
 
    

    
    


       


