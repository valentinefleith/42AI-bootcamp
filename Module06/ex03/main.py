# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/25 23:25:04 by vafleith          #+#    #+#              #
#    Updated: 2024/03/26 00:04:29 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd
import numpy as np
from my_linear_regression import MyLinearRegression as MyLR

def main():
    if len(sys.argv) != 2:
        sys.exit("You must add a csv file in argument.")
    data = pd.read_csv(sys.argv[1])
    Xpill = np.array(data['Micrograms']).reshape(-1,1)
    Yscore = np.array(data['Score']).reshape(-1,1)
    linear_model1 = MyLR(np.array([[89.0], [-8]]))
    linear_model2 = MyLR(np.array([[89.0], [-6]]))
    Y_model1 = linear_model1.predict_(Xpill)
    Y_model2 = linear_model2.predict_(Xpill)
    print(linear_model1.loss_(Yscore, Y_model1) * 2)
    print(linear_model2.loss_(Yscore, Y_model2) * 2)
    linear_model1.fit_(Xpill, Yscore)
    linear_model1.plot_pred(Xpill, Yscore)
    linear_model1.plot_loss(Xpill, Yscore)


if __name__ == "__main__":
    main()
