'''Song_Suggester app logic'''
import os
from flask import Flask, render_template, request
from .model import DB, Song, model_knn
from .spotify_client import *
from .app_funcs import *


def create_app():
    """Create and configure an instance of the flask application"""
    app = Flask(__name__)
    DATABASE_URL=os.getenv('DATABASE_URL')
    
    """
    DATABASE_URL=postgresql+psycopg2://
    DB_NAME=os.getenv('DB_NAME')
    DB_USER=os.getenv('DB_USER')
    DB_PW=os.getenv('DB_PW')
    DB_PORT=os.getenv('DB_PORT')
    DB_HOST=os.getenv('DB_HOST')
    app.config["SQLALCHEMY_DATABASE_URI"] = f'{DATABASE_URL}{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}{DB_NAME}'
    """
    # configure app
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize database
    DB.init_app(app)

    # create table(s)
    with app.app_context():
        DB.create_all()
        # load_DB(); 

   # ROOT ROUTE
    @app.route('/', methods=["GET", "POST"])
    def root():     
        """Base view"""
        resp = None
        # When visitor types song and artist then hits a button...
        if request.method == "POST":
            song_name = request.form["song_name"]
            artist_name = request.form["artist_name"]






        resp = Song.query.limit(5).all()

        return render_template(
            'predict.html', title = 'home', recommended = resp)
    return app
