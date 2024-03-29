# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/25 18:06:14 by vafleith          #+#    #+#              #
#    Updated: 2024/03/26 18:32:37 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from my_linear_regression import MyLinearRegression
from z_score import zscore


def main():
    # x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
    # y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
    y = zscore(np.array(
        [
            [63.00411131],
            [188.7195836],
            [182.05061623],
            [229.9012351],
            [194.15322434],
            [97.81371619],
            [219.13068803],
            [214.88202099],
            [282.65535451],
            [167.90620099],
            [215.8055732],
            [294.30539111],
            [227.01964445],
            [248.31781113],
            [179.26640301],
            [226.75047089],
            [373.24210857],
            [318.80746027],
            [391.48479314],
            [263.82596797],
            [333.36397535],
            [278.18737672],
            [434.87120181],
            [479.66713842],
            [343.93787107],
            [372.41235342],
            [392.11400554],
            [344.32442201],
            [384.24218543],
            [429.47730754],
            [509.69403412],
            [553.43422758],
            [559.17442405],
            [403.43185053],
            [544.39025059],
            [470.17919056],
            [561.9046634],
            [479.385147],
            [586.09404783],
            [536.64688616],
        ]
    ))
    x = zscore(np.arange(len(y)))
    # lr1 = MyLinearRegression(np.array([[-1], [2]]))
    # y_hat = lr1.predict_(x)
    # print(y_hat)
    # print(lr1.loss_elem_(y, y_hat))
    # print(lr1.loss_(y, y_hat))
    # lr1.plot_(x, y)
    # lr1.fit_(x, y)
    lr2 = MyLinearRegression(np.array([[5], [1]]), max_iter=15000, alpha=0.001)
    lr2.fit_(x, y)
    lr2.plot_pred(x, y)
    lr2.plot_grad_desc()
    lr2.plot_loss(x, y)
    print(lr2.thetas)
    y_hat = lr2.predict_(x)
    print(lr2.loss_(y, y_hat))


if __name__ == "__main__":
    main()
