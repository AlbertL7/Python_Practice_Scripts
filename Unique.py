#Write a Python function that takes a list and returns a new list with unique elements of the first list.
# First Way
from collections import Counter 

def unique_list(lst):
    print(*Counter(lst))
    
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Second Way
"""
def unique_list(lst):
    U = []
    for num in lst:
        if num not in U:
            u.append(num)
    return U

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
"""

# Third Way
"""
def unique_list(lst):
    return list(set(lst))
    
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
"""