from flask import Flask, g, render_template, request
import sqlite3
import json

app = Flask(__name__)

DATABASE = 'sql/harassment-labels.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def update_db(query, args=()):
    print(query)
    print(args)
    cur = get_db().cursor()
    cur.execute(query, args)
    get_db().commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init():
    pass

@app.route("/")
def hello():
    return render_template('index.html') 

@app.route("/<username>", methods=["GET" , "POST"])
def process(username):
    if username != 'kumarde' and username != 'zzma':
        return 'go away.'
    if request.method == "GET":
        todo = query_db('SELECT * from ' + username + ' WHERE isVerified = 0')
        out_array = []
        for elem in todo:
            new_tuple = (str(elem[0]), elem[1], elem[2], elem[3], elem[4])
            out_array.append(new_tuple)
        return render_template('request.html', username=username, requests=json.dumps(out_array))
    elif request.method == "POST":
        postData = json.loads(request.data)
        tweetID = int(postData['tweetID'])
        answer = 1 if postData['answer'] == "Yes" else 0
        update_db('UPDATE ' + username + ' SET isVerified = ?, answer = ? WHERE id = ?', args=(1, answer, tweetID))
        return 'done'
