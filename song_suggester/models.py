from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

class Song(DB.Model):
    id = DB.Column(DB.String(25), primary_key=True)
    song_name = DB.Column(DB.String(), nullable=False) # not in audio_features
    artist_name = DB.Column(DB.String(), nullable=False) # not in audio_features
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
        return "<{} + 'by' + {}>".format(self.song_name, self.artist_name)