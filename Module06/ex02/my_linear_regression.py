# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/25 09:41:43 by vafleith          #+#    #+#              #
#    Updated: 2024/03/25 17:39:32 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt


class MyLinearRegression:
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas
        self.gradient_history = []
        self.thetas_history = [thetas]

    def loss_elem_(self, y, y_hat):
        if np.shape(y) != np.shape(y_hat):
            return None
        return np.square(y - y_hat)

    def loss_(self, y, y_hat):
        """
        Computes the half mean squared error of 2 non-empty np arrays, without
        any loop. The 2 arrays must have the same dimensions.
        Args:
            y: has to be a np.array
            y_hat: had to be a np.array
        Returns:
            The half mean squared error of the 2 vectors as a float.
            None if y or y_hat are empty.
            None if y and y_hat do not share the same dimensions.
        Raises:
            This function should not raise any Exceptions.
        """
        loss_elem = self.loss_elem_(y, y_hat)
        if loss_elem is None:
            return loss_elem
        return np.mean(loss_elem) / 2

    def predict_(self, x):
        """Computes the vector of prediction y_hat from 2 non-empty np arrays.
        Args:
            x: has to be a np array, a vector of dimension m * 1.
            theta: has to be an np array, a vector of dimension 2 * 1.
        Returns:
            y_hat as a np array, a vector of dimension m*1.
            None if x and/or theta are not numpy.array.
            None if x or theta are empty np arrays.
            None if x or theta dimensions are not appropriate.
        Raises:
            This function should not raise any Exceptions.
        """
        x = self.add_intercept(x)
        if x is None:
            return None
        return np.dot(x, self.thetas)

    def gradient_(self, x, y):
        """
        Computes a gradient vector from three non-empty numpy.array, without any for loop.
        The three arrays must have compatible shapes.
        Args:
            x: has to be a numpy.array, a matrix of shape m * 1. 
            y: has to be a numpy.array, a vector of shape m * 1.
            theta: has to be a numpy.array, a 2 * 1 vector.
        Return:
            The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
            None if x, y, or theta is an empty numpy.ndarray.
            None if x, y and theta do not have compatible dimensions.
        Raises:
            This function should not raise any Exception.
        """
        x_prime = self.add_intercept(np.copy(x))
        if x_prime is None:
            return None
        y_hat = self.predict_(x.flatten())
        if y_hat is None:
            return None
        grad = (1 / len(x)) * np.matmul(x_prime.T, y_hat - y)
        return grad

    def fit_(self, x, y, plot=False):
        """
        Description:
            Fits the model to the training dataset contained in x and y.
        Args:
            x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
            y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
            theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
            alpha: has to be a float, the learning rate
            max_iter: has to be an int, the number of iterations done during the gradient descent
        Returns:
            new_theta: numpy.ndarray, a vector of dimension 2 * 1.
            None if there is a matching dimension problem.
        Raises:
            This function should not raise any Exception.
        """
        self.thetas = self.thetas.astype(float)
        for _ in range(self.max_iter):
            gradient = self.gradient_(x, y)
            if gradient is None:
                return gradient
            self.gradient_history.append(np.log(np.linalg.norm(gradient)))
            self.thetas[0] -= gradient[0] * self.alpha
            self.thetas[1] -= gradient[1] * self.alpha
            self.thetas_history.append(self.thetas)

    def plot_pred(self, x, y):
        """
        Plot the data and prediction line from three non-empty np arrays.
        Args:
            x: has to be a np array, a vector of dimension m * 1.
            y: has to be a np array, a vector of dimension m * 1.
            theta: had to be a np array, a vector of dimension 2 * 1.
        Returns:
            Nothing
        Raises:
            This function should not raise any Exceptions.
        """
        y_hat = self.predict_(x).flatten()
        x = x.flatten()
        y = y.flatten()
        loss = self.loss_(y, y_hat)
        plt.scatter(x, y)
        plt.plot(x, self.thetas[1] * x + self.thetas[0], color="orangered")
        for i, datapoint in enumerate(x):
            plt.plot([datapoint, datapoint], [y[i], y_hat[i]], color="red", linestyle="--")
        plt.title(f"Cost: {loss}")
        plt.show()

    def plot_grad_desc(self):
        plt.plot(range(1, self.max_iter + 1), self.gradient_history)
        plt.xlabel('Iteration')
        plt.ylabel('Gradient magnitude')
        plt.title('Gradient descent convergence')
        plt.show()

    def plot_loss(self, x, y):
        loss_scores = []
        for value in self.thetas_history:
            self.thetas = value
            y_hat = self.predict_(x).flatten()
            x, y = x.flatten(), y.flatten()
            loss_scores.append(np.log(self.loss_(y, y_hat)))
        plt.plot(range(1, self.max_iter + 2), loss_scores)
        plt.xlabel('Iteration')
        plt.ylabel('Cost')
        plt.title('Cost evolution through gradient descent')
        plt.show()


    @staticmethod
    def add_intercept(x):
        """
        Adds a column of 1's to the non-empty numpy.array x.
        Args:
            x: has to be a numpy.array of dimension m * n
        Returns:
            X, a numpy.array of dimension m * (n + 1)
            None if x is not a numpy.array.
            None if x is an empty numpy.array.
        Raises:
            This function should not raise any Exception.
        """
        if not isinstance(x, np.ndarray) or x.size == 0:
            return None
        x = np.column_stack((np.zeros(np.shape(x)[0]) + 1, x))
        return x


def main():
    x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
    y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
    # lr1 = MyLinearRegression(np.array([[-1], [2]]))
    # y_hat = lr1.predict_(x)
    # print(y_hat)
    # print(lr1.loss_elem_(y, y_hat))
    # print(lr1.loss_(y, y_hat))
    # lr1.plot_(x, y)
    # lr1.fit_(x, y)
    lr2 = MyLinearRegression(np.array([[5], [1]]), max_iter=150)
    lr2.fit_(x, y)
    lr2.plot_pred(x, y)
    lr2.plot_grad_desc()
    lr2.plot_loss(x, y)
    print(lr2.thetas)
    y_hat = lr2.predict_(x)
    print(y_hat)
    print(lr2.loss_elem_(y, y_hat))
    print(lr2.loss_(y, y_hat))


if __name__ == "__main__":
    main()
