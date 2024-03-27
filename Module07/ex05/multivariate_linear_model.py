# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multivariate_linear_model.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/27 19:21:57 by vafleith          #+#    #+#              #
#    Updated: 2024/03/27 20:51:39 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from mylinearregression import MyLinearRegression as MyLR


@dataclass
class Feature:
    model: MyLR
    data: np.ndarray
    colors: list[str]


def univariate_plots(data):
    myLR_age = MyLR(thetas=np.array([[600.0], [-1.0]]), alpha=2.5e-5, max_iter=100000)
    myLR_thrust = MyLR(thetas=np.array([[0.0], [20.0]]), alpha=2.5e-5, max_iter=100000)
    myLR_distance = MyLR(
        thetas=np.array([[750.0], [-5.0]]), alpha=2.5e-5, max_iter=100000
    )
    Y = np.array(data[["Sell_price"]])
    age_feat = Feature(
        myLR_age,
        np.array(data[["Age"]])[:, 0].reshape(-1, 1),
        ["midnightblue", "cornflowerblue"],
    )
    thrust_feat = Feature(
        myLR_thrust,
        np.array(data[["Thrust_power"]])[:, 0].reshape(-1, 1),
        ["forestgreen", "lime"],
    )
    distance_feat = Feature(
        myLR_distance,
        np.array(data[["Terameters"]])[:, 0].reshape(-1, 1),
        ["mediumorchid", "orchid"],
    )
    for feature in [age_feat, thrust_feat, distance_feat]:
        fit_and_plot_pred(feature, Y)


def fit_and_plot_pred(feature, Y):
    feature.model.fit_(feature.data, Y)
    y_hat = feature.model.predict_(feature.data)
    print(f"Loss: {feature.model.loss_(Y, y_hat)}")
    plt.scatter(feature.data, Y, color=feature.colors[0])
    plt.scatter(feature.data, y_hat, color=feature.colors[1], s=10)
    plt.show()


def multivariate_plots(data):
    X = np.array(data[["Age", "Thrust_power", "Terameters"]])
    Y = np.array(data[["Sell_price"]])
    my_lreg = MyLR(
        thetas=np.array([[300.0], [-20.0], [1.0], [1.0]]), alpha=1e-5, max_iter=500000
    )
    my_lreg.fit_(X, Y)
    print(my_lreg.thetas)
    y_hat = my_lreg.predict_(X)
    print(my_lreg.loss_(Y, y_hat))
    colors = [
        ["midnightblue", "cornflowerblue"],
        ["forestgreen", "lime"],
        ["mediumorchid", "orchid"],
    ]
    for i in range(3):
        plot_feat_pred_multivariate(X[:, i], y_hat, Y, colors[i])


def plot_feat_pred_multivariate(X, y_hat, Y, colors):
    plt.scatter(X, Y, color=colors[0])
    plt.scatter(X, y_hat, color=colors[1], s=10)
    plt.grid()
    plt.show()


def main():
    if len(sys.argv) != 2:
        sys.exit("You must add a csv file in argument.")
    data = pd.read_csv(sys.argv[1])
    # univariate_plots(data)
    multivariate_plots(data)


if __name__ == "__main__":
    main()
