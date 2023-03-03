
"""
Author: @pythonistabr
contact: gustavo.oceanografia@gmail.com
"""
import wget
from glob import glob
from src.links_generator import Hycom_Link_Creator as hlc

    
with open('hycom-url.txt','r') as file:
    file = file.readlines()

url = ''.join(file)

mylist = hlc(url,'2017-12-02','2018-01-01')
mylist.create_dates()
mylist.generate_urls()

previous_files = glob("E:\dados-mestrado\hycom\hycom_netcdfs\*.nc4")
counter = len(previous_files)

for _file in mylist:
    try:
        print('Downloading data...')
        print(_file)
        wget.download(_file,"E:\dados-mestrado\hycom\hycom_netcdfs\\hycom_uv{:02d}.nc4".format(counter))
        counter += 1
    except: "URLError"
    print()
    print("Url não encontrada")
    print()