'''Song_Suggester app logic'''
import os
from flask import Flask, render_template, request
from .models import *
from .spotify_client import *


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
            song_id, artist_id = retrieve_spotify_ids('superstition','stevie wonder')
            audio_features = retrieve_audio_features(song_id)
            genre_list = retrieve_genres(artist_name)
            recommend_list = spotipy_recs(song_id, limit=3) # nested list

        # ...

        return render_template(
            'base.html', title = 'home', songs = Song.query.limit(10).all())



    #...


    return app