""" 
Main execution loop for lwTrackr

Copyright 2012 J. B. Wincek 
GNU General Public License ver 3. 
written by J. B. Wincek



action_list follows the format: 
  * [ action name, action descriptor text, a function]   
  
  
  LOTS OF VARIABLES HAVE CHANGED NAMES, MAKE SURE THOSE PROPOGATE CORRECTLY 
    * the object formerly known as action_text, became action_table then action_list
  
"""
import tracker_wrapper as CLI, Database as db

versionNumber = '1.0.0'

def func(): pass
action_list = [
['display_all', 'Display all the entries', func ],
['add', 'Add a new entry', func ],
['modify', 'Modify an existing entry', func],
['delete', 'Delete an entry', func ],
['quit', 'Quit the program', func ] 
]

wtp = 2
# print the action name based off of an index number
print [x[2] for x in action_list][wtp]([x[0] for x in action_list][wtp])

print action_list[wtp][2](action_list[wtp][0])



def launch():
	running = True 
	database = db.Database(order)
	CLI.greeting(versionNumber)
	unique_ID = CLI.get_ID()
	if database.user_exists(unique_ID):
		print "welcome back"
	else:
		print "greetings new user"
	CLI.display_action_menu(action_list)
	action = CLI.get_action(action_list)
	#database.build_action_table(order)
	#db.CLI.evaluate_action(action,unique_ID,order)


launch()