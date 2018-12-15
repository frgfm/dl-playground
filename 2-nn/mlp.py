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


class Layer:

    # We store input, output, the gradient of the activation function and the gradiant of the linear combination
    inputs = None
    outputs = None
    activation_grad = None
    weight_grad = None
    grad_z = None

    def __init__(self, nb_inputs, nb_outputs, activation, requires_grad=True):
        # TODO: initialize the weights and biases to random values between [-1, 1], set the activation function, and the gradient storing option
        self.weights = None
        self.biases = None
        self.activation = None
        self.requires_grad = False

    def forward(self, x):
        """
        Compute the activation value for a given input according to the choice of weights, bias and activation
        Args:
            x (np.array): 1D-numpy array (size = weights.shape[1])
        Returns:
            output (np.array): the activation value corresponding to the input (size = weights.shape[0])
        """
        # TODO: store the input into your corresponding object attribute
        self.inputs = None
        # TODO: compute WX + b where W represents the weights, X the input and b the biases
        z = None
        # TODO: compute the activation of all perceptroons at once and assign it to the outputs attribute
        self.outputs = None
        # Gradient storing
        if self.requires_grad:
            # TODO: store activation'(WX + B)
            self.activation_grad = None
            # TODO: store the gradient of Z relatively to the weights
            # Hint: remember from the notebook that it is a 3D tensor. There are as many channels as self.inputs.size, and this need to be on axis=2
            # Hint: for each channel k, it looks like a diagonal matrix of size self.outputs.size with only self.outputs[k] on the diagonal
            # Hint: the functions numpy.eye and numpy.stack might be helpful to you
            self.weight_grad = None

        return self.outputs

    def backward(self, next_layer_grad):
        """
        Compute the loss gradient relatively to the previous layer's activation values
        Args:
            next_layer_grad (np.array): the loss gradient relatively to the layer activation values (size = weights.shape[0])
        Returns:
            grad (np.array): the loss gradient relatively to the previous layer activation values (size = weights.shape[1])
        """
        if not self.requires_grad:
            raise ValueError("Gradient was not required on forward")
        else:
            # TODO: multiply the incoming gradient by activation'(WX + B) to get the loss gradient relatively to z
            self.grad_z = None
            # TODO: multiply self.grad_z by the weights to get the loss gradient relatively to the activation of the previous layer
            # Hint: pay attention to the actual numpy operate you will use, it's a vector by matrix multiplication
            grad = None

        return grad

    def update_params(self, alpha):
        """
        Update the weight and bias of the layer using the information computed during the backward pass
        Args:
            alpha (float): learning rate
        """
        if self.grad_z is None or self.weight_grad is None:
            raise ValueError("You need to backpropagate error before updating the weights")
        else:
            # TODO: update the weights by substracting alpha * product(grad_z, weight_grad)
            # Hint: this is the moment where numpy.tensordot might become handy (check the axes argument in the function documentation)
            self.weights -= None
            # TODO: update the biases by substracting the product alpha and the gradient relatively to z
            self.biases -= None


class MLP:

    def __init__(self, input_size, layer_output_sizes, activation, requires_grad=True):
        # TODO: assign a list of Layer objects to the layers attribute and the gradient storing boolean
        # Hint: check your updated Layer constructor to successfully create layers with matching dimensions
        self.layers = None
        self.requires_grad = False

    def forward(self, x):
        """
        Compute the activation value for a given input according to the choice of layers' parameters
        Args:
            x (np.array): 1D-numpy array (size = self.layers[0].weights.shape[1])
        Returns:
            outputs (np.array): the activation value corresponding to the input (size = self.layers[-1].weights.shape[0])
        """

        # Better to initialize a fixed-length output (easier to spot errors)
        outputs = x
        for layer_idx in range(len(self.layers)):
            # TODO: update outputs by assigning it the result of its forwarding through each layer
            outputs = None

        return outputs

    def backward(self, expected_outputs):
        """
        Backpropagate the loss gradient through each layer
        Args:
            expected_outputs (np.array): the expected values for the network output
        """
        if not self.requires_grad:
            raise ValueError("Gradient was not required on forward")
        else:
            # TODO: initialize the running gradient with the gradient of the loss function relatively to the activation of the last layer
            # Hint: check the formula in the notebook
            running_grad = None
            for layer_idx in range(len(self.layers)):
                # TODO: assign the activation value of perceptron for input x at unit_idx to res[unit_idx]
                running_grad = None

    def update_params(self, alpha):
        """
        Update the weight and bias of the layers using the information computed during the backward pass
        Args:
            alpha (float): learning rate
        """
        if not self.requires_grad:
            raise ValueError("You need to backpropagate error before updating the weights")
        else:
            # Update weights & bias
            # TODO: update the parameters of each layer with learning rate alpha
