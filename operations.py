""" Util Functions """
import math
import numpy as np
import random

def addition(first: int, second: int) -> int:
    """
    Returns sum of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first + second


def subtraction(first: int, second: int) -> int:
    """
    Returns subtraction of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first - second


def multiplication(first: int, second: int) -> int:
    """
    Returns multiplication of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first * second


def division(first: int, second: int) -> float:
    """
    Returns float division of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first / second


def integer_division(first: int, second: int) -> int:
    """
    Returns integer division of two integers.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return first // second


def power(base_int: int, power_int: int) -> int:
    """
    Returns base raised to the power.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return base_int ** power_int


def modulo(dividend: int, divisor: int) -> int:
    """
    Returns remainder of dividend // divisor.

    Parameters:
        first (int) : First Integer
        second (int) : Second Integer
    """
    return dividend % divisor


def log(first: int, base: int) -> float:
    """
    Returns sum of two integers.

    Parameters:
        first (int) : Value to calculate base for. Should be > 0.
        second (int) : Logarithmic base to use.
    """
    return math.log(first, base)

def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    s = 1 / (1 + np.exp(-z))
    ### END CODE HERE ###
    
    return s

def rand_between(start: int, stop: int) -> int:
    """
    Returns a random number between two integers.
    Parameters:
        start (int) : Lower limit of Random Number
        stop (int) : Upper Limit of Random Number
    """
    return random.randint(start, stop)