#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Building blocks of Artificial neural network
'''

__author__ = 'François-Guillaume Fernandez'
__license__ = 'MIT License'
__version__ = '0.1'
__maintainer__ = 'François-Guillaume Fernandez'
__status__ = 'Development'


import numpy as np


class Activation:

    def __init__(self, function, derivative):
        # TODO: initialiaze the function and its derivative
        self.function = None
        self.derivative = None

    def forward(self, x):
        """
        Compute the function value for a given input
        Args:
            x (np.array): 1D-numpy array input
        Returns:
            a (np.array): the function values corresponding to the input
        """
        # TODO: apply the function to the input for forwarding
        return 0

    def prime(self, y):
        """
        Compute the function's derivative value for a given input
        Args:
            y (np.array): 1D-numpy array input
        Returns:
            a_prime (np.array): the function's derivative values corresponding to the input
        """
        # TODO: apply the function's derivative
        return None


class Perceptron:

    # We store input, output, the gradient of the activation function and the gradiant of the linear combination
    inputs = None
    output = None
    activation_grad = None
    grad_z = None

    def __init__(self, nb_inputs, activation, requires_grad=True):
        # TODO: set the weights, bias, activation, and requires_grad attributes of the Perceptron class using the constructor arguments
        self.weights = None
        self.bias = 0
        self.activation = None
        # This last argument is a boolean choice to speed up computation by storing gradient on forward pass to speed up the backward pass
        self.requires_grad = False

    def forward(self, x):
        """
        Compute the activation value for a given input according to the choice of weights, bias and activation
        Args:
            x (np.array): 1D-numpy array (size = weights.size)
        Returns:
            output (float): the activation value corresponding to the input
        """
        # TODO: store the input into your corresponding object attribute
        self.inputs = None
        # TODO: compute WX + b where W represents the weights, X the input and b the biases
        z = None
        # TODO: compute the activation of the linear combination
        self.output = 0
        # TODO: if the gradient was required, store activation'(WX + B)
        if self.requires_grad:
            self.activation_grad = None
        return self.output

    def backward(self, y):
        """
        Update the value of the loss gradient relatively to z (weighted sum with bias)
        Args:
            y (float): the loss gradient relatively to the perceptron activation value
        """
        if not self.requires_grad:
            raise ValueError("Gradient was not required on forward")
        else:
            # TODO: compute the loss gradient relatively to the weighted sum with the bias (=2 * error * activation'(WX + B))
            self.grad_z = None

    def update_params(self, alpha):
        """
        Update the weight and bias of the perceptron using the information computed during the backward pass
        Args:
            alpha (float): learning rate
        """
        if self.grad_z is None:
            raise ValueError("You need to backpropagate error before updating the weights")
        else:
            # TODO: update the weights (- alpha * 2 * error * activation'(WX +B) * X)
            self.weights -= None
            # TODO: update the bias (- alpha * 2 * error * activation'(WX +B))
            self.bias -= 0
