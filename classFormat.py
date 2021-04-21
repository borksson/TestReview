import setFormat

class Topic():
	def __init__(self, name, explination = "", _set = setFormat.Set(self.name+"_set"), quiz = Quiz()):
		self.name = name
		self.explination = explination
		self.set = _set
		self.quiz = quiz

class Unit():
	def __init__(self, name, topics = [], test = Test()):
		self.name = name
		self.topics = topics
		self.test = test

class Schedual():
	def __init__(self):
		print("FIXME")

class Class():
	def __init__(self, name, units = [], schedual = Schedual(), thresh = 0):
		self.name = name
		self.units = units
		self.schedual = schedual
		self.thresh = thresh

myClass = Class("Spanish 206", thresh = 0.95)