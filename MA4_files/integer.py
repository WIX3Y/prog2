""" Python interface to the C++ Integer class """
import matplotlib.pyplot as plt
import math
import random
import numpy as np
import sys
import time
import concurrent.futures as future

import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes = [ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
		lib.Integer_fib.argtypes = [ctypes.c_void_p]
		lib.Integer_fib.restypes = ctypes.c_int
		lib.Integer_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Integer_new(val)

	def get(self):
		return lib.Integer_get(self.obj)

	def set(self, val):
		lib.Integer_set(self.obj, val)

	def __del__(self):
		return lib.Integer_delete(self.obj)

	def fib(self):
		return lib.Integer_fib(self.obj)

	def fib_py(self, n):
		if n <= 1:
			return n
		else:
			return(self.fib_py(n-1) + self.fib_py(n-2))

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
		if dot_x**2 + dot_y**2 <= 1:
			plt.scatter(dot_x, dot_y, color="red")
		else:
			plt.scatter(dot_x, dot_y, color="blue")
	plt.savefig(figname)

if __name__ == '__main__':
	print("1.1")
	for n in [1000, 10000, 100000]:
		print("n=", n)
		dots_x, dots_y = dots(n)
		print("n_c=", dots_in_circle(dots_x, dots_y))
		print("4*n_c/n=", 4*dots_in_circle(dots_x, dots_y)/n, "≈pi")
#		plot_dots(str(n)+"dots.png", dots_x, dots_y)
	print("math.pi: ", math.pi, "\n")
#... 1.1
# 1.2 ...
def HyperSphere(dim, numb_dots):
	dots_in_sphere = 0
	points=[]
	for i in range(numb_dots):
		point=[random.uniform(-1.0, 1.0) for d in range(0,dim)]
		points.append(point)
	for point in points:
		distance = sum(map(lambda dot: dot**2, point))
		if distance <= 1:
			dots_in_sphere += 1
	return dots_in_sphere

def paralell_HyperSphere(dim, numb_dots, numb_processes):
	numb_sub_dots = [int(numb_dots/numb_processes)]*numb_processes
	dims = [dim]*numb_processes
	with future.ProcessPoolExecutor() as ex:
		result = ex.map(HyperSphere, dims, numb_sub_dots)
	dots_in_sphere = 0
	for r in result:
		dots_in_sphere += r
	print(dots_in_sphere)
	return dots_in_sphere

def Volume(dim):
	return (math.pi**(dim/2))/(math.gamma((dim/2) + 1))

if __name__ == '__main__':
	print("\n1.2")
	print("dim 2", (2**2) * (HyperSphere(2, 100000) / 100000))
	print(Volume(2))
	t_start = time.perf_counter()
	print("dim 11", (2**11) * (HyperSphere(11, 1000000) / 1000000))
	t_stopp = time.perf_counter()
	print("time dim 11, python: ", t_stopp-t_start)
	print(Volume(11))
	t_start = time.perf_counter()
	print((2**2) * (paralell_HyperSphere(11, 1000000, 10) / 1000000))
	t_stopp = time.perf_counter()
	print("time dim 11, c++: ", t_stopp-t_start)
# ... 1.2
# 2 ...
if __name__ == '__main__':
	cpp_fibs = []
	python_fibs = []
	ns = []
	for n in range(30, 32):
		f=Integer(n)

		t1_start = time.perf_counter()
		print(f.fib())
		t1_stopp = time.perf_counter()

		t2_start = time.perf_counter()
		print(f.fib_py(f.get()))
		t2_stopp = time.perf_counter()

		cpp_fibs.append(t1_stopp-t1_start)
		python_fibs.append(t2_stopp-t2_start)
		ns.append(n)

#	plt.scatter(ns, cpp_fibs, color="red")
#	plt.scatter(ns, python_fibs, color="green")
#	plt.savefig("pythonVSc++.png")

#	f=Integer(47)
#	f.fib()
# ... 2
