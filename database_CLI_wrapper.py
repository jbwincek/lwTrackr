"""
Database_CLI Wrapper.py
Contains functions useful for getting user input in a command line interface setting

Plan: 
	This module will be called from and instance the Database class
	Basically this should:
	  * take a list of things to ask the user for as the arguments
	  * for items in the argument list 
	  	* prompt the user to enter that item
	  	* take the input 
	  	* clean the input 
	  		* throw an InvalidInput error if the input is unclean
	  	* append a clean input action onto the return list
	  * return a list of well formatted input items, in the same order they were received

   This should be general enough to take various entries 
   could follow the structure handle_input(action, [needed values])
   then in the handle the for loop would call the appropriate get_entry_item_<action>()
     for each type of entry datapoint to handle
     This would allow for code reuse, even if it looks kinda complicated.
     the needed_entries might not be needed actually
     
   
"""

# user related methods
def add_user(): 
	"""
	* Display that we are adding a user
	* get the raw input 
	* parse the raw input 
	* return the well formatted unique_ID to be added
	"""
	message = {
				'title' : '~-~-~ ADD USER ~-~-~',
				'body' : 'Please enter a user ID',
				'prompt' : '>'} 
	unclean_unique_ID = _prompt(message)
	unique_ID = _clean(unclean_unique_ID)
	return unique_ID
	
def delete_user():	
	"""
	* Display that we are deleting  a user
	* get the raw input 
	* parse the raw input 
	* return the well formatted unique_ID to be deleted
	"""
	message = {
				'title' : '~-~-~ DELETE USER ~-~-~',
				'body' : 'Please enter a user ID',
				'prompt' : '>'} 
	unclean_unique_ID =  _prompt(message)
	unique_ID = _clean(unclean_unique_ID)
	return unique_ID

#field related methods
def create_new_field(unique_ID): 
	"""
	get the field name from the wrapper
	#creates an instance of the Field class in unique_ID's storage area. 
	"""
	message = {
				'title' : '~-~-~ CREATE A NEW FIELD ~-~-~',
				'body' : 'Please enter a field name',
				'prompt' : '>'} 
	unclean_field_name =  _prompt(message)
	field_name = _clean(unclean_field_name)
	return field_name


def list_current_fields(unique_ID, fields): 
	"""
	List all fields that exist in unique_ID's storage area.
	get's a list of fields passed to it. 
	"""
	display_text = '~-~-~ THE CURRENT FIELDS ~-~-~\n\t'

	for field in fields: 
		display_text.append(str(field) + '\n\t')
	print display_text
	return

def delete_field(unique_ID): 
	"""
	deletes an instance of the Field class in unique_ID's storage area. 
	"""
	message = {
				'title' : '~-~-~ DELETE A NEW FIELD ~-~-~',
				'body' : 'Please enter a field name',
				'prompt' : '>'} 
	return _prompt(message)

def interact_with_field(unique_ID,actions): 
	"""
	returns well formated action code add  
	"""
	field_message = {
				'title' : '~-~-~ SELECT A FIELD ~-~-~',
				'body' : 'Please enter a field name',
				'prompt' : '>'} 
	unclean_field_name =  _prompt(message)
	field_name = _clean(unclean_field_name)
	action_message = {
				'title' : '~-~-~ SELECT AN ACTION ~-~-~',
				'body' : 'Please enter a one of the following actions:',
				'prompt' : '>'} 
	for action in actions: 
		action_message['body'].append("%s\n\t" % action)
	action = _prompt(message)
	return action, field_name

#field interactions
def add_an_entry(unique_ID,field): 
	#get the value and label from the wrapper
	#use the data
	pass

def delete_an_entry(unique_ID,field): 
	#get which entry to delete from the wrapper
	#use the data
	pass

def modify_an_entry(unique_ID,field): 
	#get the new value, label, and which entry to modify from the wrapper
	#use the data
	pass
	
	
def evaluate_action(action,unique_ID):
	print (" %s choosen for user %s" % (action,unique_ID))

#private methods
def _get_unclean():
	unique_ID = ''
	return unique_ID
	
def _clean(unclean):
	#parse unclean until it's consistently clean
	cleaned = unclean
	return cleaned
	
def _prompt(message):
	""" Display the message with consistent formatting.
	Format:
	
	The Title Goes Here
		 Tab over for the body
	Prompt
	
	 """
	print( '%s\n\t%s' % (message['title'], message['body']))
	return _clean(raw_input( message['prompt']))
	