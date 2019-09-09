from pymongo import MongoClient

mongo_client = MongoClient(host='csb-comren.eng.yorku.ca', port=27017,
                           username='admin',
                           password='pse212')
db = mongo_client.Gulf_St_Lawrence_Data

i = 1
for line in db.lineData.find():
    print(i)
    i = i + 1

    MMSI = line['MMSI']
    if len(line['Location']['coordinates']) < 2:
        db.lineData.update_one(
            {"MMSI": MMSI},
            {
                "$set": {
                    "DeleteStatus": True
                }
            }
        )

print('Flag documents to be deleted. Done. \n')

db.lineData.delete_many({"DeleteStatus": True})
print('Documents deleted. Done. \n')

