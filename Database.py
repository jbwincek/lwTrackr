import mood as IM
import Database_CLI_Wrapper as CLI
"""
The database module
The database class represents contains all of the users and all of their entries

Currently the plan is to store everything in a dictionary using the unique_ID as a key
	and the value as a instance of the Mood class.

This file should also include methods for user input and display
	eventually just import those functions from somewhere

Database control flow: 
	* database gets init'ed 
		* that sets up the file and dictionary to store the data
	* database.load is called
		* try to open the file (either specified or not)
		* except file error, prompt the user to select another file. 
			then recall load with the new filename
		* else
			* pass the file data into the dictionary

"""

class Database: 
	data = {}
	def __init__(self,*args): 
		file="tracker_data.jbw"
	
	def load(file_choice = file): 
		"""
		load data from a file using default filename unless specified 
		Test how this works with different paths and different running methods (ie cron jobs)
		"""
		if file_choice!=file:
			file = file_choice

		pass
	
	def user_exists(self,unique_ID):
		"""
		Boolean function checking to see if the user exists
		"""
		try:
			self.data[unique_ID]
		except KeyError:
			return False
		else:
			return True
		
		
		
		
		"""
		The following three functions could potentially be broken down into two parts
			1.) get the data
			2.) use the data
		"""
	
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
			pass
		
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
			pass
		
	def delete_entry(unique_ID): pass
	
	def save(file_choice= file):
		if file_choice!=file:
			file = file_choice
	
	def close(): pass
	
	