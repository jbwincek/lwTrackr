"""
tracker_wrapper
example change

greeting():
	takes 



"""


def greeting(versionNumber): 
	print( """
		Welcome to the tracker app version: %s
			By J B Wincek
			
""" % (versionNumber))

def parse_input_from_(action): 
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

def get_ID():
	unique_ID = raw_input("Please enter your unique user identifier.\nIf you are a new user, pick an ID (a few letters) and enter that.\n:")
	return unique_ID

def display_action_menu(order,action_text):
	"""
	This action menu could be updated to be represented as a list of strings for each action
		that would allow easier adding and indexing of actions to help make parse_input_from()
		more robust
	"""
	print ("			Action Menu\n\nPlease choose an action by entering the corresponding number")
	for i in range(0,len(order)): 
		display_action_menu_item(order,action_text,i)
		

def display_action_menu_item(order,action_text,index):
	print ( '   %d.)  %s.' % (index, action_text[order[index]]))


def get_action():
	unclean_action = input("Please enter the number corrosponding to your choice of action:")
	# the action NEEDS to be cleaned up before this can go primetime
	action = parse_input_from(unclean_action)
	return action
	
	