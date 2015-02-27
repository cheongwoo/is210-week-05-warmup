#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function to check whether or not there are too many kittens"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Checking if there is enough litterboxes and some catfood

    Args:
        kittens (int): The number of kittens
        litterboxes (int): The number of available litterboxes
        catfood (bool): A boolean representing whether or not any catfood
                        exists

    Returns:
        bool: Whether or not we have at least one litterbox for each kitten
              and that we have some catfood
    Example:

        >>> print too_many_kittens(12, 12, False)
        True
    """
    return not (litterboxes >= kittens and catfood)
