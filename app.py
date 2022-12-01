from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Define client varible with connection to MongoDB local database on port 27017
client = MongoClient('localhost', 27017)

# references to database from MongoDB and the todos collection
db = client.flask_db
todos = db.todos

# route serves as Home page
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        # get form and priorty content
        content = request.form['content']
        degree = request.form['priority']

        # in the database, insert the content and priority
        todos.insert_one({'content': content, 'priority': degree})
        return redirect(url_for('index'))

    # this finds all the todos and passes them into the index file.
    all_todos = todos.find() # Add this line outside the if block! 
    return render_template('index.html', todos=all_todos) # add todos here! 

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))