import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from bson import ObjectId
import os

mongoURI = os.environ.get('dbConnectionString', None)
client = MongoClient(mongoURI)
db = client.Quizzy
col = db.Quizes

app = Flask(__name__)
CORS(app)

# Formats quiz into correct format
def format_quiz(quiz):
        return { 'id': str(quiz['_id']), 'name': quiz['name'], 'questions': quiz['questions']}

# Get quiz by ID
@app.route('/quiz/<quizId>', methods=["GET"])
def get_quiz(quizId):
        quiz = {"_id":ObjectId(quizId)}
        x = col.find_one(quiz)
        output = format_quiz(x)
        return jsonify(output)

# Get random quiz
@app.route('/random', methods=["GET"])
def get_random():
        random = list(col.aggregate([
                { '$match': { 'public': True } },
                { "$sample": { "size": 1 } }
        ]))

        return jsonify(format_quiz(random[0]))
          
# Create single quiz
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