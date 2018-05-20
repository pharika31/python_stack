from datetime import datetime
class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = self.get_queue_size()

	def get_queue_size(self):
		return len(self.calls)

	def add(self,newCall):
		
		self.calls.append(newCall)

	def remove(self,newCall):
		self.calls.remove(newCall)

	def info(self):
		for call in self.calls:
			print call.display()


class Call(object):
	id = 0
	def __init__(self, caller_name, caller_phone,  reason,time=datetime.now()):
		self.id +=1
		self.caller_name=caller_name
		self.caller_phone=caller_phone
		self.reason=reason
		self.time=time

	def display(self):
		print "call id: %d"%(self.id)
		print "caller name: ",self.caller_name
		print "Caller phone number: ",self.caller_phone
		print "Caller phone time: ",str(self.time)
		print "Call reason: ",self.reason


call1 = Call('Ash', '385-315-2936', 'I want to talk to Coding dojo instructor!')
call1.display()
call_center = CallCenter()
call_center.add(call1)
call_center.info()