from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = '' #DB NAME
app.config['MONGO_URI'] = 'mongodb://localhost:27017 DB NAME' # DB NAME

mongo = PyMongo(app)

@app.route('/people', methods=['GET'])
def get_all_people():
    people = mongo.db.mycol #collection name

    output = []

    for q in people.find():
         output.append({ 'Name' : q['Name'], 'Age' : q['Age'], })

    return jsonify ({'result' : output})

@app.route('/people/<Name>', methods=['GET'])
def get_one_person(Name):
    get_one_person = mongo.db.mycol

    q = get_one_person.find_one({'Name' : Name})
    
    if q:
        output = {'Name' : q['Name'], 'Age' : q['Age']}
    else:  
        output = ['No Results Found']
    return jsonify({'result' : output})

@app.route('/people', methods=['POST'])
def add_people():
    add_people = mongo.db.mycol

    name = request.json['Name']
    Age = request.json['Age']
 

    people_id = add_people.insert({'Name' : name, 'Age' : Age})
    new_people = add_people.find_one({'_id' : people_id})

    output = {'Name' : new_people['Name'],  'Age' : new_people['Age'],}

    return jsonify ({'result' : output})


if __name__ == "__main__":
    app.run(debug=True)