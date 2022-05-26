#Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
#NOTE: abs(num) returns the absolute value of a number

def absolute_value(num):
    return abs(100 - num) <= 10 or abs(200 - num) <= 10

absolute = absolute_value(201)

print(absolute)