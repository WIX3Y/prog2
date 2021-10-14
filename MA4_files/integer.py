""" Python interface to the C++ Integer class """
import math
import random
import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes = [ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
#		lib.Integer_fib.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Integer_new(val)

	def get(self):
		return lib.Integer_get(self.obj)

	def set(self, val):
		lib.Integer_set(self.obj, val)

	def __del__(self):
		return lib.Integer_delete(self.obj)

#	def fib():
#		return lib.Integer_fib(self.obj)

	def fib_py(n):
		if n <= 1:
			return n
		else:
			return(fib_py(n-1) + fib_py(n-2))

def dots_in_circle(numb_dots):
	dots_in_circle = 0
	dots = []
	for i in range(0, numb_dots):
		dots.append([random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)])
	for dot in dots:
		if dot[0]**2 + dot[1]**2 <= 1:
			dots_in_circle += 1
	return dots_in_circle


def monte_carlo():
	pass

for n in [50, 100, 200, 400]:
	print(n, ": ", dots_in_circle(n))
#print("monte carlo: ", monte_carlo())
print("math.pi: ", math.pi)

f=Integer(12)
#print(f.fib())
print(f.fib_py(f.get()))
