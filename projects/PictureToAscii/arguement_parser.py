# -*- coding: utf-8 -*-
"""run.py docstrings

This part get imformation like 'pic_path' and 'output_path' from shell and let the
PictureToAscii to use those imfomation to work

Example:
    python run.py
"""
import argparse


def create_arguement_parser():
    """return a arguement parser used in shell"""
    parser = argparse.ArgumentParser(
        prog="python run.py",
        description="A program named PictureToAscii that can make 'Picture To Ascii'",
        epilog="Written by jskyzero 2016/12/03",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prefix_chars='-')

    parser.add_argument("pictures_path", metavar="picture_path", nargs='+',
                        help="the picture(s) file path")

    parser.add_argument("-o", metavar='output dir', dest="output_dir",
                        help="the ascii file output dir", default="./")

    parser.add_argument("-e", metavar='extension name', dest="ext_name", nargs="?",
                        help="empty value means no extension name", default="txt")

    parser.add_argument("-s", metavar='size', dest="size", nargs=2, type=int,
                        help="width and height of all ascii file(s)")
    return parser
