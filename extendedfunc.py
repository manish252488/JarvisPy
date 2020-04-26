import subprocess
from speech import speak
import re
import os

list_drive = "wmic logicaldisk get name"


def cmd(command, name):
    proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    if str(err).lower() == "none":
        speak(name + " started")
        return True
    else:
        return False


def search_file(sample, file_type):
    drives = find_all_drives()
    location = []
    print(sample)
    drives.remove("C:")
    speak("pleas wait! searching files in your system")
    for drive in drives:
        drive = drive + "//"
        print("searching in:" + drive)
        dir_path = os.path.dirname(os.path.realpath(drive))
        for root, dirs, files in os.walk(dir_path):
            if str(file_type).lower() == 'dir':
                for direct in dirs:
                    if direct.startswith(sample):
                        location.append(str(root) + str(direct))
            else:
                for file in files:
                    if file.startswith(sample):
                        location.append(str(root) + str(file))

        return location


def find_all_drives():
    proc = subprocess.Popen(list_drive, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, stderr = proc.communicate()
    x = re.findall("[A-Z]:", str(stdout))
    print(x)
    return x


def terminate():
    print("exited")

