from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from bson import ObjectId
import os

mongoURI = os.environ.get('dbConnectionString', None)
print(mongoURI)
client = MongoClient(mongoURI)
db = client.Quizzy
col = db.Quizes

app = Flask(__name__)
CORS(app)

@app.route('/quiz/<quizId>', methods=["GET"])
def get_quiz(quizId):
        quiz = {"_id":ObjectId(quizId)}
        x = col.find_one(quiz)
        output = {'name': x['name'], 'questions': x['questions']}
        return jsonify(output)
          
@app.route('/create', methods=["POST"])
def create_quiz():
        quiz = request.get_json()
        insertedQuiz = col.insert(quiz)
        returnQuiz = col.find_one({'_id': insertedQuiz})
        output = {'_id': str(returnQuiz['_id'])}
        return jsonify(output), 201


@app.route('/create', methods=["OPTIONS"])
def return_options():
        return '' , 200