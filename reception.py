from person import Person
from room import Room
from patient import Patient
from doctor import Doctor
import time

class Reception:
	def __init__(self, onDuty):
		self.onDuty = onDuty

	def allot_room(self, rooms, patient):
		for room in rooms:
			if room.check_availability():
				patient.room_issued = room

	def is_doctor_avail(self, doctors):
		for doctor in doctors:
			if time.now() in doctor.opd_timings:
				return True
