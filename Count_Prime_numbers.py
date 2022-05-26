#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

def count_primes(num):
    count = 0
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            count += 1
    return count

result = count_primes(100)

print(result)
