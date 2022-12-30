"""
Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...
"""

#code by Tyler

def zero(a=None):
    if a == None:
        return 0
    else:
        return a(0)


def one(a=None):
    if a == None:
        return 1
    else:
        return a(1)


def two(a=None):
    if a == None:
        return 2
    else:
        return a(2)


def three(a=None):
    if a == None:
        return 3
    else:
        return a(3)


def four(a=None):
    if a == None:
        return 4
    else:
        return a(4)


def five(a=None):
    if a == None:
        return 5
    else:
        return a(5)


def six(a=None):
    if a == None:
        return 6
    else:
        return a(6)


def seven(a=None):
    if a == None:
        return 7
    else:
        return a(7)


def eight(a=None):
    if a == None:
        return 8
    else:
        return a(8)


def nine(a=None):
    if a == None:
        return 9
    else:
        return a(9)


def plus(a):
    def b(b):
        return a+b
    return b

def minus(a):
    def b(b):
        return b-a
    return b

def times(a):
    def b(b):
        return a*b
    return b


def divided_by(a):
    def b(b):
        return b/a
    return b


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
