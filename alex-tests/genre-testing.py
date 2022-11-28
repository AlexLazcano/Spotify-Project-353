import numpy as np
import pandas as pd
import math
import os
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import re


def main():
    songs_data = pd.read_csv('../data/playlists-v4-final.csv')
    # songs_data['genre'] = songs_data['genre'].astype('category')
    # print(songs_data)

    numeric_columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
               'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
                'duration_ms', 'time_signature',
               'popularity_scores']
               


    # clean genres
    # songs_data['genre'].drop_duplicates().sort_values().to_csv('data_genres.csv')
    
    songs_data['genre'].to_csv('data_genres_orignal.csv')
    # TODO: make k-pop and pop mutually exclusive
    regex = r'(k-pop|filmi|acoustic|corrido|bollywood|electro swing|cumbia|edm|instrumental|funk|blues|country|lo-fi|punk|folk|jazz|trap|soundtrack|reggae|salsa|bass|rap|soul|anime|ambient|metal|hip hop|country|classical|alt z|rock|r&b|rnb|indie|pop|disco|latin|alternative)'
    genres_data = songs_data['genre'].str.extract(regex,re.IGNORECASE, expand=False)
    all_genres_data = songs_data['genre'].str.extractall(regex,re.IGNORECASE)
    all_genres_data = all_genres_data.rename(columns={0:'given-genre'})
    # print("total: ", songs_data['genre'].count())
    # nonempty = genres_data[~genres_data.isnull()]
    empty = songs_data['genre'][genres_data.isnull()].dropna()
    notEmpty = genres_data[~genres_data.isnull()]
    notEmpty.to_csv('cleaned_genres.csv')
    print("count of extracted genres: ", notEmpty.count())
    # print(notEmpty.value_counts())
    print(all_genres_data.value_counts())
    all_genres_data = all_genres_data.reset_index().set_index('level_0')['given-genre']
    print("songs identified (with duplicate genres)",all_genres_data.count())
    joined = songs_data.join(all_genres_data, how='inner')
    # joined = joined[['song_title', 'genre', 'given-genre']]
    # joined.to_csv('given-genre.csv')

    generated_genres = all_genres_data.drop_duplicates().values
    print(generated_genres)

    # generate graphs of each song feature for each genre
    # for genre in generated_genres:
    #     genre_songs = joined[joined['given-genre'] == genre]
        
    #     popularity = genre_songs['popularity_scores']
    #     for col in numeric_columns: 
            
    #         plt.figure()
    #         plt.plot(genre_songs[col], popularity, '.')
    #         # plt.hist(genre_songs[col], 10)
    #         plt.title('genre: {}. {} vs popularity'.format(genre, col))
    #         exists = os.path.exists('../images/{}'.format(genre))
    #         if exists == False:
    #             os.mkdir('../images/{}'.format(genre))
            
    #         plt.savefig('../images/{}/{}'.format(genre,col))
    #         plt.close()

    mean = joined.groupby('given-genre').mean()
    print(mean.sort_values('popularity_scores', ascending=False))


    melt = joined[['given-genre', 'danceability']].melt()
    print(melt.dtypes)
    posthoc = pairwise_tukeyhsd(melt['value'], melt['variable'], alpha=0.05)
    print(posthoc)
        
    # print(empty.value_counts().to_csv('empty.csv'))
    # print(notEmpty)
    # empty.to_csv('empty.csv')
    
  
    # nonempty = nonempty.rename(columns={0: 'genre'})
    # test = nonempty.reset_index()
    # print(test)
    # gb = test.groupby('genre')['match'].count()
    # print(gb)
    # print(gb.sum())
    # nonempty.sort_values().to_csv('cleaned_genres.csv')
    # print(genres)



    # columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    #    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    #    'id', 'duration_ms', 'time_signature', 'song_title',
    #    'popularity_scores', 'genre']

    # print(songs_data.dtypes)
    # melt = songs_data[columns].melt()
    # posthoc = pairwise_tukeyhsd(melt['value'], melt['variable'], alpha=0.05)
    # print(posthoc)

    # graphs
    # for col in numeric_columns: 
    #     plt.figure()
    #     plt.plot(songs_data[col], songs_data['popularity_scores'], '.')
    #     plt.title(col)
    #     plt.savefig('../images/{}.png'.format(col))

    # chi square // contingency 
    # categorical = pd.cut(songs_data['popularity_scores'], range(0,100, 33), labels=['low', 'medium', 'high'])
    # # print(categorical)

    # contingency = pd.crosstab(songs_data['genre'], categorical)
    # print(contingency)

if __name__ == '__main__':
    main()
