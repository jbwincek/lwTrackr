""" 
main execution loop
"""
import tracker_wrapper as CLI, Database

versionNumber = '1.0.0'
action_text = {'display_all':'Display all the entries' ,'add' : 'Add a new entry','modify':'Modify an existing entry','delete':'Delete an entry','quit':'Quit the program'}
order = ['display_all','add' ,'modify' ,'delete','quit']
	

def launch():
	database = Database.Database()
	CLI.greeting(versionNumber)
	CLI.display_action_menu(order,action_text)
	unique_ID = CLI.get_ID()

launch()