class Person:
	def __init__(self):
		self.name = name
		self.__address = address 
		self.__dob = dob
		self.__email = email
		self.__bloodgroup = bloodgroup

	def get_address(self):
		return self.__address

	def get_email(self):
		return self.__email

	def get_dob(self):
		return self.__dob

	def get_bloodgroup(self):
		return self.__bloodgroup

	def update_address(self, new_address):
		self.__address = new_address
		return True

	def update_email(self, new_email):
		self.__email = new_email
		return True
