from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from commandprocessing import execute_command
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import pandas as pd
from regfun import remove_pun
from trainmodule import train_command
from speech import speak
stopwords = set(stopwords.words("english"))
pos = PorterStemmer()
lem = WordNetLemmatizer()


def parse(text):
    # filter text
    flag = False
    text = text_filter(text)
    print(text)
    # search for triggers
    trigger = search_triggers(text)
    # if triggers are found search for commands and other stuffs.
    text = trigger[1]
    val = command_classifier(text)
    if val[0]:
        trig = val[1]
        name = val[2]
        print(trig)
        print(name)
        execute_command(trig, name)
        flag = True
    else:
        flag = False
    if not val[0]:
        if greet_classifier(text):
            flag = True
    return flag


def search_triggers(sample):
    trigger_flag = False
    triggers = open("localdb/speech_trigger.txt", "rt").read()
    for w in sample:
        if str(w).lower() in word_tokenize(triggers):
            print("trigger found")
            sample.remove(w)
            trigger_flag = True
            break
    if trigger_flag:
        speak("yes sir")
    return trigger_flag, sample


def text_filter(sample):
    sample = remove_pun(sample)
    filtered_sent = []
    for w in sample:
        if w not in stopwords:
            filtered_sent.append(lem.lemmatize(w))
    return filtered_sent


def command_classifier(sample):
    is_cmd = False
    df = pd.read_csv("localdb/commands.csv")
    commands = list(df['command'])
    init_cmd = ""
    for w in sample:
        if str(w).lower() in commands:
            print("command found in normal words")
            is_cmd = True
            sample.remove(w)
            init_cmd = w
            break
        elif pos.stem(str(w).lower()) in commands:
            print("command found in stem")
            is_cmd = True
            sample.remove(w)
            init_cmd = w
            break
        else:
            print("inside syno")
            synonyms = []
            try:
                for syn in wordnet.synsets(w):
                    for l in syn.lemmas():
                        synonyms.append(l.name())
                for s in synonyms:
                    if pos.stem(str(s).lower()) in commands or str(s).lower() in commands:
                        is_cmd = True
                        sample.remove(w)
                        init_cmd = s
                        print("found in syn lemma set: " + s + " : " + w)
                        break
            except Exception:
                print("word not found in syn lemmas" + w)
    if init_cmd == "":
        print("add command")
        if str(input()).lower() == 'y':
            train_command(sample,"")
        return False, ""
    else:
        new_df = df.loc[df['command'] == init_cmd]
        trig = list(n for n in new_df['value'])
        return is_cmd, trig[0], sample[0]


def greet_classifier(sample):
    print("greet")
    return True

