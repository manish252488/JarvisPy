from speech import speak, greet
import mysql.connector as mysql


def getConnection():
    db = mysql.connect(host="localhost", user="manish25", passwd="immanish1997@", database="jarvis")
    return db


def connect():
    try:
        db = getConnection()
        print("database connected")
        greet()
        return db
    except Exception:
        speak("cannot connect to my database.")
        speak("please wait!while i create one")
        db = mysql.connect(host="localhost", user="manish25", passwd="immanish1997@")
        cur = db.cursor()
        cur.execute("Create database jarvis")
        connect()


def deleteDb():
    speak("are sure to delete my database?i will unable to function")
    print("enter y/n")
    x = input()
    if x == "y" or x == "Y":
        db = getConnection()
        cur = db.cursor()
        cur.execute("drop database jarvis")
        speak("database deleted")
    else:
        speak("ok sir!")
