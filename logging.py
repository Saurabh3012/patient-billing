from caretaker import Caretaker
from patient import Patient 
import time

class Logging:
	def __init__(self, by, forp, importance, time, todo_list, summary, task_done, expenses):
		self.__by = by
		self.forp = forp
		self.__importance = importance
		self.time = time.now()
		self.todo_list = todo_list
		self.summary = summary
		self.__task_done = task_done
		self.expenses = expenses


	def mark(self):
		pass

	def get_by(self):
		return self.__by

	def get_importance(self):
		return self.__importance

