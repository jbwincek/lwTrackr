"""
tracker_wrapper
example change

greeting():
	takes 


if function names in Database.py change, be sure to update the action_handler(action,order) table
"""


def greeting(versionNumber): 
	print( """
		Welcome to the tracker app version: %s
			By J B Wincek
			
""" % (versionNumber))

def parse_input_from(action,action_text): 
	"""
	This is currently a stand in function
	NEEDS to be updated to actually parse input
	call deal_with_poor_choice() if appropriate
	takes an unclean input as a number
	returns a string for the actions 
	"""
	try:
		action_text[action]
	except KeyError:
		#deal with more complicated parsing
		if action.isdigit():
			if int(action) > len(action_text) or int(action) < 0:
				print('%s is not a valid action, returning to action menu' % action)
			else: 
				return int(action)
		else: print( 'outer if ')
	else:
		return int(action)
		
		

def deal_with_poor_choice(): pass
	

def close_application(): quit()

def get_ID():
	# pretty self explanatoy
	unique_ID = raw_input("Please enter your unique user identifier.\n   If you are a new user, pick an ID (a few letters) and enter that.\n   If you are a returning user enter the ID from before.\n: ")
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


def get_action(action_text):
	unclean_action = raw_input(": ")
	# the action NEEDS to be cleaned up before this can go primetime
	action = parse_input_from(unclean_action,action_text)
	return action
	
def build_action_table(action,order):
	"""
	accepts a clean well formatted action integer 
	Then calls the appropriate database function	
	"""
	
	

	