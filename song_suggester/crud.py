"""This file is almost capable of populating a DB of 5 relevant tables, mostly with the kaggle dataset, but also with API calls for artist_id and genre;
while not obvious, the Artist instances will have an attribute, 'genres';
bottom-line, if we populate these tables (especially Genre) with API calls, the web app can query the DB fast."""

import re
from time import sleep
import numpy as np
import pandas as pd
from .models import *
from .spotify_client import *
# from song_suggester.models import *           # in flask shell...
# from song_suggester.spotify_client import *   # ...import like this


#-------------------------------------------------------
# POPULATE THESE TABLES: ARTIST, SONG, AUDIO_FEATURES, RECOMMENDATION
#kg = pd.read_csv('spotify_tracks_metadata.csv', index_col=0); 

DB.drop_all(); 
DB.create_all(); 
"""
def load_DB_part1():
    # The kaggle csv file is too big for rate limits
    # for i in range(len(kg['spotify_id'])):
    for i in range(20):
        song_name = kg['song_name'][i]; 
        artist_name = kg['artist_name'][i]; 

        song_id, artist_id = retrieve_spotify_ids(
            song_name=song_name, artist_name=artist_name); 

        s0 = Song(
            id = song_id, 
            song_name = song_name, 
            artist_name = artist_name,
            artist_id = artist_id); 

        f0 = AudioFeatures(
            song_id = song_id,
            danceability = float(kg['danceability'][i]),
            energy = float(kg['energy'][i]), 
            key = int(kg['key'][i]),
            loudness = float(kg['loudness'][i]),
            mode = int(kg['mode'][i]),
            speechiness = float(kg['speechiness'][i]),
            acousticness = float(kg['acousticness'][i]),
            instrumentalness = float(kg['instrumentalness'][i]),
            liveness = float(kg['liveness'][i]),
            valence = float(kg['valence'][i]),
            tempo = float(kg['tempo'][i]),
            duration_ms = int(kg['duration_ms'][i]),
            time_signature = int(kg['time_signature'][i])); 

        a0 = Artist(id = artist_id, artist_name = artist_name); 

        DB.session.add(a0); # Artist
        DB.session.add(s0); # Song
        DB.session.add(f0); # AudioFeatures

        limit = 10; # default limit=20, max limit=100
        recommend_list = spotipy_recs(
            spotify_id = song_id,
            limit = limit); 

        for R in range(limit):
            r0 = Recommendation(
                rec_song_id = recommend_list[R][0],
                rec_song_name = recommend_list[R][1], 
                rec_artist_name = recommend_list[R][2], 
                song_id = song_id
            ); 
            DB.session.add(r0); # Recommendation
"""
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