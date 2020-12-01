print('''
|======================|
        Settings
|======================|
''')

print('''

NOTE:

The following setting will apply on the CMD related things only like appearance , colour etc...

Nothing will effect the AI. 

For more info visit - http://cmpsplanes.ezyro.com
''')

print("-------------------------------------------------------------------------------------------")

print('''
||||||||||||||||||||||||||||||||||||||||
               Commands
To change colour - colour.c
||||||||||||||||||||||||||||||||||||||||

''')

while True:
    a = input("AI/Arduino/setting>>> ")

    if "colour.c" in a:
        from subprocess import *
        Popen('colour.bat')

    else:
        print("Not available...")