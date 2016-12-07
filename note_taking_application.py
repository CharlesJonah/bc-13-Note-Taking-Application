
"""This is the program main file"""
import os
import sqlite3 as lite
import sys


""" This is the main class of the program. It has functions to get user input and output. The modules that compose this class include
    CREATE_NOTE , VIEW_NOTE, DELETE_NOTE , VIEW ALL NOTES , SEARCH NOTE, EXIT FOR PROGRAM. """


class notes:
    #Main menu implementation
    
    #Initializes program variables
    def __init__(self):
        self.a =""
        self.b =""
        self.x = 0
        self.valid = False
        self.note_title = False
        self.note_content = False
        self.con = None

    #Clears screen display before output
    def clear_screen(self):
        clear = lambda: os.system('cls')
        clear()

    #The main menu method
    def main_menu(self): 
        self.clear_screen()
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("*                  NOTEMASTER                   *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("* 1. CREATE  NOTE                               *")
        print("*                                               *")
        print("* 2. VIEW NOTE                                  *")
        print("*                                               *")
        print("* 3. VIEW ALL NOTES                             *")
        print("*                                               *")
        print("* 4. DELETE NOTE                                *")
        print("*                                               *")
        print("* 5. SEARCH NOTES                               *")
        print("*                                               *")
        print("* 6. EXIT                                       *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("                                                 ")
        self.x = input("CHOOSE AN OPTION [ 1 - 6 ] : ")
        print("\n")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("\n")
        
        while self.valid == False:

            if self.x == 1:
                self.valid = True
                self.get_note_title_input(self.a)
                
            elif self.x == 2 :
                self.valid = True
                self.view_single_note()
            elif self.x == 3:
                self.valid = True
                self.view_single_note()   
            elif self.x == 4:
                self.valid = True
                self.del_note()
            elif self.x == 5:
                self.valid = True
                self.search()
            elif self.x == 6 :
                self.valid = True
                exit
            else:
                self.valid == False
                if self.valid == False:
                    self.clear_screen()
                    self.main_menu()
                    self.x=input("WRONG OPTION ! CHOOSE AN OPTION [ 1 - 6 ] : ")
                    print("\n")
                    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                    break

    """ The below function picks user input for the note  """

    def get_note_title_input(self,a):
        a = input("ENTER THE NOTE TITLE OR 0 FOR MAIN MENU: ")
        print("\n")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("\n")
        while self.note_title == False:
            if  a == 0:
                self.clear_screen()
                self.main_menu()

            else:
                if isinstance(a, str):
                    self.a = a
                    self.note_title = True
                    self.get_note_content_input()

                if self.note_content == False:
                    a = input("WRONG INPUT! ENTER THE NOTE TITLE : ")
                    print("\n")
                    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                    print("\n")
                    self.a = a
                    


    def get_note_content_input(self):
        b = input("ENTER YOUR NOTES NOW : \n\n")
        while self.note_content == False:
            if b == 0:
                self.clear_screen()
                self.main_menu()
            else:
                if isinstance(b, str):
                    self.b = b
                    self.note_content = True
                
                if self.note_content == False:
                    b = input("WRONG INPUT! ENTER YOUR NOTES AGAIN : \n\n ")
                    self.b = b

        self.input_view_note()

    def input_view_note(self):

        self.clear_screen()



        state =""

        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("*                  NOTEMASTER                   *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")


        try:
            con = lite.connect('C:\Python34/notes.db')

            with con:
                cur = con.cursor()
                sql = cur.execute("INSERT INTO note  VALUES (null,?, ?)",(self.a, self.b))
                con.commit()
                
                if  sql.rowcount == 1:
                    state = "STATUS: YOUR NOTE HAS BEEN SUCCESFULLY SAVED"



                    print("                                                 ")
                    print( state )
                    print("                                                 ")
                    print(" NOTE TITLE : {0}".format(self.a))
                    print("                                                 ")
                    print(" NOTE CONTENT : {0}".format(self.b))
                    print("                                                 ")
                    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                    print("                                                 ")

                else:
                    state = "STATUS: YOUR NOTE HAS FAILED TO SAVE"

                    print("                                                 ")
                    print( state )
                    print("                                                 ")
                    print("                                                 ")
                    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                    print("                                                 ")
                        
            
        except lite.Error, e:
            
            print ("Error {0}:" .format( e.args[0]))
            sys.exit(1)
            
        finally:
            
            if con:
                con.close()

        


        q = input("ENTER 0 TO GET BACK TO MAIN MENU: ")
        check = False
        while check == False:
            if q == 0:
                self.clear_screen()
                self.main_menu()
            else:
                
                if check == False:
                    print("\n")
                    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                    print("\n")
                    q = input("WRONG INPUT! ENTER 0 TO GET BACK TO MAIN MENU: : ")
                    if q == 0:
                        self.clear_screen()
                        self.main_menu()

    def view_single_note(self):


        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("*                  NOTEMASTER                   *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("                                                 ")


        try:
            con = lite.connect('C:\Python34/notes.db')

            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM note')

                all_rows = cur.fetchall()
                for i in all_rows:

                    nid = i[0]
                    title = i[1]

                    print(" {0} : \t {1}".format(nid,title))

                print("                                                 ")
                    
                print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                print("                                                 ")

                x = str(input("ENTER THE NOTE ID : "))

                cur.execute("SELECT * FROM note WHERE id=?",(x))

                view_note = cur.fetchone()

                for i in view_note:
                    print(i)
                    


        except lite.Error, e:
                
            print ("Error {0}:" .format( e.args[0]))
            sys.exit(1)
                
        finally:
                
            if con:
                con.close()

    def del_note(self):
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("*                  NOTEMASTER                   *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("                                                 ")


        try:
            con = lite.connect('C:\Python34/notes.db')

            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM note')

                all_rows = cur.fetchall()
                for i in all_rows:

                    nid = i[0]
                    title = i[1]

                    print(" {0} : \t {1}".format(nid,title))

                print("                                                 ")
                        
                print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                print("                                                 ")

                x = str(input("ENTER THE NOTE ID : "))

                sql = cur.execute("DELETE FROM note WHERE id=?",(x))

        except lite.Error, e:
            
            print ("Error {0}:" .format( e.args[0]))
            sys.exit(1)
            
        finally:
            
            if con:
                con.close()

    def search(self):

        z = str(input("ENTER SEARCH PHRASE : "))
        print("                                                 ")

        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("*                  NOTEMASTER                   *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("                                                 ")


        try:
            con = lite.connect('C:\Python34/notes.db')

            with con:
                cur = con.cursor()
                cur.execute('SELECT * FROM note')

                all_rows = cur.fetchall()
                for i in all_rows:
                    if str(i[2]).find(z) != -1 :
                        nid = i[0]
                        title = i[1]

                        print(" {0} : \t {1}".format(nid,title))

                print("                                                 ")
                    
                print("* * * * * * * * * * * * * * * * * * * * * * * * *")
                print("                                                 ")

                x = str(input("ENTER NOTE ID TO VIEW : "))

                cur.execute("SELECT * FROM note WHERE id=?",(x))

                view_note = cur.fetchone()

                for i in view_note:
                    print(i)
                    


        except lite.Error, e:
                
            print ("Error {0}:" .format( e.args[0]))
            sys.exit(1)
                
        finally:
                
            if con:
                con.close()









nt = notes()
nt.main_menu()






    


                                                  

 






