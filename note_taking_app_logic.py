import sqlite3 as lighted
import json

class Notes(object):
    


    def __init__(self):

        self.notes = {}
        self.search_phrase = ""
        self.del_note_id = ""
        self.notes_input = ""
        self.search = ""
        
    
    # This is an autogenerating key method for dictionaries to be created.
    def next_key(self):
        try:
            return max(self.notes.keys())+1
        except ValueError:
            return 1
    
    # This function allows the user to create a note
    def create(self, note_content):
        self.notes[self.next_key()] = note_content 
        
        print(self.notes)  
    # This function allows the user to view a single note .
    def view(self, note_id):
        try:
            self.search_phrase = int(note_id) 
            view = self.notes.get(self.search_phrase, "The note ID could not be found  \n")
            print(view)
        except ValueError:
            print ("Wrong input! You did not enter an integer : \n")
     
    # This function allows the user to delete a single note from the database
    def delete(self, note_id):
        try:
            self.del_note_id = int(note_id) 
            if self.del_note_id in self.notes.keys():
                del self.notes[self.del_note_id]
                print ("Note successfully deleted ! \n")
                print (self.notes)
        except ValueError:
            print("Wrong input! Enter ID as an integer: \n")

    # This function allows the user to view all the notes saved in batches of 20

    def list(self, lim):
        fin  = int(lim)
        if fin <= len(self.notes):
            print(self.notes[0:fin])
        else:
            print("Invalid input. Limit should be an Integer")

    # This is a method seaches the database for a phrase similar to what the user has entered
    def note_search(self, query_string):
        self.search = query_string 
        found = []
  
        for i, j in self.notes.items():
            if self.search in j:
                print(i, j)

                

