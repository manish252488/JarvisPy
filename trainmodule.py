from speech import speak
from listen import Ears
from extendedfunc import search_file, cmd
from connectdb import getConnection
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()


def command_train(trig, name):
    ob = Trainer(trig, name)
    return ob.train()


class Trainer:

    def __init__(self, trigger, name):
        self.d_type = str(get_type()).lower()
        self.exe = "cmd"
        self.name = stemmer.stem(get_name(self.d_type))
        self.command = search_file(self.name, self.d_type)
        self.trigger = trigger

    def train(self):
        print("train module")
        if len(self.command) > 1:
            speak("wallah! too many files")
            print(self.command)
            Initialize(self.command, self)
        else:
            command = "start" + " " + self.command[0]
            return update_new_command(self.trigger, self.d_type, self.exe, self.name, command)

    def selected_file(self, sample):
        command = "start" + " " + sample
        return update_new_command(self.trigger, self.d_type, self.exe, self.name, command)


def update_new_command(t, d, e, n, c):
    db = getConnection()
    cur = db.cursor()
    q = "insert into commands(trigg,type,executor,name_val,command) values('" + str(t) + "','" + str(
        d) + "','" + str(e) + "','" + str(n) + "','" + str(c) + "')"
    cur.execute(q)
    db.commit()
    return dispatcher["cmd"](c, str(n) + " " + str(d))


def get_type():
    x = True
    while x:
        speak("what is it?example an application or a file or a directory")
        type_class = Ears().run()
        if type_class != "":
            speak("sure is it a " + type_class)
            print(type_class)
            print("enter y to confirm")
            if str(input()).lower() == "y":

                type_class = find_commons(type_class)
                print(type_class)
                if type_class[0]:
                    x = False
                    type_class = type_class
                else:
                    x = True
                    speak("information not in database")
            else:
                continue
        else:
            continue
    return type_class


def get_name(d_type):
    x = True
    while x:
        speak("tell me the name of the " + d_type + " again!")
        name = Ears().run()
        if name != "":
            speak("sure is it a " + name)
            print("enter y to confirm")
            if str(input()).lower() == "y":
                x = False
            else:
                continue
        else:
            continue
    return name


def find_commons(d_type):
    db = getConnection()
    cur = db.cursor()
    q = "select common from classifications where type='" + d_type + "'"
    cur.execute(q)
    commons = cur.fetchall()
    if commons:
        return commons[0][0]
    else:
        print(commons)


def train_command(sample):
    print(sample)


dispatcher = {"cmd": cmd}
