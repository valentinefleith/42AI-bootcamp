# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 23:46:43 by vafleith          #+#    #+#              #
#    Updated: 2024/03/16 20:32:17 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from csvreader import CsvReader
import sys
import random
import matplotlib.pyplot as plt

class KmeansClustering:
    
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

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
        for _ in range(self.ncentroid):
            self.centroids.append(random.choice(X))

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
        #... your code ...

    @staticmethod
    def cosine_similarity(a, b):
        """
        Input :
        a : a numpy array representing word a as a vector
        b : a numpy array representing word b as a vector
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
    if ncentroid is None:
        ncentroid = 5
    if max_iter is None:
        max_iter = 20
    return filepath, ncentroid, max_iter


def plot_data(data):
    x = data[:, 1]
    y = data[:, 2]
    z = data[:, 3]
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z)
    plt.show()


def main():
    if not 1 < len(sys.argv) < 5:
        sys.exit("Usage: py Kmeans.py filepath='/path.csv' {ncentroid=4 max_iter=30}")
    filepath, ncentroid, max_iter = parse_args(sys.argv[1:])
    with CsvReader(filepath, skip_top=1) as file:
        data = np.array(file.getdata(), dtype=float)
    plot_data(data)
    kmc = KmeansClustering(ncentroid=ncentroid, max_iter=max_iter)
    kmc.fit(data)

if __name__ == "__main__":
    main()
