import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)) ** 2)

class KNN:
    def __init__(self, k=3):
        self.k = k
    #X_train espera um array 2D onde cada item tem uma cordenada x e y.
    #Y_train são os resultados das classificações.
    def fit(self, X, y):
        self.X_train = X
        self.Y_train = y
        
    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)
    
    def _predict(self, x):
        distance = [euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distance)[:self.k]
        k_nearest_label = [self.Y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_label).most_common(1)
        return most_common[0][0]
    