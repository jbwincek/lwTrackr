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
     
  Methods intended for internal use begin with a _. Example: _clean()
"""

#   ~-~=~-~=~-~=~-~=~-~=~-~=~-~  user related methods  ~-~~=~-~=~-~=~-~=~-~=~-~=~-~=~-~
def add_user(): 
    """
    * Display that we are adding a user
    * get the raw input 
    * parse the raw input 
    * return the well formatted unique_ID to be added
    """
    message = {
                'title' : '~-~-~ ADD USER ~-~-~',
                'body' : 'Please enter a user ID',
                'prompt' : '>'} 
    unique_ID = _prompt(message)
    return unique_ID
    
def delete_user():    
    """
    * Display that we are deleting  a user
    * get the raw input 
    * parse the raw input 
    * return the well formatted unique_ID to be deleted
    """
    message = {
                'title' : '~-~-~ DELETE USER ~-~-~',
                'body' : 'Please enter a user ID',
                'prompt' : '>'} 
    unique_ID =  _prompt(message)
    return unique_ID

#   ~-~=~-~=~-~=~-~=~-~=~-~=~-~=~  field related methods  ~-~~=~-~=~-~=~-~=~-~=~-~=~-~
def create_new_field(unique_ID): 
    """
    get the field name from the wrapper
    #creates an instance of the Field class in unique_ID's storage area. 
    """
    message = {
                'title' : '~-~-~ CREATE A NEW FIELD ~-~-~',
                'body' : 'Please enter a field name',
                'prompt' : '>'} 
    field_name = _prompt(message)
    return field_name


def list_current_fields(unique_ID, fields): 
    """
    List all fields that exist in unique_ID's storage area.
    get's a list of fields passed to it. 
    """
    display_text = '~-~-~ THE CURRENT FIELDS ~-~-~\n\t'

    for field in fields: 
        display_text.append(str(field) + '\n\t')
    print(display_text)
    return

def delete_field(unique_ID): 
    """
    deletes an instance of the Field class in unique_ID's storage area. 
    """
    message = {
                'title' : '~-~-~ DELETE A NEW FIELD ~-~-~',
                'body' : 'Please enter a field name',
                'prompt' : '>'} 
    return _prompt(message)

def interact_with_field(unique_ID, actions): 
    """
    Generalized method for all field interactions, requires a list of available
      actions. 
    """
    field_message = {
                'title' : '~-~-~ SELECT A FIELD ~-~-~',
                'body' : 'Please enter a field name',
                'prompt' : '>'} 
    action_message = {
                'title' : '~-~-~ SELECT AN ACTION ~-~-~',
                'body' : 'Please enter a one of the following actions:',
                'prompt' : '>'} 
    for action in actions: 
        action_message['body'].append("\n\t%s" % action)
    field_name = _prompt(field_message)
    action = _prompt(action_message)
    return (action, field_name)

#   ~-~=~-~=~-~=~-~=~-~=~-~=~-~=~  value related methods  ~-~~=~-~=~-~=~-~=~-~=~-~=~-~
def add_an_entry(unique_ID, field): 
    # present the UI to the user to retrieve value and label
    value_message = {
                'title' : '~-~-~ ENTER A VALUE ~-~-~',
                'body' : "Although value can be anything, a decimal number is recommended",
                'promp' : '>'}
    
    label_message = {
                'title' : '~-~-~ ENTER A LABEL ~-~-~',
                'body' : 'This will be displayed along side the value.\n' +
                            'Blank is an acceptable option.',
                'prompt': '>'}
    
    value = _prompt(value_message)
    label = _prompt(label_message)
    #return the well formatted data
    return value, label
    
def delete_an_entry(unique_ID, field): 
    """This method left intentionally blank and should not be used due to how 
    the values are stored."""
    #get which entry to delete from the wrapper
    #use the data
    pass

def modify_an_entry(unique_ID, field): 
    #get the new value, label, and which entry to modify from the wrapper
    # This method abiguously asks which one without clarifying response format. 
    which_message = {
                'title' : '~-~-~ MODIFY AN ENTRY ~-~-~',
                'body' : 'Choose which entry you would to modify',
                'prompt' : '>'}
    
    value_message = {
                'title' : '~-~-~ ENTER A VALUE ~-~-~',
                'body' : "Although value can be anything, a decimal number is recommended",
                'promp' : '>'}
    
    label_message = {
                'title' : '~-~-~ ENTER A LABEL ~-~-~',
                'body' : 'This will be displayed along side the value.\n' + 
                        'Blank is an acceptable option.',
                'prompt': '>'}
    
    which = _prompt(which_method)
    value = _prompt(value_message)    
    label = _prompt(label_message)
    #use the data
    return index, value, label
    
    
def evaluate_action(action, unique_ID, action_list, *args):
    print (" %s choosen for user %s" % (action, unique_ID))
    try:
        action_list[action][2](unique_ID)
    except KeyError:
    	print('Something went wrong')

#general public methods
def display_error(reason):
#Evaluate if this method is still needed (8/4)
    pass

# ~-~-~-~ private methods 

def _clean(unclean, type, tries, message ):
    # parse unclean until it's consistently clean
    # can raise an InvalidInput error if it's unparsable. 
    
    # ~-~ UNFINISHED as of 8/4 ~-~ 
    # currently the cleaning is not assuredly hardened
    unclean = unclean.strip()
    # strip out all non alphanumeric characters besides '.'
    parts = unclean.partition('.')
    if not (parts[0].isalnum() and parts.isalnum()):
        # called if there is any non alpha numeric besides a single period
        _nasty_input( unclean, type, tries, message)
    
    # try to convert to the right type, handle failures gracefully 
    try: 
        if type == 'int':
            cleaned = int(unclean)
        elif type == 'string': 
            cleaned = string(unclean)
        elif type == 'float':
            cleaned = float(unclean)
    except ValueError:
        _nasty_input( unclean, type, tries, message)
            
    return cleaned
    
def _prompt( message, tries = 3):
    """ Display the message with consistent formatting.
    _prompt(message)
        message contains all the needed display strings as a dictionary
        Currently utilizes these keys:
                'title' : the title of the message 
                'body' : the body of the message
                'prompt' : the prompt to display before the user input
                
                'type' : the expected type of the variable 
                         currently implemented type options are:
                              'string', 'float' and 'int'
            
    Format:
    
    The Title Goes Here
         Tab over for the body
    Prompt
    
     Returns cleaned input of the specified type
     """
    print( '%s\n\t%s' %( message['title'], message['body']))
    return _clean(input( message['prompt']), message['type'], tries, message)
    
def _nasty_input( unclean, type, tries, message):
    """_nasty_input(unclean,type,tries) deals with uncleanable input.
    unclean : the input that failed cleaning
    type : the expected type 
    tries : the remaining number of tries to prompt the user 
    """
    #planned: better explanation of error
    
    # print why this function was called
    print( "Unfortuanately that input is not valid because '%s' is not a %s." + 
            "You have %d more tries to enter a valid input" % (unclean, type, tries)) 

    #planned: add a yes/no question asking the user if they want to try again

    # call prompt again with tries decremented 
    _prompt( message, tries-1)
    
def _yes_no(message):
    # planned: ask the user the message, clean the entered answer and return a boolean
    pass