""" comprehensions  and other things test"""
def func(test):
	return test
action_list = [
['display_all', 'Display all the entries', func ],
['add', 'Add a new entry', func ],
['modify', 'Modify an existing entry', func],
['delete', 'Delete an entry', func ],
['quit', 'Quit the program', func ] ]
wtp = 2

#  pass the action name to the function for that action
#print [x[2] for x in action_list][wtp]([x[0] for x in action_list][wtp])
#print action_list[wtp][2](action_list[wtp][0])

def display_all():
	print 'displayed everything'
def add_entry():
	print 'added an entry'
def modify_entry():
	print 'modified an entry'
def delete_entry():
	print 'deleted an entry'
def quitter():
	print 'quiting'

action_table = {
				'display_all':display_all,
				'add':add_entry,
				'modify':modify_entry,
				'delete':delete_entry,
				'quit':quitter }


for actions in range(0,len(action_list)):
	action_list[actions][2] = action_table[action_list[actions][0]]

def display(aTab): 
	print ('Current Fields:')
	for field in aTab.keys():
		print( '\t%s' % str(field))
	

display(action_table)

#print [x[1] for x in action_list]
"""
#   ~-~-~-~-~  Exception testing ~-~-~-~-~
class PoorChoice: pass

def raises_PoorChoice():
	raise PoorChoice

try: 
	raises_PoorChoice()
except PoorChoice:
	print 'exception caught'
"""