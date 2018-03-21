import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['fullstack']

collection = db['entries']

post={'name':'nikhil', 
      'roll':'17hs20022',
      'class':'13'}

entries = db.entries
entries = entries.insert_one(post)



