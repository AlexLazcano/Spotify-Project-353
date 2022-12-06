import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from sklearn.neural_network import MLPClassifier


def main():
    data = pd.read_csv('genre-data.csv', index_col=0)

    # print(data)
    count = data.value_counts('given-genre')
    count = count[count > 100]
    # print(count.index.values)
    enoughData = count.index.values

    # only use data genres that have more than 100 data points
    data =data[data['given-genre'].isin(enoughData)]
    print(data.shape)
    y = data['given-genre']
    X = data.drop(['given-genre', 'genre','key', 'mode', 'id', 'song_title', 'popularity_scores', 'time_signature'], axis=1)
    
    X_train, X_valid, y_train, y_valid = train_test_split(X,y, test_size=0.15)
    # print(X)
    model = make_pipeline(
        # StandardScaler(),
        MinMaxScaler(),
        # KNeighborsClassifier(10)
        # RandomForestClassifier(n_estimators=150, max_depth=100, min_samples_split=20)
        MLPClassifier(solver='lbfgs', hidden_layer_sizes=(100, 50))
    )
    model.fit(X=X_train, y=y_train)

    
    y_predicted = model.predict(X_valid)
    print(classification_report(y_valid, y_predicted))
    print(model.score(X=X_train, y=y_train))
    print(model.score(X=X_valid, y=y_valid))

    print(y_predicted.shape)
    print(X_valid.shape)
    X_valid['ml'] = y_predicted
    ids = X_valid['ml']
    # valid['genre'] = y_predicted
    
    valid = pd.merge(data, ids, left_index=True, right_index=True)
    valid['result'] = valid['given-genre'] == valid['ml']
    valid = valid[['song_title','genre', 'given-genre', 'ml', 'result']]
    valid.to_csv('valid.csv')
   
    

if __name__ == '__main__':
    main()
    