""" 11- Inheritance at OOP """

class Dropbox():

    def __init__(self, userName = "Nihil", userLang = "Python"):
        self.userName = userName
        self.userLang = userLang

    def __str__(self):
        return """All Informations:
        userName: {}
        userLang: {}
        """.format(self.userName, self.userLang)


user01 = Dropbox(userName = "Nihilnia")
print(user01)


class Example(Dropbox):
    pass

user02 = Example(userName = "Tron")
print(user02)



""" Override & super() Function """

class mySongs():

    def __init__(self, songName, artist):
        self.songName = songName
        self.artist = artist
    
    def showInfos(self):
        print("""

            -- mySongs --

        songName:   {}

        artist:     {}

        """.format(self.songName, self.artist))

example01 = mySongs(songName = "song01", artist = "artist01")
example01.showInfos()


class herSongs(mySongs):

    def __init__(self, songName, artist, rate):
        super().__init__(songName, artist)
        self.rate = rate


example02 = herSongs(songName = "song_02", artist = "artist_02", rate = "3")
example02.showInfos()



""" 12- Error Handling """

#### Example One

try:
    print("Process 1")
    userNumber1 = int(input("Give me a number: "))
    userNumber2 = int(input("Give me another number: "))
    print("Number 1 + Number 2 =", userNumber1 + userNumber2)
except ValueError:
    print("You should give number, not word.")


#Example Two

try:
    print("Process 2")
    userNumber1 = int(input("Give me a number: "))
    userNumber2 = int(input("Give me another number: "))
    print("Number 1 / Number 2 =", userNumber1 / userNumber2)

except ValueError:
    print("You should give number, not word.")
except ZeroDivisionError:
    print("A number can't divide to zero!")


#Example Three

try:
    print("Process 3")
    userNumber1 = int(input("Give me a number: "))
    userNumber2 = int(input("Give me another number: "))
    print("Number 1 / Number 2 =", userNumber1 / userNumber2)

except ValueError:
    print("You should give number, not word.")
except ZeroDivisionError:
    print("A number can't divide to zero!")

finally:
    print("This 'finally' block always works.")


#Raise!!

def reverseIt(name):
    if isinstance(name, str):
        print(name[::-1])
    else:
        raise TypeError("You should give me a word, not a number!")