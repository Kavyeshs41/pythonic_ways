import json

from flask_pymongo import PyMongo
from flask import Flask
from flask import jsonify
from flask import Response

app = Flask(__name__)

app.config['MONGODB_NAME'] = 'hire_scikey'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/hire_scikey'

mongo = PyMongo(app)

@app.route('/getDetails', methods = ['GET'])
def all_details():
    data = mongo.db.analytics_datas
    op = []
    for s in data.find({"city": "Pune"}):
        op.append({'_id' : s['_id'], 'browser' : s['browser']})
    resp = Response(json.dumps(op, default=str))
    resp.headers["content-type"] = "application/json"
    return resp


if __name__ == '__main__':
    app.run(debug=True)
