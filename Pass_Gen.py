import secrets
import string
import sys

print('####Password Generator####\n')

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# Account name
account = input('Name of Account / website = ')

# Username
username = input('Username / Email = ')

# Extra info

extra = input('Amplifying Information / Pin = ')

# fix password length
pwd_length = int(input('\nEnter the number length of the password\n'))

# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print('\nYour PASSWORD =',pwd, 'your USERNAME =', username, 'your AMPLIFYING INFO =', extra, 'for', account)

original_stdout = sys.stdout

with open('passwords.txt', 'a') as f:
  sys.stdout = f 
  str(print('\n', account, '|', username, '|', pwd, '|', extra,'\n'))
  sys.stdout = original_stdout
