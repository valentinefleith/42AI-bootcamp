# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multivariate_linear_model.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/27 19:21:57 by vafleith          #+#    #+#              #
#    Updated: 2024/03/27 20:07:56 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR


def fit_and_plot_pred(myLR, X, Y, colors):
    myLR.fit_(X, Y)
    y_hat = myLR.predict_(X)
    plt.scatter(X, Y, color=colors[0])
    plt.scatter(X, y_hat, color=colors[1], s=10)
    plt.show()

    
def main():
    if len(sys.argv) != 2:
        sys.exit("You must add a csv file in argument.")
    data = pd.read_csv(sys.argv[1])
    X = np.array(data[['Age']])[:, 0].reshape(-1, 1)
    AGE = np.array(data[['Sell_price']])
    myLR_age = MyLR(thetas=np.array([[600.0], [-1.0]]), alpha=2.5e-5, max_iter=100000)
    colors_age = ["midnightblue", "cornflowerblue"]
    THRUST = np.array(data[['Thrust_power']])
    myLR_thrust = MyLR(thetas=np.array([[0.0], [20.0]]), alpha=2.5e-5, max_iter=100000)
    colors_thrust = ["forestgreen", "lime"]
    DISTANCE = np.array(data[['Terameters']])
    myLR_distance = MyLR(thetas=np.array([[750.0], [-5.0]]), alpha=2.5e-5, max_iter=100000)
    colors_distance = ["mediumorchid", "orchid"]
    fit_and_plot_pred(myLR_age, X, AGE, colors_age)
    fit_and_plot_pred(myLR_thrust, X, THRUST, colors_thrust)
    fit_and_plot_pred(myLR_distance, X, DISTANCE, colors_distance)


if __name__ == "__main__":
    main()
