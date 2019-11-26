from caretaker import Caretaker
from patient import Patient
from treatmentlog import TreatmentLog
from logging import Logging

class Doctor(Caretaker):
	def __init__(self, type1, name, address, dob, email, bloodgroup, privileges, specialization, opd_timings, patients):
		super().__init__(type1, name, address, dob, email, bloodgroup)
		self.privileges = privileges
		self.specialization = specialization
		self.opd_timings = opd_timings
		self.patients = patients

	def finish_patient_treatment(self, patient):
		if patient in patients:
			self.patients.pop(patient)
			return patients

	def get_patient_treatment_logs(self, patient):
		if patient in patients:
			logs = patient.get_details()
			return logs

	def update_patient_treatment(self, patient, log):
		if patient in patients:
			log.logs.append()