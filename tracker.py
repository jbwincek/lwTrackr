""" 
main execution loop
"""
import tracker_wrapper as CLI, Database as db

versionNumber = '1.0.0'
action_text = {'display_all':'Display all the entries' ,'add' : 'Add a new entry','modify':'Modify an existing entry','delete':'Delete an entry','quit':'Quit the program'}
order = ['display_all','add' ,'modify' ,'delete','quit']
action_table = {}

	

def launch():
	running = True 
	database = db.Database(order)
	CLI.greeting(versionNumber)
	unique_ID = CLI.get_ID()
	if database.user_exists(unique_ID):
		print "welcome back"
	else:
		print "greetings new user"
	CLI.display_action_menu(order,action_text)
	action = CLI.get_action(action_text)
	#database.build_action_table(order)
	#db.CLI.evaluate_action(action,unique_ID,order)


launch()