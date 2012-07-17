from sys import path
path.append("/home/stanislavfeldman/projects/python/putils/")
path.append("/home/stanislavfeldman/projects/python/pev/")
from pev import Eventer

eventer = Eventer()
def on_message(msg):
	print msg
eventer.subscribe("m", on_message)
eventer.publish("m", "zzzz")
