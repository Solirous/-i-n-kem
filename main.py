from datetime import datetime
import wmi
import sys
import os
now = datetime.now().time()

banned_browser={
	"chrome.exe":1,
	"msedge.exe":1,
}
f=wmi.WMI()

def checkopen():
	for process in f.Win32_Process():
		for x in banned_browser.keys():
			if x == process.Name:
				return "rac",process
def getpath():
	with open("path.txt") as f:
		return f.readline()
def findpw():
	path = getpath()
	print(str(path))
	dir_list =os.listdir(path)
	for x in dir_list:
		if x == "nminhtue123.tuedepzai":
			return True 
		elif (x=="exit.codetuedepzai"):
			print("SYTEM REMOVED")
			sys.exit("uhhh xoa chuong trinh I guess")
	return False
if __name__ == "__main__":
	hour = now.hour
	if (hour > 12):
		while(True):
				try:
					tdz,pr = checkopen()
					if(tdz=="rac" and pr):
						if (findpw()==False):
							pr.Terminate()
						else:
							print("I FOUND PASSW")

				except Exception as e:
					print(e)
					print("Cant get file path!!")

