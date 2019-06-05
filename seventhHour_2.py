import sqlite3
from random import randint

#Creating a db

connectToDb = sqlite3.connect("example.DB")
cursor = connectToDb.cursor()


#Creating table

cursor.execute("Create table if not exists ExampleTable(name TEXT, surname TEXT, id INT)")
connectToDb.commit() #after any change in db, you should commit it.


#Inserting informations to table

userName = input("What is your name: ")
userSurName = input("What is your surname: ")
userID = randint(1, 9999)
cursor.execute("Insert into ExampleTable values(?, ?, ?)", (userName, userSurName, userID))
connectToDb.commit()


#Getting informations from table

userSearch = input("Give me your name so I can search you on db: ")
cursor.execute("Select * from ExampleTable where name = (?)", (userSearch, ))
result = cursor.fetchall()
print("""
ALL INFORMATIONS ABOUT YOU:
Name:       {}
Surname:    {}
Id:         {}
""".format(result[0][0], result[0][1], result[0][2]))
#ofc this way is so simple, there can be two same name.. but this is just the example.


#Update informations
userSearch = input("Give me your name so I can search you on db: ")
cursor.execute("Select * from ExampleTable where name = (?)", (userSearch, ))
result = cursor.fetchall()
print("RRR:", result)
# print("""
# ALL INFORMATIONS ABOUT YOU:
# Name:       {}
# Surname:    {}
# Id:         {}
# """.format(result[0][0], result[0][1], result[0][2]))
userChoice = input("What do you wanna change: ")

if userChoice.lower() == "name":
    newName = input("New name: ")
    cursor.execute("Update ExampleTable set name = (?) where name = (?)", (newName, userSearch))
    connectToDb.commit()
    print("Name changed.")
elif userChoice.lower() == "surname":
    newSurname = input("New surname: ")
    cursor.execute("Update ExampleTable set surname = (?) where name = (?)", (newSurname, userSearch))
    connectToDb.commit()
    print("Surname changed.")
else:
    newID = input("New ID: ")
    cursor.execute("Update ExampleTable set ID = (?) where name = (?)", (newID, userSearch))
    connectToDb.commit()
    print("ID changed.")


#Delete?
deleteWhat = input("Which name you wanna delete: ")
cursor.execute("Delete from ExampleTable where name = (?)", (deleteWhat, ))
connectToDb.commit()
print(deleteWhat, "deleted from DB!")

connectToDb.close()