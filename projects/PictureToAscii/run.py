# -*- coding: utf-8 -*-
"""run.py docstrings

This part get imformation like 'pic_path' and 'output_path' from shell and let the
PictureToAscii to use those imfomation to work

Example:
    python run.py tests/sample.jpg
"""


from PictureToAscii import PictureToAscii
from PictureToAscii import create_arguement_parser


if __name__ == "__main__":
    PARSER = create_arguement_parser()
    APP = PictureToAscii()

    APP.main_func(**vars(PARSER.parse_args()))
