# Field.py module 
# contains the mood class
import time
import re



class Field: 
	"""
	The Field class is used for keeping track of a value, with the ability to 
	include time and an optional label.  
	
	Data is a list of tuples laid out like this (time, value, label)
	Most functions will need to catch excepts when calling (usually InvalidInput)
	
	"""
	def __init__(self):
		self.data = []
		
	def appendEntry(self, value, label = ''):
		"""
		Adds an entry to the end of the list of entries. 
		
		This should be the default function for adding to current entries to be stored. 
		
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
		Modifies an existing entry. 
		
		The time parameter defaults to updating the entry time to current, but
			can be specified to be a previous time. 
			
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
		Don't use this function, it may cause unintended consequences in the 
			data later specifically the time will be off. The data list works
			by having all the items in order with ascending times. 
			(until I figure out a way to let the user input the correct time:
			this should not be used due to the possible issues that could
			arise from times out of order.) 
		Currently inserts the current time, which is bad ish
		
		Catch the possibility of InvalidInput when calling this function.
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
		# this function should go with appendEntry
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
