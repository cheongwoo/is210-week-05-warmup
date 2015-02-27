#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Default value setting function"""


def defaults(my_required, my_optional=True):
    """Set default value

    Args:
        my_required (bool): Boolean value
        my_optional (bool): Boolean with default value True
    Returns:
        bool: Boolean value on whether two arguments are same
    Example:

        >>> print defaults(True, False)
        False
    """
    return my_optional is my_required
