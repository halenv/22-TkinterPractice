"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Noelle Hale.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------

    root = tkinter.Tk()


    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------

    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()

    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    say_hello_button = ttk.Button(frame1, text='Say hello')
    # alternatively, say_hello_button = ttk.Button(frame1, text= print_hello())
    say_hello_button.grid()

    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------

    say_hello_button['command'] = (lambda: print('hello world!'))

    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    hi_bye_button = ttk.Button(frame1, text='Test for ok')
    hi_bye_button['command'] = (lambda: check_for_okay(my_entry_box))
    hi_bye_button.grid()
    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    int_button = ttk.Button(frame1, text='print n times')
    int_button.grid()
    entry2 = ttk.Entry(frame1)
    entry2.grid()
    int_button['command'] = (lambda: print_n_times(entry2, my_entry_box))

    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # -----------------------------------------------------------------
    root.mainloop()

def print_hello():
    print('Hello World!')

def check_for_okay(entry_box):
    contents = entry_box.get()
    if contents == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def print_n_times(entry2, entry_box):
    num_times = int(entry2.get())
    content_to_print = entry_box.get()
    for k in range(num_times):
        print(content_to_print)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

