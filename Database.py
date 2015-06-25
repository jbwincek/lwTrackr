"""
The Database class is based off of a dictionary and contains all the methods
	needed for storing, acessing and modifying all the data in the program. 
"""
import database_CLI_wrapper as wrapper
import Field


class Database(dict):

	def __init__(self):
		pass
	
	# user related methods
	def user_exists(self, unique_ID):
		# check to see if unique_ID is already a user
		# could be reimplemented as self.get(unique_ID, False)
		try:
			self[unique_ID]
			return True
		except KeyError:
			return False

	def add_user(self, unique_ID = None): 
		#get the user name to add from the wrapper
		if not unique_ID:
			unique_ID = wrapper.add_user()
		#create an entry with that username
		self[unique_ID] = {}
	
	def delete_user(self): 
		#get the user name to delete from the wrapper
		unique_ID = wrapper.delete_user()
		#use the data
		del self[unique_ID]
	
	#field related methods
	def create_new_field(self, unique_ID): 
		#get the field name from the wrapper
		field_name = wrapper.create_new_field()
		#creates an instance of the Field class in unique_ID's storage area. 
		self[unique_ID][field_name] = Field()
	
	def list_current_fields(self, unique_ID): 
		#list all fields that exist in unique_ID's storage area.
		wrapper.list_current_fields(unique_ID, self[unique_ID]) 
		pass
	
	def delete_field(self, unique_ID): 
		#get which field to delete from the wrapper
		field_name = wrapper.delete_field(unique_ID)
		#remove the specified field from unique_ID's storage area. 
		del self[unique_ID][field_name]
	
	def interact_with_field(self, unique_ID): 
		field_actions = {
						'add' : self.add_an_entry,
						'delete' : self.delete_an_entry,
						'modify' : self.modify_an_entry
						}
		#get the which action and which field from the wrapper
		(action, field) =  wrapper.interact_with_field(unique_ID,field_actions.keys())
		#call the specified action passing in the unique_ID and the field.
		field_actions[action](unique_ID,field)
		pass
	
	#field interactions
	def add_an_entry(self, unique_ID, field): 
		"""add_an_entry(unique_ID,field) add an value to the specified field"""
		value, label = wrapper.add_an_entry(unique_ID,field)
		self[unique_ID][field].appendEntry(value,label)
	
	def delete_an_entry(self, unique_ID, field): 
		#get which entry to delete from the wrapper
		#use the data
		pass
	
	def modify_an_entry(self, unique_ID, field): 
		#get the new value, label, and which entry to modify from the wrapper
		#use the data
		pass
	
	def display_all(self):
		# (8/1) this method is pending review as to it's necessity
		# (8/4) it is T.T
		wrapper.list_current_fields(unique_ID,self[unique_ID])