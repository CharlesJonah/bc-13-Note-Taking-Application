"""
This uses docopt library to allow for a smooth user Interactive session.
Usage:
    note_app note_create <note_content>...
    note_app note_create <note_content>
    note_app note_view <note_id>
    note_app note_delete <note_id>
    note_app note_list <limit>
    note_app note_search <query_string>
    note_app note_import_json <note_id>
    note_app note_export_json <jsonfile_id>
    

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
import os
from note_back import Notes
from docopt import docopt, DocoptExit
nt = Notes()




def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

#This function clears the screen for fresh output
def clear_screen():
    clear = lambda: os.system('cls')
    clear()

#This class ties all the docopt calling functions
class ScreenOut (cmd.Cmd):

    clear_screen()

    #The below statements print a menu to act as a directive to the user
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                               *")
    print("*           NOTE TAKING APPLICATION             *")
    print("*                                               *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                               *")
    print("* USE THE LISTED COMMAND TO EXECUTE TASKS       *")
    print("*                                               *")
    print("* 1. note_create                                *")
    print("*                                               *")
    print("* 2. note_view                                  *")
    print("*                                               *")
    print("* 3. note_delete                                *")
    print("*                                               *")
    print("* 4. note_view_all                              *")
    print("*                                               *")
    print("* 5. note_search                                *")
    print("*                                               *")
    print("* 6. note_delete                                *")
    print("*                                               *")
    print("* 7. import_json                                *")
    print("*                                               *")
    print("* 8. export_json                                *")
    print("*                                               *")
    print("* 9. help                                       *")
    print("*                                               *")
    print("* 10. quit                                      *")
    print("*                                               *") 
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
    print("                                                 ") 

    #The prompt that shows the use that he or she is running form the application in the cmd
    prompt = '(notes_app) '


    # This cmd links to the create() method
    @docopt_cmd
    def do_note_create(self, arg):
        """Usage: note_create <note_content>..."""

        nt.create(' '.join(arg['<note_content>']))
    # This cmd links to the view() method
    @docopt_cmd
    def do_note_view(self, arg):
        """Usage: note_view <note_id>"""

        nt.view(arg['<note_id>'])

    # This cmd links to the delete() method
    @docopt_cmd
    def do_note_delete(self, arg):
        """Usage: note_delete <note_id>"""
        
        
        nt.delete(arg['<note_id>'])

    # This cmd links to the list() method
    @docopt_cmd
    def do_note_list(self, arg):
        """Usage: note_list <limit>"""

        nt.list(arg['<limit>'])
    
           
    # This cmd links to the search() method
    @docopt_cmd
    def do_note_search(self, arg):
        """Usage: note_search <query_string>..."""

        nt.search(' '.join(arg['<query_string>']))

    # This cmd links to the next() method
    @docopt_cmd
    def next_note(self, arg):
        """Usage: next_note <next_word>"""

        noted.nextNote(arg['<next_word>'])


    

    # This cmd allows the user to quit from the app
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        clear_screen()
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("*           NOTE TAKING APPLICATION             *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print("*                                               *")
        print("* BYE! THANK YOU FOR USING THIS APPPLICATION    *")
        print("*                                               *")
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        exit()


ScreenOut().cmdloop()

print(opt)