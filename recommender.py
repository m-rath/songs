#creating a class that can take this data and generate recommendations as a result. 

class Spotify_Recommendation():
    def __init__(self, database):
        self.database = database
    def recommend(self, songs, amount=1):
        distance = [] #list will hold the "distance" of the features column values from one another, the closer the numbers, the more likely they are to be recommended
        song = self.database[(self.database.song_name.str.lower() == songs.lower())].head(1).values[0]
        rec = self.database[self.database.song_name.str.lower() != songs.lower()]
        for songs in features(rec.values):
            d = 0
            for cols in np.arange(len(rec.columns)):
                if not col in [1, 6, 12, 14, 18]:
                    d = d + np.absolute(float(song[col]) - float(songs[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['artists', 'name']
        return rec[columns][:amount]

recommendations = Spotify_Recommendation(df)
recommendations.recommend("Blinding Lights", 10)
