from person import Person

class CareTaker(Person):
	def __init__(self, type, name, address, dob, email, bloodgroup):
		super().__init__(name, address, dob, email, bloodgroup)
		self.type = type


	def get_type(self):
		return self.type



c1 = CareTaker(0, "saurabh", "iiit delhi", "30/07/1996", "saurabhg@iiitd.ac.in", "B+")

print(c1.get_type())
print(c1.get_dob())