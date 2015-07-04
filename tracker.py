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
import tracker_wrapper as CLI 
import Database as db
import sys
import pdb

versionNumber = '1.0.0'

def func(): pass
# Field actions 


def launch():
	running = True 
	database = db.Database()
	CLI.greeting(versionNumber)
	unique_ID = CLI.get_ID()
	action_list = [
	               ['add_user', 'Add a new user', database.add_user],
	               ['delete_user','Delete a current user', database.delete_user],
				   ['list_fields', 'Display all the fields', database.list_current_fields],
				   ['create_field', 'Create a new field', database.create_new_field],
				   ['delete_field', 'Delete an existing field', database.delete_field],
				   ['entry_interactions', 'create/delete/modify a field entry', database.interact_with_field],
				   ['quit', 'Quit the program', quit ]]

	print(repr(unique_ID))
	try:
		if database.user_exists(unique_ID):
			print("welcome back")
		else:
			print("greetings new user")
			# add user to dabase
			action_list[0][2](unique_ID)
	except TypeError:
		# I have no idea why user_exists(unique_ID) throws a type error
		pass
	#for item in dir(db.wrapper):
	#    if not str(item)[0] == '_':
	#        print(item)
	try:
		while running:
			#sys.cls()
			CLI.display_action_menu(action_list)
			action = CLI.get_action(action_list)
			#pdb.set_trace()
			db.wrapper.evaluate_action(action, unique_ID, action_list)
	except KeyboardInterrupt:
		print("  quiting...")
	#database.build_action_table(order)
	
launch()
