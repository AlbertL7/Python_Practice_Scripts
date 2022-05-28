#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
#Hint: You may want to use .replace() method to get rid of spaces.

import string
def check_pangram(pos_pangram,alphabet = string.ascii_lowercase):
    the_bet = set(alphabet)
    str1 = set(pos_pangram.replace(' ','').lower())
    
    return str1 == the_bet

print (check_pangram('The quick brown fox jumps over the lazy dog'))