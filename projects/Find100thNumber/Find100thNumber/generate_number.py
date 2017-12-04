# -*- coding: utf-8 -*-
"""generate_number.py
generate the number
"""

import random


def generate_number(date_size):
    """return a int num from [0, date_size]"""
    return random.randint(0, date_size)
