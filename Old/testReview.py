import json

#Read in sets, ask to edit or create a set
class Q:
	def __init__(self, question, answers, know = 0):
		self.question = question
		self.answers = answers
		self.know = know

	def getKnow(self):
		return self.know

	def getQ(self):
		return self.question

	def getA(self):
		return self.answers

	def printQ(self):
		print("Q: ", self.question)

	def printA(self):
		print("A: ", self.answers)

	def editQ(self, newQ, newA):
		self.question = newQ
		self.answers = newA

	def testQ(self, testAns):
		print("Q: ", question)
		if(testAns!=answers):
			print("Incorrect!")
			print("The correct answer is: ", answers)

class StudySet:
	def __init__(self, setName):
		self.setName = setName
		self.qList = []

	def getQList(self):
		return self.qList

	def addQ(self, question, answers, know=0):
		newQ = Q(question, answers, know)
		self.qList.append(newQ)

	def printQs(self):
		for Q in self.qList:
			Q.printQ()
			Q.printA()

	def getName(self):
		return self.setName

	def learnQs(self): ...

	def testQs(self): ...

class SetManager:
	def __init__(self):
		self.setList = [];

	def importSet(self, setName, iqList):
		newSet = StudySet(setName)
		if(iqList):
			for QA in iqList:
				newSet.addQ(QA['question'], QA['answers'], QA['know'])
		self.setList.append(newSet)

	def addSet(self, setName):
		newSet = StudySet(setName)
		self.setList.append(newSet)
		
	def getSets(self):
		return self.setList

	def printSets(self):
		if not self.setList:
			print("No sets")
		else:
			print([sets.getName() for sets in self.setList])

	def printSet(self, setName):
		[s for s in self.setList if(s.getName()==setName)][0].printQs()

	def deleteSet(self, setName):
		s = [s for s in self.setList if(s.getName()==setName)]
		self.setList.remove(s[0])

	def editSet(self, setName):
		curSet = [s for s in self.setList if(s.getName()==setName)][0]
		curSet.printQs();
		while(True):
			print("Type 'add question', 'edit question', 'delete question', or 'quit editor'")
			usrIn = input()
			if(usrIn == "quit editor"):
				break
			elif(usrIn == "add question"):
				print("What is the question?")
				Q = input()
				print("What is the answer?")
				A = input()
				curSet.addQ(Q, A)
				print("Question added!")
			elif(usrIn == "edit question"):
				print("FIXME")
			elif(usrIn == "delete question"):
				print("FIXME")
			elif(usrIn == "delete question"):
				print("FIXME")
			else:
				print("Invalid command!")

	def importSets(self, importFile):
		for sets in importFile:
			self.importSet(sets['setName'], sets['qList'])

	def isSet(self, input):
		if(setName in [sets.getName() for sets in self.setList]):
			return(True)
		else:
			return(False)

	def setsToJSON(self):
		export = []
		for sets in self.setList:
			eqList = []
			for Q in sets.getQList():
				eqList.append({"question": Q.getQ(), "answers": Q.getA(), "know": Q.getKnow()})
			export.append({"setName": sets.getName(), "qList": eqList})
		return export

	def setToQuizlet(self, setName):
		eqList = []
		s = [s for s in self.setList if(s.getName()==setName)][0]
		for Q in s.getQList():
			S = ""
			eqList.append(S.join([Q.getQ(),"\t", Q.getA(), "\n"]))
		S = ""
		return S.join(eqList)

def main():
	setManager = SetManager()
	print("Importing data...")
	with open("dataFile.json") as f:
		dataFile = json.load(f)
	setManager.importSets(dataFile)
	f.close()
	print("Data imported!")
	print("Welcome to the Test Review!")
	while(False):
		print("Sets:")
		setManager.printSets()
		print("Type 'add set', 'view set', 'learn set', 'test set', 'edit set', 'delete set', or 'quit'")
		usrIn = input()
		if(usrIn == "add set"):
			print("What is the set name?")
			setName = input()
			if(not setManager.isSet(setName)):
				setManager.addSet(setName)
				print("Set added!")
			else:
				print("Set already exsits!")
		elif(usrIn == "view set"):
			print("What is the set name?")
			setName = input()
			if(setManager.isSet(setName)):
				print("Set: ", setName)
				print("Set questions:")
				setManager.printSet(setName)
			else:
				print("Set doesn't exsit!")
		elif(usrIn == "learn set"):
			print("FIXME")
		elif(usrIn == "test set"):
			print("FIXME")
		elif(usrIn == "edit set"):
			print("What is the set name?")
			setName = input()
			if(setManager.isSet(setName)):
				setManager.editSet(setName)
			else:
				print("Set doesn't exsit!")
		elif(usrIn == "delete set"):
			print("What is the set name?")
			setName = input()
			if(setManager.isSet(setName)):
				setManager.deleteSet(setName)
				print("Set deleted.")
			else:
				print("Set doesn't exsit!")
		elif(usrIn == "quit"):
			break
		else:
			print("Invalid command.")
	#print("Saving...")
	#for sets in setManager.getSets():
	#	with open(sets.getName()+"_quizlet.txt", "w") as f:
	#		f.write(setManager.setToQuizlet(sets.getName()))
	#	f.close()
	#with open("dataFile.json", "w") as f:
	#	json.dump(setManager.setsToJSON(), f)
	#f.close()
	print("Saved.")
	return 0

main()