from datetime import datetime
import wmi
import sys
import os
import codecs
now = datetime.now().time()

banned_browser = {
    "chrome.exe": 1,
    "msedge.exe": 1,
}
f = wmi.WMI()


def checkopen():
    for process in f.Win32_Process():
        for x in banned_browser.keys():
            if x == process.Name:
                return "rac", process
def getpath():
    with open("path.txt") as f:
        return f.readline()
def pw():
    with open("pw.txt") as f:
        return f.readline()

def exit():
    with open("pw.txt") as f:
        return f.readline()


def findpw():
    path = getpath()
    print(str(path))
    dir_list = os.listdir(path)
    for x in dir_list:
        if x == codecs.decode(pw(),'rot13'):
            return True
        elif x == codecs.decode(exit(),'rot13'):
            print("SYTEM")
            sys.exit("uhhh xoa chuong trinh I guess")
    return False


hour = now.hour
if hour > 12:
    while True:
        try:
            tdz, pr = checkopen()
            if tdz == "rac" and pr:
                if findpw() == False:
                    pr.Terminate()
                else:
                    print("I FOUND PASSW")

        except Exception as e:
            print(e)
            print("Cant get file path!!")
