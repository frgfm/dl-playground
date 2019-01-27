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
from naive_perceptron import NaivePerceptron


class NaiveLayer:

    def __init__(self, weights, biases, activation):
        # TODO: assign a list of NaivePerceptrons to self.units using the weights, biases and activation arguments
        # Hint: you should have as many perceptrons as biases, and each row of the weight matrix correspond to a given perceptron's weights
        self.units = [NaivePerceptron(None, None, None)
                      for i in range(1)]

    def forward(self, x):
        """
        Compute the activation value for a given input
        Args:
            x (np.array): 1D-numpy array of the same size as the weights
        Returns:
            res (np.array): the activation values corresponding to the input
        """

        # Better to initialize a fixed-length output (easier to spot errors)
        res = np.zeros(len(self.units))
        for unit_idx in range(len(self.units)):
            # TODO: assign the activation value of perceptron for input x at unit_idx to res[unit_idx]
            res[unit_idx] = 0

        return res
