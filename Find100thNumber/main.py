# -*- coding: utf-8 -*-
"""main.py
main part of the pragram
"""

from Find100thNumber import FileProcess
from Find100thNumber import generate_number
from Find100thNumber import FindNthMaxNumber
from Find100thNumber import check_number
import timeit


class FindNumber(object):
    """Main obj of this Find100thNumber"""

    def __init__(self, part_num, file_path):
        self.process_file = FileProcess(file_path)
        self.part_num = int(part_num)
        self.file_path = file_path
        self.data_filename = "data"
        self.ans_filename = "ans"
        self.check_filename = "check"
        self.data_length = int(5E8)
        self.data_size = 2**32
        self.ans_size = 100

    def main_func(self):
        """use part_num to do the func"""
        if self.part_num == 1:
            print "Part 1 time :", timeit.timeit(stmt=self.part1, number=1)
        if self.part_num == 2:
            print "Part 1 time :", timeit.timeit(stmt=self.part1, number=1)
            print "Part 2 time :", timeit.timeit(stmt=self.part2, number=1)
        if self.part_num == 3:
            print "Part 1 time :", timeit.timeit(stmt=self.part1, number=1)
            print "Part 2 time :", timeit.timeit(stmt=self.part2, number=1)
            print "Part 3 time :", timeit.timeit(stmt=self.part3, number=1)

    def part1(self):
        """save 1E8 random value to file"""
        write_stream = self.process_file.open_write_stream(self.data_filename)
        for _ in xrange(0, self.data_length):
            write_stream.write(str(generate_number(self.data_size)) + '\n')
        write_stream.close()

    def part2(self):
        """find max 100 numbers and save to file"""
        read_stream = self.process_file.open_read_stream(self.data_filename)
        write_stream = self.process_file.open_write_stream(self.ans_filename)
        ans = FindNthMaxNumber(self.ans_size)
        for line in read_stream:
            ans.add_date(int(line))
        write_stream.write("\n".join([str(num)
                                      for num in ans.return_ans()]) + "\n")
        read_stream.close()
        write_stream.close()

    def part3(self):
        """use shell to check ans"""
        check_number(self.file_path, self.data_filename,
                     self.ans_filename, self.check_filename)
