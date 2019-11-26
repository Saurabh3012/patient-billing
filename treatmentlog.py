from patient import Patient
from logging import Logging
from collections import defaultdict

class TreatmentLog:
	def __init__(self, id, of, logs, active):
		self.id = id
		self.of = of
		self.logs = logs[:]
		self.active = active

	def add_to_log(self, new_log):
		self.logs.append(new_log)

	def mark_unactive(self):
		self.active = False

