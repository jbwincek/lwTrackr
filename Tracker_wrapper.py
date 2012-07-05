"""
tracker_wrapper
example change

Variables:
  * action_text: a dictionary that maps short textual representations of actions onto  longer descriptive text
  * action: a short string representation of an action with no capitals or non-alpha characters
  * unclean_action: the user input represented as a number corresponding to the index of an action described in order
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
def greeting(versionNumber): 
	print( """
		Welcome to the tracker app version: %s
			By J B Wincek
			
""" % (versionNumber))

def deal_with_poor_choice(action_text):
	print("We're sorry that text was in some way not able to be intepereted please try again")
	get_action(action_text)
	
def close_application(): quit()

def get_ID():
	# pretty self explanatoy
	unique_ID = raw_input("Please enter your unique user identifier.\n   If you are a new user, pick an ID (a few letters) and enter that.\n   If you are a returning user enter the ID from before.\n: ")
	return unique_ID

def display_action_menu(table):
	"""
	This action menu could be updated to be represented as a list of strings for each action
		that would allow easier adding and indexing of actions to help make parse_input_from()
		more robust
	"""
	print ("			Action Menu\n\nPlease choose an action by entering the corresponding number")
	for i in range(0,len(action_table)): 
		display_action_menu_item(action_table,i)
		

def display_action_menu_item(action_table,index):
	print ( '   %d.)  %s.' % (index, action_table[1]))


def get_action(action_text):
	unclean_action = raw_input(": ")
	# the action NEEDS to be cleaned up before this can go primetime
	action = parse_input_from(unclean_action,action_text)
	return action

def parse_input_from(unclean_action, action_text): 
	"""
  * This is currently an INCOMPLETE function, NEED complete the parsing methods
  * try to parse parse input if it can't parse the input to anything 
  	useful, then call deal_with_poor_choice() 
  	  ERROR: currently this attempt will fail every time, action_text uses words to describe an
  	  but it is attempted with an number
  * takes an unclean input as a string representing a number
  * cleaned_action holds the text that gets cleaned
  * returns a number to be used as the index of the action described by order
	"""
	cleaned_action = ''
	cleaned_action = unclean_action.strip()
	cleaned_action = cleaned_action.lower()
	try:
		# THIS NEEDS TO BE CHANGED (see comment at top) 
		action_text[unclean_action]
	except KeyError:
		#deal with more complicated parsing
		if unclean_action.isdigit():
			if int(unclean_action) > len(action_text) or int(unclean_action) < 0:
				# out of bounds check
				deal_with_poor_choice(action_text)
			else: 
				# unclean_action has been successfully cleaned
				cleaned_action = unclean_action
				
		else: print( 'outer if ')
	else:
		return int(action)


def action_converter(int_action):
	action = '' 
	
	
	return action
def build_action_table(action,order):
	"""
	accepts a clean well formatted action integer 
	Then calls the appropriate database function	
	"""
	
	

	