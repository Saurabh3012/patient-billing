from caretaker import Caretaker
from ward import ward
from doctor import Doctor
import time

class Nurse(Caretaker):
	def __init__(self, type1, name, address, dob, email, bloodgroup, privileges, specialization, opd_timings, assigned_to_ward, assigned_to_doctor):
		super().__init__(type1, name, address, dob, email, bloodgroup)
		self.privileges = privileges
		self.specialization = specialization
		self.opd_timings = opd_timings
		self.assigned_to_ward = assigned_to_ward
		self.assigned_to_doctor = assigned_to_doctor

	def tasks_to_do(self):
		pass

	def is_available(self):
		if time.now in self.opd_timings:
			return True