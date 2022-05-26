# reversing a string

def master_yoda(text):
    return ' '.join(text.split()[::-1])

reverse_string = master_yoda('I am home')

print(reverse_string)