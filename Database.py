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
		
	
	def add_entry(unique_ID): pass
	
	def modify_entry(unique_ID): pass
	
	def delete_entry(unique_ID): pass
	
	def save(file_choice= file):
		if file_choice!=file:
			file = file_choice
	
	def close(): pass
	
	