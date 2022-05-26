#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def times_3(string):
    text = ' '
    for i in string:
        text += i*3
    return text

result = times_3('Hello')

print(result)