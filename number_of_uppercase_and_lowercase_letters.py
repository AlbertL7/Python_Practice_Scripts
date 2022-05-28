#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
#HINT: Two string methods that might prove useful: .isupper() and .islower()

def up_low(lett):
    uppercase = 0
    lowercase = 0
    for i in lett:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        else:
            pass
    
    print(f'Original string: {lett}')
    print(f'No. of Upper case characters: {uppercase}')
    print(f'No. of Lower case Characters: {lowercase}')
    
print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))