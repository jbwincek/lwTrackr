""" comprehensions test"""
def func(test):
	return test
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

