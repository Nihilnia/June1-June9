""" 5- Loops (For, While) """

a = list("Nihil")
index = 0
for f in a:
    print("Index no:", index, "item:", f)
    index += 1

countIt = 0
for f in a:
    if "i" in f:
        countIt += 1
print("'i' in the list {} times".format(countIt))

#range()

for f in range(0, 31, 2):
    print(f)

#prime numbers Example

primes = list()

for f in range(2, 100):
    divs = 0
    for x in range(2, f):
        if f % x == 0:
            divs += 1
    if divs == 0:
        primes.append(f)

print(primes)



""" 6- List Comprehensions """

numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenNumbers = [f for f in numbersList if f % 2 == 0]
print("Evens:", evenNumbers)

oddNumbers = [x for x in numbersList if x % 2 == 1]
print("Odds:", oddNumbers)

# 1 - 100 Evens

to100 = [f for f in range(101) if f % 2 == 0]
print("to 100:", to100)

#another Example

tupleList = [("a", 1), ("b", 2), ("c", 3)]

executeThem = [x for f in tupleList for x in f]
print("Ex:", executeThem)

#Last Example:

channelList = {"Channel 1": "TV 1", "Channel 2": "TV 2", "Channel 3": "TV 3"}
channelNumbers = [numbers for numbers in channelList.keys()]
channelNames = [names for names in channelList.values()]

print("Channel Names:")
print(channelNames)

print("Channel Numbers:")
print(channelNumbers)

primeees = []
for f in range(2, 100):
        divs = 0
        for x in range(2, f):
                if f % x == 0:
                        divs += 1

        if divs == 0:
                primeees.append(f)

print("Primes:", primeees)

# /w List Comprehension

daftPunk = [f for f in range(2, 100) if all (f % y != 0 for y in range(2, f))]
print("Daft Punk:", daftPunk)

""" 
Daft Punk: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,59, 61, 67, 71, 73, 79, 83, 89, 97]
"""