# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 23:46:43 by vafleith          #+#    #+#              #
#    Updated: 2024/03/17 02:29:43 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from csvreader import CsvReader
import sys
import random
import matplotlib.pyplot as plt


class KmeansClustering:
    
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def init_centroids(self, X):
        min_val, max_val = np.min(X, axis=0), np.max(X, axis=0)
        self.centroids = [random.uniform(min_val, max_val) for _ in range(self.ncentroid)]
        # for _ in range(self.ncentroid):
        #     self.centroids.append(random.choice(X))

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.init_centroids(X)
        prev_centroids = None
        for _ in range(self.max_iter):
            sorted_points = self.predict(X)
            prev_centroids = self.centroids
            self.centroids = [np.mean(cluster, axis=0) for cluster in sorted_points]
            # print("Centroids shape:", [centroid.shape for centroid in self.centroids])
            # print("Prev centroids shape:", [centroid.shape for centroid in prev_centroids])
            for i, centroid in enumerate(self.centroids):
                if np.isnan(centroid).any():
                    self.centroids[i] = prev_centroids[i]
            # print("Centroids shape:", [centroid.shape for centroid in self.centroids])
            if np.equal(self.centroids, prev_centroids).all():
                break
        # print(sorted_points)


    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        sorted_points = [[] for _ in range(self.ncentroid)]
        for value in X:
            distances = []
            for centroid in self.centroids:
                distances.append(self.cosine_similarity(value, centroid))
            centroid_index = np.argmin(distances)
            sorted_points[centroid_index].append(value)
        return sorted_points

    @staticmethod
    def cosine_similarity(a, b):
        """
        Input :
        a : a numpy array representing data a as a vector
        b : a numpy array representing data b as a vector
        Output:
        cos_ab : a scalar proportional to the the similarity in angles between a and b
        """
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def parse_args(args):
    filepath, ncentroid, max_iter = None, None, None
    for arg in args:
        if arg.startswith("filepath=") and len(arg) > len("filepath="):
            filepath = arg.split('=')[1]
        if arg.startswith("ncentroid=") and len(arg) > len("ncentroid="):
            ncentroid = arg.split('=')[1]
        if arg.startswith("max_iter=") and len(arg) > len("max_iter="):
            max_iter = arg.split('=')[1]
    if filepath is None:
        sys.exit("ERROR : Filepath is mandatory.")
    if ncentroid is None or int(ncentroid) <= 1:
        ncentroid = 5
    if max_iter is None or int(max_iter) <= 1:
        max_iter = 20
    return filepath, ncentroid, max_iter


def plot_data(data):
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z)
    plt.show()


def plot_sorted_points(data, prediction):
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(projection='3d')
    for valx, valy, valz in zip(x, y, z):
        for i, cluster in enumerate(prediction):
            if np.equal(np.array([valx, valy, valz]), cluster).any():
            #if np.array([valx, valy, valz]).all() in cluster.any():
                if i == 0:
                    ax.scatter(valx, valy, valz, color='black')
                if i == 1:
                    ax.scatter(valx, valy, valz, color='green')
                if i == 2:
                    ax.scatter(valx, valy, valz, color='red')
                if i == 3:
                    ax.scatter(valx, valy, valz, color='blue')
    ax.scatter(x, y, z)
    plt.show()

def main():
    if not 1 < len(sys.argv) < 5:
        sys.exit("Usage: py Kmeans.py filepath='/path.csv' {ncentroid=4 max_iter=30}")
    filepath, ncentroid, max_iter = parse_args(sys.argv[1:])
    with CsvReader(filepath, skip_top=1) as file:
        data = np.array(file.getdata(), dtype=float)
    data = data[:, 1:]
    # plot_data(data)
    kmc = KmeansClustering(ncentroid=ncentroid, max_iter=max_iter)
    kmc.fit(data)
    prediction = kmc.predict(data)
    #print(prediction)
    plot_sorted_points(data, prediction)

if __name__ == "__main__":
    main()
