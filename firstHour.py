""" 1- Strings, Type Converts """

a = 1
print(type(a)) #<class 'int'>

a = str(a)
print(type(a)) #<class 'str'>

nick = "Nihilnia"

print("Nick:", nick[:5]) #Nick: Nihil

#Reverse String
print(nick[::-1]) #ainlihiN



""" 2- Lists (append, pop, sort) """ 

a = ["This", "is", "a", "List"]
print(a) #['This', 'is', 'a', 'List']

print(a[2:]) #['a', 'List']

a.append("Nihil")

print(a) #['This', 'is', 'a', 'List', 'Nihil']

b = list("hey")
print(b) #['h', 'e', 'y']

b.pop() #Last item deleted from list.
print(b) #['h', 'e']

c = [1, "a", 2, "b"]
print(c) #[1, 'a', 2, 'b']



""" 3- Tuples (count, index) """

b = ("This", "is", "a", "tuple")
print(b) #('This', 'is', 'a', 'tuple')

#Note: You can't make any change on Tuples.

print(b.count("This")) #1
print(b.count("Nihil")) #0

print(b.index("This")) #0
# print(b.index("Nihil")) #ValueError



""" 4- Dictionaries (keys, values, items) """

whoAmI = {"keyOne": "valueOne", "keyTwo": 2, 3: "ValueThree"}
print(whoAmI["keyOne"])


print("Keys:", whoAmI.keys())
print("Values:", whoAmI.values())
print("Items:", whoAmI.items())

#You can use index() on Dicts either.