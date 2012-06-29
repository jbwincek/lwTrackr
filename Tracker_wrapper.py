"""
tracker_wrapper
example change

greeting():
	takes 



"""

def greeting(): 
	print( """
Welcome to the tracker app version: %g
By J B Wincek """ % (versionNumber))

def parse_input_from_( action): 
	"""
	This is currently a stand in function
	NEEDS to be updated to actually parse input
	call deal_with_poor_choice() if appropriate
	takes an unclean input as a number
	returns a string for the actions 
	"""
	return action

def deal_with_poor_choice():
	print("Your choice is not a valid option, please type just the number then hit enter")

def close_application(): pass

def get_ID(unique_ID):
	unique_ID = input("Please enter your unique user identifier.\nIf you are a new user, pick an ID (a few letters) and enter that.")
	return unique_ID

def display_action_menu():
	"""
	This action menu could be updated to be represented as a list of strings for each action
		that would allow easier adding and indexing of actions to help make parse_input_from()
		more robust
	"""
	print ("""
~-~-~-~   Main menu:   ~-~-~-~ 
Available Actions:
	1.) Display all the entries
	2.) Add a new entry
	3.) Modify an existing entry
	4.) Delete an entry
	5.) Quit the program
""")

def get_action():
	unclean_action = input("Please enter the number corrosponding to your choice of action:")
	#the action NEEDS to be cleaned up before this can go primetime
	action = parse_input_from(unclean_action)
	return action
	
	