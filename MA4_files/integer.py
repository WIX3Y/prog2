""" Python interface to the C++ Integer class """
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import math
import random
import numpy as np
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
#f=Integer(12)
#print(f.fib())
#print(f.fib_py())

# 1.1 ...
def dots(numb_dots):
	dots_x = []
	dots_y = []
	for i in range(0, numb_dots):
		dots_x.append(random.uniform(-1.0, 1.0))
		dots_y.append(random.uniform(-1.0, 1.0))
	return dots_x, dots_y

def dots_in_circle(dots_x, dots_y):
	dots_in_circle = 0
	for dot_x, dot_y in zip(dots_x, dots_y):
		if dot_x**2 + dot_y**2 <= 1:
			dots_in_circle += 1
	return dots_in_circle

def plot_dots(figname, dots_x, dots_y):
	for dot_x, dot_y in zip(dots_x, dots_y):
		if math.sqrt(dot_x**2 + dot_y**2) <= 1:
			plt.plot(dot_x, dot_y, color="red")
		else:
			plt.plot(dot_x, dot_y, color="blue")
	plt.savefig(figname)

print("1.1")
for n in [1000, 10000, 100000]:
	print("n=", n)
	dots_x, dots_y = dots(n)
	print("n_c=", dots_in_circle(dots_x, dots_y))
	print("4*n_c/n=", 4*dots_in_circle(dots_x, dots_y)/n, "≈pi\n")
	plot_dots(str(n)+"dots.png", dots_x, dots_y)
print("math.pi: ", math.pi)
#... 1.1
# 1.2 ...
#def HyperSphere(dim, numb_dots):
#    dots_in_sphere = 0
#	points=[]
#    for i in range(numb_dots):
#		point=np.array(random.uniform(-1.0, 1.0) for d in range(0,dim))
#		points.append(point)
#        if distance <= 1:
#            dots_in_sphere += 1
#		map(lambda dot: dot**2, points)
#    return np.power(2.0, dim) * (count_in_sphere / iterations)

#print(HyperSphere(10, 100000))
