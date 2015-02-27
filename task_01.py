#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Responses to a question by a motion and nudge certain number of times

    Args:
        wink (str): First motion response to question 'Know what I mean?'
        numwink (int): Number of times Arg motion and nudge to be repeated

    Returns:
        str: 'Know what I mean?' followed by Arg wink and 'nudge ' set number
             of times

    Example:

        >>> know_what_i_mean(wink='blink ', numwink=3)
            Know what I mean? blink blink blink, nudge nudge nudge
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
