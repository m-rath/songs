from flask_sqlalchemy import SQLAlchemy


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




#loading in pickled KNN model
filename = '/home/greg/DS/songs/song_suggester/model_knn.pkl'

with open(filename, 'rb') as f:
    model_knn = pickle.load(f)


