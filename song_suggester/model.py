# TODO: THIS IS ZOMBIE CODE WE NEED TO DELETE THIS
from flask_sqlalchemy import SQLAlchemy
import pandas as pd


# Our postgres table, 'song', inherits from flask_sqlalchemy starter DB.Model

DB = SQLAlchemy()

class Song(DB.Model):
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
<<<<<<< Updated upstream

#----------------------------------------------------------------------------
# Define a function to Create and Insert, i.e. load the DB

def DB_load(batch_size=1000):
    try:
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
    except SQLAlchemyError as e:
        print(e)
    finally:
        DB.session.close()


# Mark P. manually loaded DB from df (Aug 26 2021) in flask shell like this:
# DB.drop_all()
# DB.create_all()
# DB_load(batch_size=1000)
# DB.session.commit()

#loading in pickled KNN model
filename = '/home/greg/DS/songs/song_suggester/model_knn.pkl'

with open(filename, 'rb') as f:
    model_knn = pickle.load(f)
=======
>>>>>>> Stashed changes
