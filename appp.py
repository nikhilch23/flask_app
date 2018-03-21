from flask import Flask, render_template, request, jsonify
import random
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['fullstack']

collection = db['entries']


app= Flask('__main__')

@app.route('/')
def main():
   return render_template('text.html')

@app.route('/id', methods=['POST'])
def find_id():
   
   name = request.form['name']

   if collection.find_one({'name': name}):
      return 'name already exists and its id is {}'.format(collection.find_one({'name': name})['id'])

   else:	
      id1 = random.randint(10000000, 90000000) 
      d = { 'name': name,
            'id' : id1
          }

      collection.insert_one(d)
      return str(id1)  


@app.route('/name', methods=['POST'])
def find_name():
   id1 = request.form['id']
   dic = collection.find_one({'id': int(id1)})
   if dic:
      return 'Your respective name is {}'.format(dic['name'])
   else:
      return "Wrong ID, please type again."

app.run(port=5002)



