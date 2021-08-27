import pickle
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial.distance import cityblock
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.postgresql import *


DB = SQLAlchemy()


class Song(DB.Model):
    """Each row is a song and its spotify audio features"""
    __tablename__ = 'song'

    id = DB.Column(DB.String(25), primary_key=True) # Spotify ID for track
    song_name = DB.Column(DB.String(), nullable=False)
    artist_name = DB.Column(DB.String(), nullable=False)
    danceability = DB.Column(DB.Float)
    energy = DB.Column(DB.Float)
    key = DB.Column(DB.Integer)
    loudness = DB.Column(DB.Float)
    mode = DB.Column(DB.Integer)
    speechiness = DB.Column(DB.Float)
    acousticness = DB.Column(DB.Float)
    instrumentalness = DB.Column(DB.Float)
    liveness = DB.Column(DB.Float)
    valence = DB.Column(DB.Float)
    tempo = DB.Column(DB.Float)
    duration_ms = DB.Column(DB.BigInteger)
    time_signature = DB.Column(DB.Integer)

    def __repr__(self):
        return "<{}>".format(self.song_name)


def DB_load(batch_size=1000):
    for i in range(batch_size):
        song_row = Song(
            id = df['spotify_id'][i],
            song_name = df['song_name'][i], 
            artist_name = df['artist_name'][i], 
            danceability = float(df['danceability'][i]),
            energy = float(df['energy'][i]), 
            key = int(df['key'][i]),
            loudness = float(df['loudness'][i]),
            mode = int(df['mode'][i]),
            speechiness = float(df['speechiness'][i]),
            acousticness = float(df['acousticness'][i]),
            instrumentalness = float(df['instrumentalness'][i]),
            liveness = float(df['liveness'][i]),
            valence = float(df['valence'][i]),
            tempo = float(df['tempo'][i]),
            duration_ms = int(df['duration_ms'][i]),
            time_signature = int(df['time_signature'][i])) 
        DB.session.add(song_row)
    DB.session.commit()

df = pd.read_csv('spotify_tracks_metadata.csv', index_col = 0)
df.drop_duplicates(subset = 'spotify_id', ignore_index=True, inplace=True)

# DB.drop_all()
# DB.create_all()
# DB_load(batch_size=439889)
# DB.session.commit()
# DB.session.close()