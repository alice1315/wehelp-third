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


@app.route("/api/messages", methods = ["GET"])
def get_messages():
    sql = ("SELECT message, image_url FROM messages ORDER BY id")
    sql_data = ()
    result = db.execute_sql(sql, sql_data)

    result_dict = {"data": result}

    return jsonify(result_dict)


@app.route("/api/messages", methods = ["POST"])
def upload_messages():
    # Get request data
    message = request.form["message"]
    file = request.files["file"]
    filename = file.filename

    if (not message or not file):
        return make_response(jsonify({"error": True, "message": "No data"}), 400)

    else:
        # Upload image
        s3.upload_file(file.read(), filename)
        file_url = "https://dhobt9qjfs77v.cloudfront.net/wehelp/" + filename

        # Insert data into rds
        sql = ("INSERT INTO messages (message, image_url) VALUES (%s, %s)")
        sql_data = (message, file_url)
        db.execute_sql(sql, sql_data, commit=True)

        result_dict = {"data": {"message": message, "image_url": file_url}}

        return jsonify(result_dict)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "3000")
