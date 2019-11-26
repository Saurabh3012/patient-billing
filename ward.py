from person import Person

class Ward:
	def __init__(self, ward_id, person):
		self.__ward_id = ward_id
		self.__ward_head = person


	def get_ward_head(self):
		return self.__ward_head


p1 = Person("saurabh", "iiit delhi", "30/07/1996", "saurabhg@iiitd.ac.in", "B+")

w1 = Ward(1, p1)

print(w1.get_ward_head().dob)