# Readme

This repository contains data, scripts, and notebooks for analyzing playlist data and generating genre classification models.

## Data

The following data files are included in this repository:

- **playlists-v4.csv**: Raw playlist data, generated using the `generate_track_data.py` script. This script uses Daniel Tham's Spotify API key, so the data file is not included in this repository.
- **playlists-v4-final.csv**: Cleaned version of the `playlists-v4.csv` file, generated using the `clean_track_data.ipynb` Jupyter notebook.

## Analysis Scripts and Python Notebooks

The `genre-testing` folder contains the following scripts and notebooks:

- **genre-generation.py**: Generates genre data in `genre-data.csv`. This file is used in `ml-genre.py` and `stats-genre.py`.
- **genre-testing.py**: Main script for testing genre classification models.
- **stats-genre.py**: Performs statistical analysis of genre data.
- **ml-genre.py**: Contains machine learning models for genre classification.

To run the scripts, use the following commands:

<code>
python3 genre-testing.py
python3 stats-genre.py
python3 ml-genre.py
</code>

The `analyse.ipynp` and `classifiers.ipynp` notebooks contain further analysis of the data, including exploration with scatterplots, bar plots, histograms, box plots, and a correlation chart. The `classifiers.ipynp` notebook also includes normalization of datasets using `MinMaxScaler` and `StandardScaler`, feature selection with `RFE`, and construction of classifier models using `RandomForestClassifier`, `KNeighborsClassifier`, `DecisionTreeClassifier`, `GaussianNB`, and `SVC`.

## Images

The `images` folder contains images used in the report, which were generated using the scripts in the `genre-testing` folder.
