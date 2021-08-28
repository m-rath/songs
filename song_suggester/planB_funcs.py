"""some objects and functions supporting html actions and routes"""
import pickle
import numpy as np
import pandas as pd
import matplotlib as plt 
from scipy.spatial import distance
# from sqlalchemy import func, distinct
# from sqlalchemy.sql import expression #(.exists, .select, ...)
from .spotify_client import *


# unpickle a trained kmeans algorithm and cluster-distances 
kmeans_pipe = pickle.load(open('song_suggester\kmeans_pipe.sav', 'rb'))
df_index = pickle.load(open('song_suggester\df_index.sav', 'rb'))
song_space_locs = pickle.load(open('song_suggester\song_space_locs.sav', 'rb'))


def suggest_ids(song_name, artist_name, count=100):
    """Compares a track to ~440,000 others, based on 13 numeric audio features, and returns the spotify_ids of 35 songs with similar cluster-distance coordinates; it would be cool if a button press would display the next closest set.  It would be cooler if matplotlib displayed a 3D plot, with 3 drop-down menus for choosing any 3 features (of 13) for plot axes (or a 3D tSNE plot, not with audio features but with projections to abstract 3D space); and if the color of input song were bright color, similar to neighbors displayed in table, but different from the faded grey others"""
    song_id, artist_id = retrieve_spotify_ids(song_name, artist_name)
    
    features = retrieve_audio_features(song_id)    
    feats = ['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature']

    model_input = [features[0][feat] for feat in feats]
    song_space_base = kmeans_pipe.transform([model_input])
    dists = distance.cdist(song_space_locs, song_space_base, 'cityblock')
    dists = pd.DataFrame(dists, index=df_index).sort_values(by=0)[:count] #top10
    spotify_ids = dists.index

    return spotify_ids


def relevant_genres(tracks):
    artist_names = [track.artist_name for track in tracks]
    genres_nested_lists = [retrieve_genres(art) for art in artist_names]
    genre_list = [g for g_list in genres_nested_lists for g in g_list]

    return genre_list
