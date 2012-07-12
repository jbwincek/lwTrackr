"""
tracker_wrapper
example change

Variables:
  * OUTDATED: action_text: a dictionary that maps short textual representations
  	of actions onto  longer descriptive text
  * action: a short string representation of an action with no capitals or 
  	non-alpha characters
  * unclean_action: the user input represented as a number corresponding to the
  	index of an action described in order
  * versionNumber: a string representing the version
  * order: a list of actions, used to describe the order to present them to the user in

greeting(versionNumber):
  * prints the welcoming text with the versionNumber in it 

get_ID():
  * asks the user for there ID
  * returns their input exactly without any cleaning

parse_input_from(unclean_action,action_text)
  * tries to clean the user entered action to make it match an existing action 
  * if that is impossible call deal_with_poor_choice(action_text) to handle what to do next

display_action_menu(order,action_text)
  * prints general text used to describe available actions to the user and how to input them 
  * calls diplay_action_menu_item(order,action_text,<current index>) to display each individual item

display_action_menu_item(order,action_text,index):
  * uses the variables passed to print a well formatted string that describes the action to the user

get_action(action_text):
  * prompts the user for an action
  * uses parse_input_from(unclean_action,action_text) attempt to to clean the action 
  * returns a cleaned action

deal_with_poor_choice(action_text):
  * tells the user that the input was uninterpretable 
  * calls get_action(action_text) again

if function names in Database.py change, be sure to update the action_handler(action,order) table
"""

import pydoc

def PoorChoice():
	# except for dealing with poor choices 
	def __init__(self, attempted_text, reason):
		self.attempted_text = attempted_text
		self.reason = reason

def greeting(versionNumber): 
	print( """
		Welcome to the tracker app version: %s
			By J B Wincek
			
""" % (versionNumber))
	
def close_application(): quit()

def get_ID():
	# pretty self explanatoy
	unique_ID = raw_input("Please enter your unique user identifier.\n   If you are a new user, pick an ID (a few letters) and enter that.\n   If you are a returning user enter the ID from before.\n: ")
	return unique_ID

def display_action_menu(action_list):
	"""
	uses the text in the action list to build a text based menu for the user
	
	"""
	print ("\t\t\tAction Menu\n\nPlease choose an action by entering the corresponding number")
	print_list = [x[1] for x in action_list]
	for i in range(0,len(print_list)): 
		# pass the human readable action description
		display_action_menu_item(print_list[i],i)
		

def display_action_menu_item(description,action_number):
	print ( '   %d.)  %s.' % (action_number, description))


def get_action(action_list):
	"""
	Takes user input as an action, treats that input as unclean
	The prompt is very short because display_action_menu() builds most of the actual prompt 
	parse_input_from() returns the action as an integer corrosponding to the index of the action
	"""
	unclean_action = raw_input(": ")
	try:
		action = parse_input_from(unclean_action,action_list)
	except PoorChoice,PC:
		deal_with_poor_choice(PC.attempted_text,PC.reason)
	return action

def parse_input_from(unclean_action, action_list): 
	"""
  * This parsing may have some holes in it, but generally it should clean most things
  * try to parse parse input if it can't parse the input to anything useful, 
    then raise a PoorChoice exception
  * takes an unclean input as a string representing a number
  * cleaned_action holds the text while it's being cleaned
  * returns a number to be used as the index of the action described by order
	"""
	cleaning_action = unclean_action.strip()
	cleaning_action = cleaning_action.lower()
	if cleaning_action.isdigit():
		if int(cleaning_action) > len(action_list) or int(cleaning_action) < 0:
			# out of bounds check
			raise PoorChoice(unclean_action,'out of bounds')
		else: 
			# unclean_action has been successfully cleaned
			cleaned_action = cleaning_action 
	else:
		raise PoorChoice(unclean_action,'not a valid option')
	return int(cleaned_action)

def deal_with_poor_choice(attempted_text,reason):
	print( "%s is %s. Please enter one of the listed numbers." % (attempted_text,reason))
	get_action(action_text)

def action_converter(int_action, action_list):
	"""
	converts integer based action representations into string form 
	ie 1 goes to 'add'
	BE CAREFUL: this does not check the passed in variables at all
	"""
	return action_list[int(int_action)][0]
	
def build_action_table(action,order):
	"""
	accepts a clean well formatted action integer 
	Then calls the appropriate database function	
	"""
	
	

	