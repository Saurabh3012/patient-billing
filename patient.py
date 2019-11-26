from person import Person
from caretaker import Caretaker

class Patient(Person):
	def __init__(self, type, name, address, dob, email, bloodgroup, is_admitted, room_issued):
		super().__init__(name, address, dob, email, bloodgroup)
		self.caretaker = []
		self.is_admitted = is_admitted