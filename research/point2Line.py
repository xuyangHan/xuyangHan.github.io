from pymongo import MongoClient

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.Gulf_St_Lawrence_Data
MMSI_list = []

i = 1
for point in db.PointData.find():
    if i % 100 == 0:
        print(i)
    i = i + 1

    MMSI = point['MMSI']
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
            "BaseDateTimeStart": BaseDateTimeStart,
            "BaseDateTimeEnd": BaseDateTimeEnd,
            "Location": {
                "type": "LineString",
                "coordinates": [[Longitude, Latitude]]
            },
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
        db.lineData.insert_one(d)
    else:
        line = db.lineData.find_one({"MMSI": MMSI})

        BaseDateTimeEnd = point['BaseDateTime']
        db.lineData.update_one(
            {"MMSI": MMSI},
            {
                "$set": {
                    "BaseDateTimeEnd": BaseDateTimeEnd,
                }
            }
        )

        coordinates = line['Location']['coordinates']
        coordinates.append(point['Location']['coordinates'])
        db.lineData.update_one(
            {"MMSI": MMSI},
            {
                "$set": {
                    "Location": {
                        "type": "LineString",
                        "coordinates": coordinates
                    }
                }
            }
        )

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
                    "Velocity": {
                        "SOG": SOGs,
                        "COG": COGs,
                        "Heading": Headings,
                    },
                }
            }
        )
