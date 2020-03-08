from flask import Flask, jsonify, json
from pymongo import MongoClient
from bson import json_util
# from bson.objectid import ObjectId
# https://docs.mongodb.com/manual/tutorial/query-documents/      //pour les command de mongodb.

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
mydb = client.mydb


@app.route('/<user>')
def api(user):

    nbr = mydb.etudiant.find_one({'firstname': str(user)})
    # print(nbr)

    if nbr == None:
        return "n'exist pas"
    else:
        return json.loads(json_util.dumps(nbr))


if __name__ == '__main__':
    app.run(debug=True)
