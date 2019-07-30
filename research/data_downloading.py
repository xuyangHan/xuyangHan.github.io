import urllib.request
import requests


print('Beginning file download with urllib2...')
#https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2009/01_January_2009/Zone9_2009_01.zip

for i in range(0, 20):
    file_num = i + 1
    # if file_num < 10:
    #     file_num = '0' + str(file_num)
    file = 'Zone' + str(file_num) + '_2009_08.zip'
    url = 'https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2009/08_August_2009/' + file
    location = r'C:/Users/62707/Downloads/data/' + file
    response = requests.get(url)
    print(file_num)
    if response.status_code == 200:
        urllib.request.urlretrieve(url, location)
