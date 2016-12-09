import sqlite3
import json
import sys
import os
from tabulate import tabulate

class Notes(object):
    


    def __init__(self):

        self.notes = ""
        self.search_phrase = ""
        self.del_note_id = ""
        self.notes_input = ""
        self.search = ""
        self.search_dict = {}
        
    
    # This is an autogenerating key method for dictionaries to be created.
    def next_key(self):
        try:
            return max(self.notes.keys())+1
        except ValueError:
            return 1
    
    # This function allows the user to create a note
    def create(self, note_content):

        

        self.notes = note_content 


        try:

            con = sqlite3.connect('notes.db')
            cur = con.cursor()
            sql = cur.execute("INSERT INTO note (content) VALUES (?)",[self.notes])

            con.commit()
            print("\n")
            print("YOUR NOTE HAS BEEN SUCCESFULLY CREATED")
            print("\n")
            
            
        except Exception as e:#(sqlite3.Error, e):
            print("Note creation has failed")
            #print ("Error")\
            #print ("Error {0}:" .format( e.args[0]))
            sys.exit(1)
            
        finally:
            
            if con:
                con.close()
        
       
    # This function allows the user to view a single note .
    def view(self, note_id):
        try:
            self.search_phrase = int(note_id)

            con = sqlite3.connect('notes.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM note WHERE id=?",[self.search_phrase])
            view_note = cur.fetchall()
            headers = ["ID","NOTE"]
            nlist = []

            for i in view_note:

                rows = [i[0], i[1]]
                nlist.append(rows)
            print("\n")
            print(tabulate(nlist, headers, tablefmt="fancy_grid"))
            print("\n")

        except ValueError:
            print ("Wrong input! You did not enter an integer : \n")
        finally:
            
            if con:
                con.close()
     
    # This function allows the user to delete a single note from the database
    def delete(self, note_id):
        try:
            self.del_note_id = int(note_id) 
            con = sqlite3.connect('notes.db')
            cur = con.cursor()
            cur.execute("DELETE FROM note WHERE id=?",[note_id])
            con.commit()

            cur.execute("SELECT * FROM note")
            all_rows = cur.fetchall()

            headers = ["ID","NOTE"]
            nlist = []

            for i in all_rows:

                rows = [i[0], i[1]]
                nlist.append(rows)
            print("\n")
            print("YOUR NOTE HAS BEEN DELETED SUCCESFULLY. BELOW ARE THE NEW NOTES")
            print(tabulate(nlist, headers, tablefmt="fancy_grid"))

        except Exception as e:
            print(e)

    # This function allows the user to view all the notes saved in batches of 20

    def list(self):
        try:
            
            con = sqlite3.connect('notes.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM note")

            all_rows = cur.fetchall()

            headers = ["ID","NOTE"]
            nlist = []

            for i in all_rows:

                rows = [i[0], i[1]]
                nlist.append(rows)

            print("\n")
            print(tabulate(nlist, headers, tablefmt="fancy_grid"))
            print("\n")

                
            
        except Exception as e:
            print(e)
        
        
    # This is a method seaches the database for a phrase similar to what the user has entered
    def note_search(self, query_string):
        self.search = str(query_string)

        try:
            
            con = sqlite3.connect('notes.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM note")

            all_rows = cur.fetchall()

            headers = ["ID","NOTE"]
            nlist = []

            for i in all_rows:
                    if str(i[1]).find(query_string) != -1 :
                        rows = [i[0], i[1]]
                        nlist.append(rows)

            print("\n")
            print("BELOW ARE YOUR SEARCH RESULTS")
            print(tabulate(nlist, headers, tablefmt="fancy_grid"))
            print("\n")


        except Exception as e:
            print(e)

    def export(self,file_name):
        con = sqlite3.connect('notes.db')
        file_name = file_name
        cur = con.cursor()
        cur.execute("SELECT * FROM note")
        result_rows = cur.fetchall()

        with open(file_name +'.json', 'w') as f:
            data = json.dump(result_rows,f,indent=4)

        print("THE EXPORT WAS SUCCESSFULL")
        
        
