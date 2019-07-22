import urllib.request
import requests


print('Beginning file download with urllib2...')
#

for i in range(11, 20):
    file_num = i + 1
    if file_num < 10:
        file_num = '0' + str(file_num)
    file = 'AIS_2017_01_Zone' + str(file_num) + '.zip'
    url = 'https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2017/' + file
    location = r'C:/Users/admin/Downloads/data downloaded/' + file
    response = requests.get(url)
    print(file_num)
    if response.status_code == 200:
        urllib.request.urlretrieve(url, location)
