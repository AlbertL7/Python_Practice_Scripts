#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    return name[:3].capitalize() + name[3:].capitalize()

print(old_macdonald('macdonald'))