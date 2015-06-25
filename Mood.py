# mood.py module 
# contains the mood class
import time
import re



class Mood: 
	"""
	Data is a list of lists laid out like this [time, value, label]
	Most functions will need to catch excepts when calling (usually InvalidInput)
	"""
	def __init__(self):
		self.data = []
		
	def appendEntry(self, value, label = ''):
		"""
		Catch the possibility of InvalidInput when calling this function.
		"""
		if self.inputIsValid(value, label):
			timeEntry = time.time()
			self.data.append([timeEntry,value,str(label)])
			print("appended: \n\ttime: %s\n\tvalue: %s\n\tlabel: %s" % (time.strftime("%B %d %X",time.gmtime(timeEntry)),str(value),label))
		else:
			raise InvalidInput
	
	def modifyEntry(self,index, value, label = '', updateTime=True):
		"""
		Catch the possibility of InvalidInput when calling this function.
		"""
		try: 
			if self.inputIsValid(value, label):
				if updateTime:
					timeEntry=time.time()
				else:
					timeEntry= self.data[index][0]
				self.data[index] = [timeEntry,value,label]
			else: 
				raise InvalidInput
		except IndexError:
			print("error: index value out of bounds")
			raise InvalidInput
	def insertEntry(self,keyBefore,value,label = ''):
		"""
		Don't use this function, it may cause unintended consequences in the data later 
			Specifically the time will be off (until I figure out a way to let the user input the correct time)
		Catch the possibility of InvalidInput when calling this function.
		Currently inserts the current time, which is bad ish
		"""
		if self.inputIsValid(value, label,):
			timeEntry = time.time()
			try:
				self.data.insert(keyBefore,[timeEntry,value,str(label)])
				print("inserted: \n\ttime: %s\n\tvalue: %s\n\tlabel: %s" % (time.strftime("%B %d %X",time.gmtime(timeEntry)),str(value),label))
			except IndexError:
				print("error:index value out of bounds")
				raise InvalidInput
		else:
			raise InvalidInput
	def deleteEntry(self, index):
		pass
	
	def returnEntryAsString(self,index):
		pass

		
	def inputIsValid(self,value, label):
		# this function should go with addEntry
		OK = True
		try:
			float(value)
		except ValueError:
			return false
		#this match is too strict fix that
		#clean = re.match('/w+',label)
		#if clean.group() != label:
		#	return false
		#else: 
		return True
