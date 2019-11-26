from logging import Logging

class Expenses:
	def __init__(self, for_log, amount):
		self.for_log = for_log
		self.__amount = amount

	def clear(self):
		self.__amount = 0