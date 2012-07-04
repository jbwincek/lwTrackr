""" 
main execution loop

action_table follows the format: 
  * key : index, text to display, function to execute 
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



def launch():
	running = True 
	database = db.Database(order)
	CLI.greeting(versionNumber)
	unique_ID = CLI.get_ID()
	if database.user_exists(unique_ID):
		print "welcome back"
	else:
		print "greetings new user"
	CLI.display_action_menu(action_table)
	action = CLI.get_action(action_table)
	#database.build_action_table(order)
	#db.CLI.evaluate_action(action,unique_ID,order)


launch()