import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['fullstack']

collection = db['entry']

post={'name':'nik', 
      'roll':'17hs20022',
      'class':'13'}

entry = db.entry
entry = entry.insert_one(post)



