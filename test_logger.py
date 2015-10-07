from pylogger.logger import *

class a:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@logging_for_func(level='DEBUG')
def add(a, b):
	info("fawefw")  # info log
	z = a.x + b.y

def function1():
	error("nuivvea")  # error log


import time
@logging_for_func(level='DEBUG')
def longtime_function(duration):
	time.sleep(duration)
	
		

m = a(1, 2)
n = a(3, 4)
add(m ,n)
function1()
longtime_function(10)

