""" 7- Functions """

def sayHello():
    print("Hello")

def sayHi(name = "Nihil"):
    print("Hi", name)

sayHello()
sayHi()

def primeQ(number):
    if number == 0 or number == 1:
        print(number, "is not a Primer number.")
    else:
        divs = 0
        for f in range(2, number):
            if number % f == 0:
                divs += 1
            
        if divs == 0:
            print(number, "is a Primer number.")
        else:
            print(number, "is not a Primer number.")
            
primeQ(13)

# return() Expression

def hitMe():

    firstNumber = int(input("Give me a number: "))
    secondNumber = int(input("Give me the second number: "))

    return firstNumber + secondNumber

print("Result:", hitMe())

# Flexible parameters - we know it.



""" 8- Lambda Expressions """

#Short way to create a function


def Nihil1():
    print("Gimme tha Power")

Nihil2 = lambda: print("Gimme tha Power x2")

Nihil1()
Nihil2()

#Another Example

divideNumbers = lambda a, b: float(a/b) #If we won't write anything, it means return
print(divideNumbers(12, 2))


#Last Example

""" Finding are of circle (A = pi * r**2) """

findCircle = lambda r: 3.14 * (r ** 2)
print(findCircle(r = 2.5))