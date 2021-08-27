
import re
from time import sleep
import numpy as np
import pandas as pd
# from .models import *
# from .spotify_client import *
from song_suggester.models import *           # in flask shell...
from song_suggester.spotify_client import *   # ...import like this

#----------------------------------------------------------------------------
# We found our dataset at <https://www.kaggle.com/luckey01/test-data-set>

#kg = pd.read_csv('spotify_tracks_metadata.csv', index_col=0); 

#----------------------------------------------------------------------------

DB.drop_all(); 
DB.create_all(); 



s0 = Song(
    id = song_id, 

    song_name = kg['song_name'][0]; 
    artist_name = kg['artist_name'][0]; 

    danceability = float(kg['danceability'][0]),
    energy = float(kg['energy'][0]), 
    key = int(kg['key'][0]),
    loudness = float(kg['loudness'][0]),
    mode = int(kg['mode'][0]),
    speechiness = float(kg['speechiness'][0]),
    acousticness = float(kg['acousticness'][0]),
    instrumentalness = float(kg['instrumentalness'][0]),
    liveness = float(kg['liveness'][0]),
    valence = float(kg['valence'][0]),
    tempo = float(kg['tempo'][0]),
    duration_ms = int(kg['duration_ms'][0]),
    time_signature = int(kg['time_signature'][0])); 

a0 = Artist(id = artist_id, artist_name = artist_name); 

DB.session.add(a0); # Artist
DB.session.add(s0); # Song
DB.session.add(f0); # AudioFeatures
DB.session.commit(); 

#-------------------------------------------------------------

recommend_list = spotipy_recs(
    spotify_id = song_id,
    limit = 2); 

r0 = Recommendation(
    rec_song_id = recommend_list[0][0],
    rec_song_name = recommend_list[0][1], 
    rec_artist_name = recommend_list[0][2], 
    song_id = song_id
); 

r1 = Recommendation(
    rec_song_id = recommend_list[1][0],
    rec_song_name = recommend_list[1][1], 
    rec_artist_name = recommend_list[1][2], 
    song_id = song_id
); 


DB.session.add(r0); # Recommendation

DB.session.commit(); 


#-----------------------------------------------------------
# POPULATE THE GENRE TABLE COMPLETELY

def load_DB_part2():
    genre_set = SPOTIPY_API.recommendation_genre_seeds()['genres']
    for genre in genre_set:
        g = Genre(genre=genre); 
        DB.session.add(g); 
    DB.session.commit(); 

    # FOR EACH ARTIST, RETRIEVE AND APPEND GENRES; 
    for A in Artist.query.all():
        artist_genre_zone = retrieve_genres(artist_name = A.artist_name); 
        for Z in artist_genre_zone:
            A.genres.append(Genre.query.filter_by(genre=Z).one()); 
            DB.session.add(A); 
    DB.session.commit()