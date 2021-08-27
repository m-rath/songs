"""
FROM FLASK SHELL, POPULATE DATABASE AND PICKLE KMEANS MODEL AND TRANSFORMED CLUSTER-DISTANCE SONG COORDINATES (SEE SKLEARN DOCS FOR DETAILS)

SPOTIFY DATASET FROM <https://www.kaggle.com/luckey01/test-data-set>"""

import pickle
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from song_suggester.model import *

#---------------------------------------------------------------

# csv_file too big for github repository
csv_file = 'spotify_tracks_metadata.csv'

df = pd.read_csv(csv_file, index_col = 0)
df.drop_duplicates(subset = 'spotify_id', ignore_index=True, inplace=True)
df_index = df['spotify_id']

# these columns align with audio features from spotify's API, conveniently 
feats = ['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature']
df = df[feats]

# fit the model, get locations in song-feature-space, relative to clusters
kmeans_pipe = Pipeline(steps = [
    ('scaler', StandardScaler()), 
    ('kmeans', KMeans(n_clusters = 5, n_init = 10))
    ])
song_space_locs = kmeans_pipe.fit_transform(df)

# save the pickles in app folder for heroku deployment
pickle.dump(kmeans_pipe, open('kmeans_pipe.sav', 'wb'))
pickle.dump(df_index, open('df_index.sav', 'wb'))
pickle.dump(song_space_locs, open('song_space_locs.sav', 'wb'))

# when batch_size = len(df), 439889 songs load into postgresql DB in 4 minutes
DB.drop_all()
DB.create_all()
DB_load(batch_size=439889)
DB.session.commit()
DB.session.close()