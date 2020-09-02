from mainv2 import CRUD
import datetime
from scrap import webDrivers
import time

class Alarm:
	fromlst = {}
	mail=''
	password=''

	def __init__(self):
		crud = CRUD()
		cursor = crud.retdb()
		self.mail,self.password = crud.getuserCredentials()
		for row in cursor:
			self.fromlst[row[0]] = row[2]

	def runAlarm(self):
		while True:
			l = str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)
			if(l in self.fromlst):
				drivers = webDrivers()
				drivers.openLink(self.fromlst[l],self.mail,self.password)
			time.sleep(1)

	def Checkalarm(self):
		res = not bool(self.fromlst)
		if(res==True):
			return "No records found..."
		else:
			return ""


try:
	arg =sys.argv[1]
	inp = Alarm()

	if(arg == '-r'):
		inp.runAlarm()
except:
	print('')