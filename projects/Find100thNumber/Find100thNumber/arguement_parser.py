# -*- coding: utf-8 -*-
"""arguement_parser.py
get options from user by shell
"""
import argparse


def creat_arguement_parser():
    """return a argurment parser used in shell"""
    parser = argparse.ArgumentParser(
        prog="Find100thNumber",
        description="Generate numbers, find first 100MaxNumber and check the ans ",
        epilog="jskyzero 2016/12/12",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prefix_chars='-'
    )
    parser.add_argument("-p", metavar="part number", dest="part_num",
                        choices=['1', '2', '3'], default="3",
                        help="Number i meams do until part i (eg: 2 means do part 1, 2)")

    parser.add_argument("-f", metavar="file path", dest="file_path",
                        default="data",
                        help="set file path")
    return parser
