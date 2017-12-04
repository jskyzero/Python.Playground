#!/usr/bin/env python 
#-*- coding:utf-8 -*-

from content import sample
import unittest

def fun(x):
	return x + 1

class MyTest(unittest.TestCase):
	def test(self):
		self.assertEqual(fun(3), 4)

