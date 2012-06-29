import mood as IM
"""
The database module
The database class represents contains all of the users and all of their entries

Currently the plan is to store everything in a dictionary using the unique_ID as a key
	and the value as a instance of the Mood class.

This file should also include methods for user input and display
	eventually just import those functions from somewhere
"""

class Database: 
	
	def __init__: 
		data = []
		file="tracker_data.jbw"
	
	def load(file_choice = file): 
		"""
		load data from a file using default filename unless specified 
		Test how this works with different paths and different running methods (ie cron jobs)
		"""
		if file_choice!=file:
			file = file_choice

		pass
	
	def user_exists(unique_ID):
		"""
		Boolean function checking to see if the user exists
		"""
		if not data[unique_ID]:
			return True
		else: 
			return False 
		
	
	def add_entry(unique_ID):
		"""
		These functions will need to prompt the user for information
			asks for the value of the entry to enter, and any label
			
			I could make appendEntry except arbitrarily long lists of input, in case the user wants that
		"""
		## get value
		## get label
		try:
			data[unique_ID].appendEntry(value,label)
		except InvalidInput:
			#deal with bad input
	
	def modify_entry(unique_ID): 
		"""
		These functions will need to prompt the user for information
			asks for the value of the entry to enter, and any label
		"""
		## get which entry to modify
		## get value
		## get label
		## ask if they want the current or original time
		try:
			data[unique_ID].modifyEntry(index,value,label,time)
		except InvalidInput:
			#deal with bad input
		
	def delete_entry(unique_ID): pass
	
	def save(file_choice= file):
		if file_choice!=file:
			file = file_choice
	
	def close(): pass
	
	