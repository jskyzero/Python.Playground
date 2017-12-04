# -*- coding: utf-8 -*-
"""check_number.py
check ans is right or not
"""

import os
import re


def check_number(file_path, date_filename, ans_filename, check_filename):
    """check ans is right or not"""
    shell_find_num = "less {date_path}  | sort -n | tail -n 100  > {check_path}"
    shell_check_num = "diff {ans_path} {check_path}"
    date_path = file_path + '/' + date_filename
    ans_path = file_path + '/' + ans_filename
    check_path = file_path + '/' + check_filename
    shell_find_num = re.sub("{date_path}", date_path, shell_find_num)
    shell_find_num = re.sub("{check_path}", check_path, shell_find_num)
    shell_check_num = re.sub("{ans_path}", ans_path, shell_check_num)
    shell_check_num = re.sub("{check_path}", check_path, shell_check_num)
    os.system(shell_find_num)
    os.system(shell_check_num)
