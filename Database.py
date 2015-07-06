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
        """Iterate through all the entries in all or the specified field. """
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


    def add_field(self, *, field_name = None, data_fields = None):
        """Create a field in the database with field_name as the name, 
           and data_fields as the slots in the named tuple.
           Keyword Arguments: 
                field_name [string] : used to specify fields
                data_fields [list of strings] : specifies what the field should track
            Effects: 
                adds a field to the internal dictionary
                updates dictionary with [field_name]_tuple to include a list of 
                    data fields this field tracks. Used for when adding entries 
                    to the field. 
            """
        if field_name is not None and data_fields is not None:
            self.fields[field_name] = [] 
            Field = namedtuple('Field', data_fields)
            self.fields[field_name+'_tuple'].append(Field)   
        pass

    def delete_field(self, field_name = None):
        """Deletes specified field."""
        del self.fields[field_name]

    def modify_field(self, field_name = None, data_fields = None, rewrite = False):
        """Modifies what a field tracks.
            Keyword Arguments: 
                field_name [string] : used to specify in which field to modify
                data_fields [list of strings] : the new list of things the field
                                                should track.
                rewrite [boolean] : whether to erase and start afresh with the 
                                    field, or just switch to using new data 
                                    fields from this point forward.
            Effects: 
                changes specified field to track new data
                if rewrite is True, it will erase all the existing entries in 
                    the specified field, use with caution. 
        """
        pass

    def add_entry(self, *, field_name = None, index = None, **kwargs):
        """Add an entry using kawgs as the data_fields.
            Keyword Arguments:
                field_name [string] : used to specify in which field to add the 
                                      entry to. 
                index [int] : if specified it will insert the entry at index,
                              otherwise it will append to the end of the list.
                kwargs : must be valid data field names.
            Effects:
                adds an entry to the specified field
            Errors:
                AttributeError if kwargs don't match up perfectly to the data_fields
                KeyError if field_name is not actually a field
                IndexError if the index is out of the bounds of the list
        """
        pass

    def delete_entry(self, *, field_name = None, index = None):
        """ Delete the entry at index in field_name
            Keyword Arguments:
                field_name [string] : used to specify in which field to delete
                index [int] : the index of the entry to delete 
            Effects:
                deletes the specifed entry
            Errors:
                KeyError if field_name is not actually a field
                IndexError if the index is out of the bounds of the list
        """"
        pass
    
    def modify_entry(self,):
        pass

    def save(self,):
        pass

    def load(self,): 
        pass