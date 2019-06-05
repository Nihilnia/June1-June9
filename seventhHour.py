" Continue to Built-In Functions"

#reduce() Function

from functools import reduce

def factorial(x, y):

    return x * y

resultF = reduce(factorial, range(2, 6))
print("resultF:", resultF)


#zip() Function

listOne = ["nihil", "nia", "Python", "Big Data", "AI"]
listTwo = list(range(len(listOne)))

for items, numbers in zip(listOne, listTwo):
    print(numbers, items)


# all() & any()


listThree = [1, 0]
print(any(listThree)) #True
print(all(listThree)) #False

theList = [True, True, False]
print(all(theList)) #False
print(any(theList)) #True
