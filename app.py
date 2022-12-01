from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Define client varible with connection to MongoDB local database on port 27017
client = MongoClient('localhost', 27017)

# references to database from MongoDB and the todos collection
db = client.flask_db
todos = db.todos