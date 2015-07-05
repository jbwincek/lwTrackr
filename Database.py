# -*- coding: utf-8 -*-
""" A database for storing lists of generic data fields. """
from collections import abc

class Database(abc.MutableMapping):
    
    #abc implementations 
    def __init__(self,):
        #initialize self.fields to just a dictionary, nothing special
        self.fields = {}

    def __getitem__(self, item):
        """Get either the field or entry specified.
            Arguments: 
                item: expects a string either as a field_name key, or a 
                      field_name dotted with an entry number.
            Usage: 
                'field1'   - > return field1
                'field1.5' - > return 5th entry in field1
            Returns: 
                field (list of namedtuples) or entry (namedtuple)
            Errors: 
                KeyError: if field_name does convert neatly into a possible
                          dictionary key.
                IndexError: if the entry_number is out of bounds 
        """ 
        try:
            field_name, entry_number = item.split('.')
        except ValueError:
            # if statement disguised as exception handling 
            field_name = item
            entry_number = None 
        except AttributeError:
            raise KeyError('Key not a valid string')
        if entry_number is not None:
            return self.fields.get(field_name)[int(entry_number)]
        else:
            return self.fields.get(field_name)

    def __setitem__(self, item = None, value = None):
        """"Set either the field or entry specified to value. 
            Arguments:
                item: expects a string either as a field_name key, or a
                      field_name dotted with an entry number.
                value: should be either a list –– either empty or of well formed
                       namedtuples –– or a namedtuple in the appropriate format
                       for the given field.
            Errors:  
                KeyError: if field_name does convert neatly into a possible
                          dictionary key.
                IndexError: if the entry_number is out of bounds 
            """
        try:
            field_name, entry_number = item.split('.')
        except ValueError:
            # if statement disguised as exception handling 
            field_name = item
            entry_number = None 
        except AttributeError:
            raise KeyError('Key not a valid string')
        if entry_number is not None:
            self.fields[field_name][int(entry_number)] = value
        else:
            self.fields[field_name] = value 

    def __delitem__(self, item = None):
        """ Delete either the field or entry specified. 
            Arguments:
                item: expects a string either as a field_name key, or a
                      field_name dotted with an entry number.
        """
        try:
            field_name, entry_number = item.split('.')
        except ValueError:
            # if statement disguised as exception handling 
            field_name = item
            entry_number = None 
        except AttributeError:
            raise KeyError('Key not a valid string')
        if entry_number is not None:
            self.fields[field_name].pop(int(entry_number))
        else:
            #this may be redudant
            self.fields[field_name].clear()
            del self.fields[field_name]

    def __iter__(self, *, field_name = None):
        if field_name is None: 
            for field in self.fields.values():
                yield from field
        else:
            yield from self.fields[field_name]

    def __len__(self):
        """gives total number of entries in all the fields"""
        total = 0 
        for field in self.fields.values():
            for entry in field:
                total+=1
        return total 


    def add_field(self, *, field_name = None, data_fields = []):
        """create a field in the database with field_name as the name, 
           and data_fields as the slots in the named tuple
           Keyword Arguments: 
                field_name [string] : used to specify fields
                data_fields [list of strings] : specifies what the field should track
            EFFECTS: 
                adds a field to the internal dictionary
            """
        if field_name is not None:
            self.fields[field_name] = data_fields    
        pass

    def delete_field(self,):
        pass

    def modify_field(self,):
        pass

    def construct_field_entry(self,):
        pass

    def add_entry(self,):
        pass

    def delete_entry(self,):
        pass
    
    def modify_entry(self,):
        pass

    def save(self,):
        pass

    def load(self,): 
        pass