'''Song_Suggester app logic'''
import os
from flask import Flask, render_template, request
from .model import DB, Song
from .spotify_client import *
from .app_funcs import *


def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)

    # configure app
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize database
    DB.init_app(app)

    # create table(s)
    with app.app_context():
        DB.create_all()

    # ROOT ROUTE
    @app.route('/', methods=["GET", "POST"])
    def root():     
        # ...

        # When visitor types song and artist then hits a button...
        if request.method == "POST":
            song_name = request.form["song_name"]
            artist_name = request.form["artist_name"]
            spotify_ids = suggest_ids(song_name, artist_name)
            # = DB.session.query(Song).filter(Song.id in )

        # ...

        return render_template(
            'predict.html', title='home', song_name=song_name, artist_name=artist_name, suggest=suggest)


    return app