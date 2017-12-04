#!/usr/bin/env python
#-*- coding:utf-8 -*-


def square(x):
	"""Square x.

	>>> square(2)
	4
	>>> square(-2)
	4
	"""

	return x * x

if __name__ == '__main__':
	import doctest
	doctest.testmod()

