from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
MONGODB_URI = "mongodb+srv://subratap6060_db_user:DIQMuweCZAKPS7pY@cluster0.zeiczov.mongodb.net"
client = MongoClient(MONGODB_URI)
db = client["myData"]
collection = db["myData"]


@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/save", methods=["POST"])
def save_data():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"message": f"Data inserted with ID: {result.inserted_id}"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=50000)
