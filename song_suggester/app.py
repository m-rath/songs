'''Song_Suggester app logic'''
import os
from flask import Flask, render_template, request
from sqlalchemy import func, distinct
from .model import df, DB, Song, DB_load
from .spotify_client import *


def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)

    # configure app
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize database
    DB.init_app(app)

    # create and insert into Song table
    with app.app_context():
        DB.create_all()
        # load_DB(); 


    @app.route('/', methods=["GET", "POST"])
    def root():     
        # ...

        # When visitor types song and artist then hits a button...
        if request.method == "POST":
            song_seed = request.form["song_name"]
            # artist_name = request.form["artist_name"]
            
            recomm = Song.query.limit(2).all() # put model output here
        # ...
        return render_template(
            'predict.html', title='home', song_seed=song_seed, recomm=recomm)

    #...
    return app