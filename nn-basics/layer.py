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


class Layer:

    def __init__(self, nb_inputs, nb_outputs, activation):
        # TODO: initialize the weights and biases to random values between [-1, 1] and set the activation function
        self.weights = 0
        self.biases = 0
        self.activation = None

    def forward(self, x):
        """
        Compute the activation value for a given input
        Args:
            x (np.array): 1D-numpy array of the same size as the weights
        Returns:
            res (np.array): the activation values corresponding to the input
        """

        # TODO: compute WX + b where W represents the weights, X the input and b the biases
        lin_comb = 0
        # TODO: compute the activation of all perceptroons at once
        res = 0
        return res


class MLP:

    def __init__(self, input_size, layer_output_sizes, activation):
        # TODO: assign a list of consecutive layers to self.layers while the same activation respecting the input and consecutive output sizes
        self.layers = [Layer(None, None, activation=None)
                       for layer_idx in range(1)]

    def forward(self, x):
        """
        Compute the network output for a given input
        Args:
            x (np.array): 1D-numpy array of the same size as the first layer weights
        Returns:
            res (np.array): the network output
        """

        # Better to initialize a fixed-length output (easier to spot errors)
        res = x
        for layer_idx in range(len(self.layers)):
            # TODO: iteratively forward the input to each layer
            res = None

        return res
