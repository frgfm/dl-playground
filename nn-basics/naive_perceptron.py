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


class NaivePerceptron:

    def __init__(self, weights, bias, activation):
        # TODO: set the weights, bias and activation attributes of the NaivePerceptron class using the constructor arguments
        self.weights = 0
        self.bias = 0
        self.activation = None

    def forward(self, x):
        """
        Compute the activation value for a given input
        Args:
            x (np.array): 1D-numpy array of the same size as the weights
        Returns:
            res (float): the activation value corresponding to the input
        """
        # TODO: compute WX + b where W represents the Weights, X the input and b the bias
        lin_comb = 0
        # TODO: compute the activation of this value
        res = 0

        return res
