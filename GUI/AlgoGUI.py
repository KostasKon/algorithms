from tkinter import *

import functions


# main module which initialises the GUI
def display():

    global dr_list1

    # window creation
    frame = Tk()
    frame.title("nryoung's algorithms graphic interface")
    frame.geometry("500x400")

    # menu bar creation
    menubar = Menu(frame)
    menubar.add_cascade(label="Close", command=close)
    frame.config(menu=menubar)

    # add a greeting/instruction message
    t = 'Welcome to the GUI implementation\n' \
        'for nryoung\'s algorithm library!\n' \
        'Please choose a sublibrary below to get started.'
    var = StringVar()
    var.set(t)
    msg = Label(frame, textvariable=var, padx=10, pady=10)

    # dropdown menu creation for the libraries
    DEFAULTVALUE_OPTION1 = ""
    optionFrame1 = Frame(frame)
    libraries = ['Factorization', 'Math', 'Random', 'Searching', 'Sorting', 'Shuffling']
    selection1 = StringVar()
    dr_list1 = OptionMenu(optionFrame1, selection1, *libraries)
    selection1.set(DEFAULTVALUE_OPTION1)
    dr_list1["width"] = 15

    # choice submission and close buttons
    button1 = Button(frame, text="OK", command=submit)
    button2 = Button(frame, text="Close", command=close)

    # pack all the elements by order of apperance
    msg.pack()
    dr_list1.pack(side=LEFT)
    optionFrame1.pack(pady=100)
    button1.pack(side=LEFT, padx=100)
    button2.pack(side=RIGHT, padx=100)

    # run the GUI
    frame.mainloop()


# collect the user choice and open the appropriate popup
def submit():
    try:
        # read user's choice
        function = dr_list1.cget('text')
        if function is '':
            raise NameError

        # open the appropriate popup
        if function == 'Factorization':
            functions.factorization()
        elif function == 'Math':
            functions.math()
        elif function == 'Random':
            functions.random()
        elif function == 'Searching':
            functions.searching()
        elif function == 'Sorting':
            functions.sorting()
        elif function == 'Shuffling':
            functions.shuffling()
    except NameError:
        msg = "Please select a sublibrary first!"
        toplevel = Toplevel()
        toplevel.title("Error")
        toplevel.geometry("400x50")
        error = Label(toplevel, text=msg, padx=10, pady=10)
        error.pack()


# method to close the window
def close():
    exit()

if __name__ == '__main__':
    display()
