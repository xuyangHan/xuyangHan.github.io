import time

start = time.process_time()
import pymongo
from pymongo import MongoClient

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.Lakes_Ontario_Data
print('Database Connection: ')
Connection_time = time.process_time()
print(Connection_time - start)

MMSI_list = []
# for lineData in db.lineData.find():
#     MMSI = lineData['MMSI']
#     MMSI_list.append(MMSI)
# print('The content and the size of MMSI: \n')
# print(MMSI_list)
# print(len(MMSI_list))

i = 1
discarded = 0
imported = 0

cursor = db.PointData.find().sort([("BaseDateTime", pymongo.ASCENDING)])
print('Find Documents: ')
Document_time = time.process_time()
print(Document_time - Connection_time)

print('Data loading continues \n')
Update_time = time.process_time()
Insert_time = time.process_time()
for point in cursor:
    if i % 1000 == 0:
        print(i)
    i = i + 1

    MMSI = point['MMSI']
    # loop_start_time = time.process_time()
    if MMSI not in MMSI_list:
        MMSI_list.append(MMSI)
        BaseDateTimeStart = point['BaseDateTime']
        BaseDateTimeEnd = point['BaseDateTime']
        Longitude = point['Location']['coordinates'][0]
        Latitude = point['Location']['coordinates'][1]
        SOG = point['SOG']
        COG = point['COG']
        Heading = point['Heading']
        VesselName = point['Vessel Info']['VesselName']
        IMO = point['Vessel Info']['IMO']
        CallSign = point['Vessel Info']['CallSign']
        VesselType = point['Vessel Info']['VesselType']
        Length = point['Vessel Info']['Length']
        Width = point['Vessel Info']['Width']
        Status = point['Status']
        Draft = point['Draft']
        Cargo = point['Cargo']

        d = {
            "MMSI": MMSI,
            "geometry": {
                "type": "LineString",
                "coordinates": [[Longitude, Latitude]]
            },
            "BaseDateTime": [BaseDateTimeEnd],
            "BaseDateTimeStart": BaseDateTimeStart,
            "BaseDateTimeEnd": BaseDateTimeEnd,

            "Velocity": {
                "SOG": [SOG],
                "COG": [COG],
                "Heading": [Heading],
            },
            "Vessel Info": {
                "VesselName": VesselName,
                "IMO": IMO,
                "CallSign": CallSign,
                "VesselType": VesselName,
                "Length": Length,
                "Width": Width
            },
            "Status": Status,
            "Draft": Draft,
            "Cargo": Cargo,
        }
        imported += 1
        db.lineData.insert_one(d)
        # print('Insert a Document: ')
        # Insert_time = Insert_time + time.process_time() - loop_start_time
        # print(Insert_time - loop_start_time)
    else:
        line = db.lineData.find_one({"MMSI": MMSI})

        coordinates = line['geometry']['coordinates']

        BaseDateTimes = line['BaseDateTime']
        lastMinute = int(BaseDateTimes[-1][-7]) * 60 + int(BaseDateTimes[-1][-5]) * 10 + int(BaseDateTimes[-1][-4])
        BaseDateTimeEnd = point['BaseDateTime']
        currentMinute = int(BaseDateTimeEnd[-7]) * 60 + int(BaseDateTimeEnd[-5]) * 10 + int(BaseDateTimeEnd[-4])
        if (coordinates[-1][0] - point['Location']['coordinates'][0] <= 0.00005 and coordinates[-1][1] -
            point['Location']['coordinates'][1] <= 0.00005) or \
                abs(lastMinute - currentMinute) < 14:
            discarded += 1
            continue
        else:
            imported += 1
            BaseDateTimes.append(BaseDateTimeEnd)
            coordinates.append(point['Location']['coordinates'])

        SOGs = line['Velocity']['SOG']
        SOGs.append(point['SOG'])
        COGs = line['Velocity']['COG']
        COGs.append(point['COG'])
        Headings = line['Velocity']['Heading']
        Headings.append(point['Heading'])

        db.lineData.update_one(
            {"MMSI": MMSI},
            {
                "$set": {
                    "BaseDateTimeEnd": BaseDateTimeEnd,
                    "BaseDateTime": BaseDateTimes,
                    "geometry": {
                        "type": "LineString",
                        "coordinates": coordinates
                    },
                    "Velocity": {
                        "SOG": SOGs,
                        "COG": COGs,
                        "Heading": Headings,
                    },
                }
            }
        )

        # db.lineData.update_one(
        #     {"MMSI": MMSI},
        #     {
        #         "$set": {
        #             "geometry": {
        #                 "type": "LineString",
        #                 "coordinates": coordinates
        #             }
        #         }
        #     }
        # )
        #
        #
        # db.lineData.update_one(
        #     {"MMSI": MMSI},
        #     {
        #         "$set": {
        #             "Velocity": {
        #                 "SOG": SOGs,
        #                 "COG": COGs,
        #                 "Heading": Headings,
        #             },
        #         }
        #     }
        # )
        # print('Update a Document: ')
        # Update_time = Update_time + time.process_time() - loop_start_time
        # print(Update_time - loop_start_time)

# print('Update a Document: ')
# print(Update_time)
#
# print('Insert a Document: ')
# print(Insert_time)

print('discarded')
print(discarded)
print('imported')
print(imported)
