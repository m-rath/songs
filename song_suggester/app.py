'''Song_Suggester app logic'''
import os
from flask import Flask, render_template, request

from .app_funcs import *
from .spotify_client import *


def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)

    # configure app
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize database
    from .model import DB
    DB.init_app(app)

    @app.route('/', methods=["GET", "POST"])
    def root():     
        # ...

        # When visitor types song and artist then hits a button...
        if request.method == "POST":
            song_name = request.form["song_name"]
            artist_name = request.form["artist_name"]
            spotify_ids = suggest(song_name, artist_name)
                        = DB.session.query(Song).filter()



        # ...
        return render_template(
            'predict.html', title='home', song_name, artist_name, suggest=suggest)

    #...
    return app