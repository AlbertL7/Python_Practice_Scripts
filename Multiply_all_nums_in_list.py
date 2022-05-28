#Write a Python function to multiply all the numbers in a list.

#Sample List : [1, 2, 3, -4]
#Expected Output : -24

def multiply(numbers):
    result = 1
    for i in numbers:
        result = i * result
    return result

print(multiply([1, 2, 3, -4]))