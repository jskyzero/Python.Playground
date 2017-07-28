# -*- coding: utf-8 -*-

print "\n\nand"
print "True and True = %r" % (True and True) 

print "\n\ndel"
a = [0, 1, 2, 3, 4, 5]
print "a = ", a
print "del a[0]"
del a[0]
print "a = ", a
print "\n\nfrom"
print "from ex25 import *"
from ex25 import *
print "%r" % break_words(".,., .,., .,., .,., .,.,")
print "\n\nnot"
print "not True = %r" % (not True)
print "\n\nwhile"
n = 1
while n >= 0:
    print n
    n-=1
print "\n\nas"
print "from ex25 import break_words as f"
from ex25 import break_words as f
print "%r" % f(".,., .,., .,., .,., .,.,")


assert(True == 1)

try:
    s = "hello"
    if s is None:
        raise NameError
except:
    print "Error"
finally:
    print "finally"


func = lambda x, y = 10 :  x + y
print func(100, 200)


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        print b
        a, b = b, a + b
        n = n + 1


f = fab(20)

for x in range(1,10):
    f.next()