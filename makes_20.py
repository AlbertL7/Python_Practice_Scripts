#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

from operator import truediv
import re


def makes_twenty(n1,n2):
    if n1+n2 == 20:
        return True
    elif n1 == 20 or n2 == 20:
        return True
    else: 
        return False
    
result = makes_twenty(10,10)

print(result)
    