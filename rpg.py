#!/usr/bin/env python

from sys import argv
import random

class Die(object):
	def __init__(self):
		random.seed()

	@classmethod
	def roll(self, num):
		return random.randrange(1,num)

class Test(object):
	def __init__(self, name):
		self.name = name

	def post(self):
		print(self.name)

def main(argv):
	random.seed()
	print roll(6)
	print Die.roll(3)
	classTest = Test("Default Name")
	classTest.post()

def roll(num):
	return random.randrange(1,num)

if __name__=="__main__":
	main(argv)