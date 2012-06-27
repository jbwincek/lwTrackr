# mood tracker 
import mood as IM
class InvalidInput: pass

versionNumber = 0.1
database = {}
# database entries are instances of the Mood Class  
# database = {retrieval key : Mood instance}
# testing needs to be done on the appropriate way to name the instances

def addUser(RC):
	mood = IM.Mood()
	database[RC]=mood

def promptForInput():
	"""
	"""
		#prompt the user for input
	print(
		"""
Welcome to the tracker app version: %g
Action list:
	1.) Display all the entries
	2.) Add a new entry
	3.) Modify an existing entry
	4.) Quit the program""" %(versionNumber))
	inputAction = raw_input("Please enter the number corrosponding to the action now:")
	#print(inputAction)
	dealWithInput(inputAction)
	

def dealWithInput(action):
	"""
	See the action list in promptForInput for clarification on action numbers
	These should all be rewritten with try/except blocks when I'm not so tired
	"""
	#print (action)
	if action == '1':
		#call display function once it's written
		pass
	elif action == '3':
		print(" For modifying an entry you need to enter the index number of the entry (they are displayed when you display all the entries), whatever data you are tracking (preferably a number), and a label for that datapoint if you would like.")
		index = raw_input("\tEnter the index:")
	elif action == '2':
		print(" For adding a new entry you need to enter whatever data you are tracking \n  (preferably a number), and a label for that datapoint if you would like.")
	value = raw_input("\tEnter the value:")
	label = raw_input("\tEnter the label (can be blank):")
	print("  You entered %s for the value, and \'%s\' for the label"% (str(value),str(label)) )
	correctChoices = raw_input("\tIs that the data you want to add, please answer y for yes or n for no:")
	if correctChoices == 'y':
		pass
		#do the right action
	elif correctChoices == 'n':
		print ("  Okay, have a another try.")
		dealWithInput(action)
	else:
		print("  %s isn't a y or n, so enter your data again")
		dealWithInput(action)


def run():
	"""
	The main action loop of the program
	Will open database file, 
		the prompt for input, 
		if the user decides to quit: save the database
		if there's an unrecoverable error: close the database without saving
	"""
	try:
		promptForInput()
	except InvalidInput:
		print ("Let's do that again and not enter bad data this time...")
		promptForInput()
	else:
		pass
		#save the database
	finally: 
		pass
		#close the database file (without saving) 
		#quit 
		
run()
#addUser('test')
#database['test'].appendEntry(5.2,'today')