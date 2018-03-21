from flask import Flask, render_template, request, jsonify
import random
import pprint
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['fullstack']

collection = db['entries']


app= Flask('__main__')

@app.route('/')
def main():
   return render_template('file.html')

@app.route('/id', methods=['POST'])
def id():
   
   name = request.form['name']
   entry = db.entries.find_one({'name': name})
   if entry:
      return 'name already exists'

   else:	
      id1 = random.randint(10000000, 90000000) 
      d = { 'name': name,
            'id' : id1
          }
      entries = db.entries
      entries = entries.insert_one(d)
      return str(id1)  

app.run(port=5002)



