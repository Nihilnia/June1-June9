""" 9- Modules """

# There is four ways to import modules

# 1- Importing all module

import math
#or
from math import *

# 2- Importing spesific 'things' from a module

from math import pow

# 3- Importing a module as a new name

import math as daftPunk

# 4- Importion spesific 'things' as a new named

from math import pow as pooo
from math import pi as p1111

print(p1111 * 2)
print(pooo(2, 3))

""" HOW TO CREATE YOUR OWN MODULE """

#First of all you should create your 'things', codes etc.
#Nothing different. Just create a Python file.

def nF():
    print("Intro III")

#After that you should move your py file to Python lib
# Here is my current directory D:\Python\Python37\Lib
#Now we can use our own module

from dinozorlar import nF as newName

newName()



""" 10- OBJECT ORIENTED PROGRAMMING """

class Nihil():

    name = "Nihil"
    age = 25

person = Nihil()
print(person.name)
print(person.age)

## __init__(self)

class Nihil2():

    def __init__(self, name, age):
        self.personaName = name
        self.personaAge = age
        print("Init always works first!", self.personaName, self.personaAge)

person02 = Nihil2("Nihilnia", 25)