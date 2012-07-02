"""
Database_CLI Wrapper.py
Contains functions useful for getting user input in a command line interface setting

Plan: 
	This module will be called from and instance the Database class
	Basically this should:
	  * take a list of things to ask the user for as the arguments
	  * for items in the argument list 
	  	* prompt the user to enter that item
	  	* take the input 
	  	* clean the input 
	  		* throw an InvalidInput error if the input is unclean
	  	* append a clean input action onto the return list
	  * return a list of well formatted input items, in the same order they were received

   This should be general enough to take various entries 
   could follow the structure handle_input(action, [needed values])
   then in the handle the for loop would call the appropriate get_entry_item_<action>()
     for each type of entry datapoint to handle
     This would allow for code reuse, even if it looks kinda complicated.
     the needed_entries might not be needed actually
     
   
"""




def get_entry_item_add(): pass

def get_entry_item_modify(): pass

def delete_entry_(): pass

def evaluate_action(action,unique_ID):
	print (" %s choosen for user %s" % (action,unique_ID))


	