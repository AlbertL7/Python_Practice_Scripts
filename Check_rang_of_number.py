#Write a function that checks whether a number is in a given range (inclusive of high and low)

def range_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in the range {low} to {high}')
    else:
        print(f'{num} is not in the range {low} to {high}')

print(range_check(10,10,20))