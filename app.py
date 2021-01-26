from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

@app.route("/api/v1.0/precipitation")


@app.route("/api/v1.0/stations")


@app.route("/api/v1.0/tobs")

@app.route("/api/v1.0/<start>")


@app.route("/api/v1.0/<start>/<end>")

