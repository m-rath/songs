from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table

DB = SQLAlchemy()

class Song(DB.Model):
    __tablename__ = 'song'
    id = DB.Column(DB.String(25), primary_key=True) # Spotify ID for track
    song_name = DB.Column(DB.String(), nullable=False)
    artist_name = DB.Column(DB.String(), nullable=False)
    artist_id = DB.Column(DB.String(), DB.ForeignKey('artist.id'))

    artist = DB.relationship('Artist', 
        backref = DB.backref('songs', uselist=False))

    def __repr__(self):
        return "<{}>".format(self.song_name)


association_table = Table('association', DB.metadata,
    DB.Column('genre_id', DB.ForeignKey('genre.id'), primary_key=True),
    DB.Column('artist_id', DB.ForeignKey('artist.id'), primary_key=True))


class Artist(DB.Model):
    __tablename__ = 'artist'
    """THIS IS NOT A UNIQUE PKEY"""
    id = DB.Column(DB.String(25), primary_key=True) # Spotify ID for artist
    artist_name = DB.Column(DB.String(), nullable=False)

    genres = DB.relationship('Genre',
        secondary = association_table,
        backref = 'artists')

    def __repr__(self):
        return "<{}>".format(self.artist_name)


class Genre(DB.Model):
    __tablename__ = 'genre'
    id = DB.Column(DB.Integer, primary_key=True)
    genre = DB.Column(DB.String(), nullable=False, unique=True)

    def __repr__(self):
        return "<{}>".format(self.genre)


class Recommendation(DB.Model):
    __tablename__ = 'recommendation'
    id = DB.Column(DB.Integer(), primary_key=True)
    rec_song_id = DB.Column(DB.String())
    rec_song_name = DB.Column(DB.String(), nullable=False)
    rec_artist_name = DB.Column(DB.String(), nullable=False)
    song_id = DB.Column(DB.ForeignKey('song.id'), nullable=False)

    song = DB.relationship("Song", 
        backref=DB.backref('recommendations', lazy=True))

    def __repr__(self):
        return "<'{}' by {}>".format(self.rec_song_name, self.rec_artist_name)


class AudioFeatures(DB.Model):
    __tablename__ = 'audio_features'
    id = DB.Column(DB.Integer, primary_key=True) 
    song_id = DB.Column(DB.ForeignKey('song.id'), unique=True, nullable=False)
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

    song = DB.relationship("Song", 
        backref=DB.backref('audio_features', lazy=True))
    
    def __repr__(self):
        return "Like songs? Register at Spotify! <https://open.spotify.com/>"