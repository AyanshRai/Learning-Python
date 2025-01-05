# i 

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

# ii 

print(5*1)
print(5*2)
print(5*3)
print(5*4)
print(5*5)
print(5*6)
print(5*7)
print(5*8)
print(5*9)
print(5*10)

# iii

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello AI")
engine.runAndWait()

# iv and v 

import os

# Specify the directory path
directory_path = '/New folder'  # '.' refers to the current directory

# Get the list of files and directories in the specified path
contents = os.listdir(directory_path)

# Print each item in the directory
for item in contents:
    print(item)



