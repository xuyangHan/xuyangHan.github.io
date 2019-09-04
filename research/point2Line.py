from pymongo import MongoClient

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.Gulf_St_Lawrence_Data
MMSI_list = []

for point in db.pointData.find():
    MMSI = point['MMSI']
    if MMSI not in MMSI_list:
        BaseDateTimeStart = point['BaseDateTime']
        BaseDateTimeEnd = point['BaseDateTime']
        Longitude = point['location']['coordinates'][0]
        Latitude = point['location']['coordinates'][1]
        SOG = point['SOG']
        COG = point['COG']
        Heading = point['Heading']
        VesselName = point['VesselName']
        IMO = point['IMO']
        CallSign = point['CallSign']
        VesselType = point['VesselType']
        Length = point['Length']
        Width = point['Width']
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
            "SOG": SOG,
            "COG": COG,
            "Heading": Heading,
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
        coordinates = line['location']['coordinates']
        coordinates.append(point['location']['coordinates'])
        db.lineData.update_one(
            {"MMSI": MMSI},
            {
                "$set": {
                    "location": {
                        "type": "LineString",
                        "coordinates": coordinates
                    }
                }
            }
        )

