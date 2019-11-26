class Person:
	def __init__(self, name, address, dob, email, bloodgroup):
		self.name = name
		self.address = address 
		self.dob = dob
		self.email = email
		self.bloodgroup = bloodgroup

	def get_address(self):
		return self.address

	def get_email(self):
		return self.email

	def get_dob(self):
		return self.dob

	def get_bloodgroup(self):
		return self.bloodgroup

	def update_address(self, new_address):
		self.address = new_address
		return True

	def update_email(self, new_email):
		self.email = new_email
		return True
