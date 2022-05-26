#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    word = text.split()
    return word[0][0] == word[1][0]

result = animal_crackers('lama camel')

print(result)