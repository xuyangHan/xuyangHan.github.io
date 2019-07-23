import os

csv_header = 'MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,' \
             'CallSign,VesselType,Status,Length,Width,Draft,Cargo'
csv_out = 'AIS_2017_01.csv'

csv_dir = r'C:\Users\admin\Downloads\data downloaded\AIS_ASCII_by_UTM_Month\2017_v2'
os.chdir(csv_dir)

dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
    pass

csv_list = []
for file in filenames:
    if file.endswith('.csv'):
        csv_list.append(file)

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header)
csv_merge.write('\n')

i = 0
for file in csv_list:
    print('start merge file_' + str(i) + '\n')
    csv_in = open(file)
    for line in csv_in:
        if line.startswith(csv_header):
            continue
        csv_merge.write(line)
    csv_in.close()

    print('file_' + str(i) + ' merged success \n')
    i += 1

csv_merge.close()
print('Verify consolidated CSV file : ' + csv_out)
