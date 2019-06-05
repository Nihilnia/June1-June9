""" 13- File Operations """
try:
    userChoice = int(input("How many users you wanna create?: "))
except ValueError:
    print("you should give a number..")

usersList = open("usersList.txt", "a", encoding = "utf-8")

for f in range(userChoice):
    if f < 9:
        usersList.write("Username:" + "\tuser0" + str(f + 1) + "\t" + "password:" + "\tpass0" + str(f + 1) + "\n")
    else:
         usersList.write("Username:" + "\tuser" + str(f + 1) + "\t" + "password:" + "\tpass" + str(f + 1) + "\n")
print("Done!")

usersList.close()

userChoiceX2 = input("Wanna see usersList?\n")
if userChoiceX2.lower() == "yes":
    usersList = open("usersList.txt", "r", encoding = "utf-8")
    content = usersList.read()
    print(content)

userChoiceX3 = input("any spesific user?")
if userChoiceX3:
    foundUser = ""
    whichUser = input("Which user?: ")
    readUserList = open("usersList.txt", "r", encoding = "utf-8")
    for f in readUserList:
        if whichUser in f:
            foundUser = f
        
    if not foundUser:
        print("User not found")
    else:
        print(foundUser)



""" 14- Built-In Functions """

"map(), filter(), reduce(), zip()"


# map() Function

def x2E(number):
    return number * 2

results = list(map(x2E, range(10)))
print(results)

# filter() Function
"""same like map function, the only difference:
filter only works when the function returns True"""

def oddOnes(args):

    return args % 2 != 0

results = list(filter(oddOnes, range(10)))
print(results)
