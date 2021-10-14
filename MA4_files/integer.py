""" Python interface to the C++ Integer class """
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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
	dots_x = []
	dots_y = []
	for i in range(0, numb_dots):
		dots_x.append(random.uniform(-1.0, 1.0))
		dots_y.append(random.uniform(-1.0, 1.0))
	for dot_x, dot_y in zip(dots_x, dots_y):
		if dot_x**2 + dot_y**2 <= 1:
			dots_in_circle += 1
	return dots_in_circle

def plot_dots():
	for dot_x, dot_y in zip(dots_x, dots_y):
		if dot_x**2 + dot_y**2 <= 1:
			plt.plot(dot_x, dot_y, color="red")
		else:
			plt.plot(dot_x, dot_y, color="blue")
	plt.savefig("dots.png")

for n in [50, 100, 200, 400]:
	print("n=", n)
	print("n_c=", dots_in_circle(n))
	print("4*n_c/n=", 4*dots_in_circle(n)/n, "\n")
plot_dots()
print("math.pi: ", math.pi)

#f=Integer(12)
#print(f.fib())
#print(f.fib_py())
