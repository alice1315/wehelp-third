from flask import Flask, render_template, request, jsonify, make_response

from models.database import Database
from models.s3 import S3
from config import MYSQL_CONFIG

app = Flask(__name__, static_folder = "static", static_url_path = "/")

db = Database(MYSQL_CONFIG)
s3 = S3()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/messages", methods = ["POST"])
def upload_messages():
    # Get request data
    file = request.files["file"]
    message = request.form["message"]

    filename = file.filename
    if filename == "":
        return "No file"
    else:
        s3.upload_file(file.read(), filename)
        return "ok"

@app.route("/api/messages", methods = ["GET"])
def get_messages():
    sql = ("SELECT message, image_url FROM messages ORDER BY id DESC")
    sql_data = ()
    result = db.execute_sql(sql, sql_data)

    result_dict = {"data": result}

    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(port = "3000")
