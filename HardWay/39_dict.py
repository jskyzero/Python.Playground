# -*- coding: utf-8 -*-

things = ['a', 'b', 'v', 'd']
print things[1]
things[1] = 'z'
print things[1]
print things

stuff = {'name':'zed', 'age':36, 'height':6 * 12 + 2}
print stuff['name']
print stuff['age']
print stuff['height']
stuff['city'] = "San Francisco"
print stuff['city']
del stuff['city']

# create a mapping of state to abbreviation
states = {
    'orange': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    "a": 'a',
    1 : 1
}
x = 'a'
print states[1], states[x]

cities = {
    'CA':'Sanfrancisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Jacksonville'

print '-' * 10
print "MY State has: ", cities['NY']
print "Or State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']