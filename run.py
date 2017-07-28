# -*- coding: utf-8 -*-
"""run.py
run this pragram

Example:
    python run.py -p 1 -f ./
"""

from Find100thNumber import creat_arguement_parser
from Find100thNumber import FindNumber

if __name__ == "__main__":
    PAESER = creat_arguement_parser()
    APP = FindNumber(**vars(PAESER.parse_args()))

    APP.main_func()
