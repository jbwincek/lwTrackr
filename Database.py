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

The  three functions modify, add, delete are in the process of being broken down into two parts
	1.) get the data -- this part has been moved into Database_CLI_Wrapper
	2.) use the data
	    * this step means interfacing with the instance of the Mood class keyed by the unique_ID in the data dictionary
	    * mood class has these relevant functions:
	    	* appendEntry(value,label='') 
	    	* modifyEntry(self,index, value, label = '', updateTime=True)
	    	* WARNING: deleteEntry is currently unimplemented
	    	* WARNING: returnEntryAsString is currently unimplemented

"""
import mood as IM
import database_CLI_wrapper as CLI

class Database: 
	data = {}
	action_table = {}
	
	def __init__(self,order,*args): 
		file="tracker_data.jbw"
		action_table = {'display_all':CLI.display_all,'add':CLI.add_entry ,'modify':CLI.modify_entry ,'delete':CLI.delete_entry,'quit':self.quit}
	
	def action_interface(self, action, *args):
		"""
		needs action as a string
		"""
		try:
			self.action_table[action](*args)
		except KeyError:
			print('this error should never be encountered, an errant action slipped into the database')
	
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
	
	def add_entry(unique_ID,value,label):
		"""
		Takes well formatted input and operates on the database with it
		
		WARNING: this isn't using the mood class at all
		"""
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
	
	