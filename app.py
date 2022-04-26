from flask import Flask, render_template, request, jsonify

from database.database import Database
from config import MYSQL_CONFIG

app = Flask(__name__, static_folder = "static", static_url_path = "/")

db = Database(MYSQL_CONFIG)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/messages", methods = ["POST"])
def upload_messages():
    data = request.get_json()

@app.route("/api/messages", methods = ["GET"])
def get_messages():
    sql = ("SELECT message, image_url FROM messages ORDER BY id DESC")
    sql_data = ()
    result = db.execute_sql(sql, sql_data)

    result_dict = {"data": result}

    return jsonify(result_dict)


app.run(port = "3000")