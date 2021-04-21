import json

#Question class:
#Types: term, spelling_term, question

class question(object):
	"""docstring for question"""
	def __init__(self, questionType, question, answer, wrongAnswer):
		self.questionType = questionType
		self.question = question
		self.answer = answer
		self.wrongAnswer = wrongAnswer
		
	def toJSON(self):
		return {
	    "questionType": self.questionType,
      "question": self.question,
      "answer": self.answer,
      "wrongAnswer": self.wrongAnswer
		}
		
class Set(object):
	"""docstring for set"""
	def __init__(self, setName, questions = []):
		self.setName = setName
		self.questions = questions
			
	def toJSON(self):
		export = []
		for question in self.questions:
			export.append(question.toJSON())
		return {
			"setName": self.setName,
			"questions": export
		}

sets = []

def importSets(JSONfile):
	with open(JSONfile) as f:
		dataFile = json.load(f)
	f.close()
	for _set in dataFile:
		questions = []
		for _question in _set["questions"]:
			questions.append(question(_question["questionType"], _question["question"], _question["answer"], _question["wrongAnswer"]))
		sets.append(set(_set["setName"], questions))

def addSet(set):
	sets.append(set)

def setsToJSON():
	export = []
	for _set in sets:
		export.append(_set.toJSON())
	return export

def saveSets(JSONfile):
	with open(JSONfile, "w") as f:
		json.dump(setsToJSON(), f)
	f.close()