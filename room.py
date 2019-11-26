from ward import ward

class Room:
	def __init__(self, ward_id, is_free):
		self.__id = ObjectID
		self.ward_id = ward_id
		self.is_free = is_free

	def check_availability(self):
		if self.is_free == True:
			return True
		

# create ward object
# create Room object