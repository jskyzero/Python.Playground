# -*- coding: utf-8 -*-
"""find_number.py
find number from date
"""

from sortedcontainers import SortedList


class FindNthMaxNumber(object):
    """store Nth max number"""

    def __init__(self, size):
        self.size = size
        self.ans = SortedList()

    def add_date(self, num):
        """add new num to ans"""
        if len(self.ans) < self.size:
            self.ans.add(num)
        else:
            self.ans.add(num)
            del(self.ans[0])

    def return_ans(self):
        """return list(ans)"""
        return list(self.ans)
