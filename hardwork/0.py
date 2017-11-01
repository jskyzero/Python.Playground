# -*- coding: utf-8 -*-

print '-' * 10
print "List"

a = ['0', '1', '2', '3', '4', '5']
print "a = %r" % a
print "len(a) = %r" % len(a)
print "a[0] = %r, %s" % (a[0], a[0])
print "a[-len(a)] = %r, %s" % (a[-len(a)], a[-len(a)])
print "a[0:3] = %r" % a[0:3]
print "a[::2] = %r" % a[::2]
a.append('7')
print "a = %r" % a
a.insert(len(a)-1, '6')
print "a = %r" % a 
a.insert(6, 'x')
print "a = %r" % a 
del(a[6])
print "a = %r" % a
a.pop()
print "a = %r" % a 
a.pop(6)
print "a = %r" % a


print "\n" * 3
print '-' * 10
print "tuple"
b = (1, 2, [1,2])
print "b =", b
b[2][0] = 2
print "b = ", b

try: 
    tuple.append(3)
except:
    print "Error"