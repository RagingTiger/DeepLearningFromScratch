# std libs
from typing import Callable

# 3rd party libs
import numpy
from numpy import ndarray


# functions
def square(x: ndarray) -> ndarray:
    """Apply x^2 function to each element in numpy array."""
    return numpy.power(x, 2)


def leaky_relu(x: ndarray) -> ndarray:
    """Apply Recitified Linear Unit (ReLU) to input array.
    Ref: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
    """
    return numpy.maximum(0.2 * x, x)


def deriv(func: Callable[[ndarray], ndarray],
          x: ndarray,
          delta: float = 0.001) -> ndarray:
    """Take in a function and approximate its derivative."""
    return (func(x + delta) - func(x - delta)) / (2 * delta)
    
