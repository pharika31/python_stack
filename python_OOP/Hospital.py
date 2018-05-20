class Patient(object):
	id=0
	
	def __init__(self, name, allergies,bed_number=None):
		self.id +=1
		self.name=name
		self.allergies=allergies
		self.bed_number =bed_number

class Hospital(object):
	def __init__(self,name,capacity):
		self.patients=[]
		self.name=name
		self.capacity=capacity

	def admit(self,new_patient):
		if len(self.patients) >= self.capacity:
			print 'The Hospital is full!! Sorry!!'
		else:
			patient_record = {
            'ID': new_patient.id,
            'Name': new_patient.name,
            'Allergies': new_patient.allergies,
            'Bed Number': new_patient.bed_number
            }
			self.patients.append(patient_record)
	def discharge(self,patient_name):
		for patient in self.patients:
			if patient['Name'] == patient_name:
				patient['Bed Number'] == None
				self.patients.remove(patient)
			else:
				print "Sorry! Patient not found."

care_hospital = Hospital('care',3)
patient1 = Patient('Haritha',['gluten','pollen'],1)
patient2 = Patient('abc',['gluten'],3)
patient3 = Patient('Zack',['gluten','shellfish'],2)
patient4 = Patient('Jack',['gluten','shellfish'],4)

care_hospital.admit(patient1)
care_hospital.admit(patient2)
care_hospital.admit(patient3)
care_hospital.admit(patient4)
care_hospital.discharge('Haritha')
care_hospital.admit(patient4)

