from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



engine = create_engine("sqlite:///./Resources/hawaii.sqlite")


Base = automap_base()

Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
app = Flask(__name__)


@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

session = Session(engine)

date = dt.datetime(2016, 8, 23)

plot_results = session.query(Measurement.prcp, Measurement.date).\
    filter(Measurement.date >= date).\
    order_by(Measurement.date.desc()).all()
return jsonify(plot_results)

@app.route("/api/v1.0/stations")


@app.route("/api/v1.0/tobs")

@app.route("/api/v1.0/<start>")


@app.route("/api/v1.0/<start>/<end>")

