# Python27
`jskyzero` `2018/01/01`

![python logo](https://www.python.org/static/community_logos/python-logo-generic.svg)


## Overview
+ Python is a widely used high-level programming language for general-purpose programming,
+ Python lets you work quickly and integrate systems more effectively.

## Projects
```
.
├── hardwork
│   ├── hardway           // hardway to learn
│   └── leetcode          // leetcode solutions
├── projects
│   ├── example           // Python Project Example
│   ├── FigureLetters     // Use KMeans to figure letters in picture
│   ├── Find100thNumber   // Produce numbers, find Nth largest numbers
│   ├── NoteBook          // A basic note book use socket (client/server)
│   ├── PictureToAscii    // Convert your picture to ascii characters
│   └── YandeSpider       // A spider downloading picture from yande.re
└── README.md
```

## PEP 8 -- Style
+ Code lay-out
  + Use 4 spaces per indentation level.
  + Limit all lines to a maximum of 79 characters.
  + Code in the core Python distribution should always use UTF-8 (or ASCII in Python 2).
+ Naming Styles
  + Package and Module Names should have short, all-lowercase names. `lower_case_with_underscores`.
  + Class names should normally use the CapWords convention.
  + Names of type variables should normally use CapWords preferring short names: T, AnyStr, Num.
  + Function names should be `lower_case_with_underscores`
  + Function and method arguments
    + Always use self for the first argument to instance methods
    + Always use cls for the first argument to class methods.
    + `class_` is better than `class`. (Perhaps better is to avoid such clashes by using a synonym.)
  + Method Names and Instance Variables
    + Use the function naming rules: `lower_case_with_underscores`
    + Use one leading underscore only for non-public methods and instance variables.
  + Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include `MAX_OVERFLOW` and `TOTAL`.

`lower_case_with_underscores` : lowercase with words separated by underscores as necessary to improve readability.

## Reference
+ [python](https://www.python.org)
+ [learnpythonthehardway](https://learnpythonthehardway.org)
+ [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
