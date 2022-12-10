
data: 

generate_track_data.py: is the file while generated playlist data which converts to song data to turn into csvs
- but requires Daniel Tham's API key/secret API key to Spotify 

clean_track_data.ipynb: cleaned the playlists-v4.csv to create the playlists-v4-final.csv


Analysis Scripts and Python Notebooks:

in genre-testing: 
genre-generation.py - generates genre data in genre-data.csv. Used in ml-genre.py and in stats-genre.
python3 genre-testing.py

stats-genre.py - statistical analysis of genre data.
python3 stats-genre.py

ml-genre.py - machine learning models for genre data.
python3 ml-genre.py

classifiers.ipynp - normalization of datasets using MinMaxScaler and StandardScaler and usage of RFE for feature selection to improve results.
                  - construction a model using Random Forest, K-Nearest Neighbor, Decision Tree Classifier, Gaussian Naive-Bayes, and SVM.
                  - Grid-Search on Random Forest, Decision Tree and K-Nearest Neighbors 
                  - results using cross-validation 



images: 
images used in the report that were created in the genre-testing folder. 
