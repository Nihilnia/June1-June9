# import sqlite3, os

# connectToDB = sqlite3.connect("example.DB")

# cursor = connectToDB.cursor()


# cursor.execute("Create table if not exists fight (Name TEXT, Number INT)")
# cursor.commit()

# cursor.execute("Insert into fight ")


import os 

a = 0

for x, y, z in os.walk(r"C:\Users\Nihil\Desktop\sysNihil"):
    for f in z:
        print("""
        X(YOL): {}
            
        Z(Dosya): {}

        """.format(x, f))
        