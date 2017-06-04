from tkinter import *
from random import randint

import data_manipulation


def fct_handler(fn_code):

    global value, f_code, lbl2

    f_code = fn_code
    msg = "Please enter a integer to factorize below:"
    msg1 = ""
    if fn_code == 1:
        msg1 = "Mode: Fermat"
    elif fn_code == 2:
        msg1 = "Mode: Pollard Rho"
    elif fn_code == 3:
        msg1 = "Mode: Trial Division"
    toplevel = Toplevel()
    toplevel.title("Factorization input")
    toplevel.geometry("300x200")
    lbl = Label(toplevel, text=msg, padx=10, pady=10)
    lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
    lbl2 = Label(toplevel, text="", padx=10, pady=10)
    value = StringVar()
    e = Entry(toplevel, textvariable=value)
    button = Button(toplevel, text="OK", command=fetch_fct_res, width=30)
    lbl.pack()
    lbl1.pack()
    e.pack()
    lbl2.pack()
    button.pack()


def mth_handler(fn_code):

    global value, value1, value2, f_code, lbl2

    f_code = fn_code
    toplevel = Toplevel()
    toplevel.title("Math input")
    toplevel.geometry("500x300")
    if fn_code == 1:
        msg = "Enter the taylor exponent below to get the approximate\n" \
              " cumulative distribution of the normal distribution:"
        msg1 = "Mode: Approximate Cumulative Distribution Function"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="")
        value = StringVar()
        e = Entry(toplevel, textvariable=value)
        button = Button(toplevel, text="OK", command=fetch_mth_res_1_input, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        Label(toplevel, text="").pack()
        e.pack()
        Label(toplevel, text="").pack()
        button.pack()
    elif fn_code == 2:
        msg = "Enter two integers below to get their extended greatest common divisor:"
        msg1 = "Mode: Extended Greatest Common Divisor"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="")
        lbl3 = Label(toplevel, text="Integer 1", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Integer 2", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        button = Button(toplevel, text="OK", command=fetch_mth_res_2_inputs, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        Label(toplevel, text="").pack()
        lbl3.pack()
        e1.pack()
        lbl4.pack()
        e2.pack()
        Label(toplevel, text="").pack()
        button.pack()
    elif fn_code == 3:
        msg = "Enter two integers below to get their lowest common multiple"
        msg1 = "Mode: Lowest Common Multiple"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="")
        lbl3 = Label(toplevel, text="Integer 1", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Integer 2", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        button = Button(toplevel, text="OK", command=fetch_mth_res_2_inputs, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        Label(toplevel, text="").pack()
        lbl3.pack()
        e1.pack()
        lbl4.pack()
        e2.pack()
        Label(toplevel, text="").pack()
        button.pack()
    elif fn_code == 4:
        msg = "Enter an integer below to determine if it is prime:"
        msg1 = "Mode: Primality Test"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="")
        value = StringVar()
        e = Entry(toplevel, textvariable=value)
        button = Button(toplevel, text="OK", command=fetch_mth_res_1_input, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        Label(toplevel, text="").pack()
        e.pack()
        Label(toplevel, text="").pack()
        button.pack()
    elif fn_code == 5:
        msg = "Enter an integer below as the limit to the Sieve of Atkin:"
        msg1 = "Mode: Sieve of Atkin"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="")
        value = StringVar()
        e = Entry(toplevel, textvariable=value)
        button = Button(toplevel, text="OK", command=fetch_mth_res_1_input, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        Label(toplevel, text="").pack()
        e.pack()
        Label(toplevel, text="").pack()
        button.pack()
    elif fn_code == 6:
        msg = "Enter an integer below as the limit to the Sieve of Eratosthenes:"
        msg1 = "Mode: Sieve of Eratosthenes"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="")
        value = StringVar()
        e = Entry(toplevel, textvariable=value)
        button = Button(toplevel, text="OK", command=fetch_mth_res_1_input, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        Label(toplevel, text="").pack()
        e.pack()
        Label(toplevel, text="").pack()
        button.pack()
    elif fn_code == 7:
        msg = "Enter an integer below as a parameter for the equation to calculate the Standard Normal\n" \
              " Probability Density :"
        msg1 = "Mode: Standard Normal Probability Density Function"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="")
        value = StringVar()
        e = Entry(toplevel, textvariable=value)
        button = Button(toplevel, text="OK", command=fetch_mth_res_1_input, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        Label(toplevel, text="").pack()
        e.pack()
        Label(toplevel, text="").pack()
        button.pack()


def rnd_handler():

    global value, lbl2

    msg = "Click the button below to receive a random integer:"
    msg1 = "Mode: Mersenne Twister"
    toplevel = Toplevel()
    toplevel.title("Randomization")
    toplevel.geometry("300x200")
    lbl = Label(toplevel, text=msg, padx=10, pady=10)
    lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
    lbl2 = Label(toplevel, text="", padx=10, pady=10)
    button = Button(toplevel, text="Display number", command=fetch_rnd_res, width=30)
    lbl.pack()
    lbl1.pack()
    lbl2.pack()
    button.pack()


def src_handler(fn_code):

    global value1, value2, value3, f_code, lbl2, array, e1, e2, graph

    f_code = fn_code
    array = []
    graph = {}
    toplevel = Toplevel()
    toplevel.title("Searching input")
    toplevel.geometry("500x500")
    if fn_code == 1:
        msg = "Enter a list of integers and the key below to execute a binary search:"
        msg1 = "Mode: Binary Search"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="", padx=10, pady=10)
        lbl3 = Label(toplevel, text="", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Key", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        button = Button(toplevel, text="Enter integer", command=src_submit, width=30)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        button1 = Button(toplevel, text="OK", command=fetch_src_res, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        e1.pack()
        Label(toplevel, text="").pack()
        button.pack()
        lbl4.pack()
        e2.pack()
        lbl3.pack()
        button1.pack()
    elif fn_code == 2:
        msg = "Enter a string and the substring to be found below to execute a BMH search:"
        msg1 = "Mode: BMH Search"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="", padx=10, pady=10)
        lbl3 = Label(toplevel, text="", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Key", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        button1 = Button(toplevel, text="OK", command=fetch_src_res, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        e1.pack()
        Label(toplevel, text="").pack()
        lbl4.pack()
        e2.pack()
        lbl3.pack()
        button1.pack()
    elif fn_code == 3:
        msg = "Enter a graph and the starting node below to execute a DFS search:"
        msg1 = "Mode: Depth First Search"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="", padx=10, pady=10)
        lbl3 = Label(toplevel, text="", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Starting node", padx=10, pady=10)
        lbl5 = Label(toplevel, text="Node", padx=10, pady=10)
        lbl6 = Label(toplevel, text="Edges (enter one at a time)", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        value3 = StringVar()
        e3 = Entry(toplevel, textvariable=value3)
        button1 = Button(toplevel, text="OK", command=fetch_src_res, width=30)
        button2 = Button(toplevel, text="Enter edge", command=enter_edge, width=30)
        button3 = Button(toplevel, text="Submit node and edges", command=submit_node_edges, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        lbl5.pack()
        e1.pack()
        Label(toplevel, text="").pack()
        lbl6.pack()
        e2.pack()
        Label(toplevel, text="").pack()
        button2.pack()
        Label(toplevel, text="").pack()
        button3.pack()
        Label(toplevel, text="").pack()
        lbl4.pack()
        e3.pack()
        lbl3.pack()
        button1.pack()
    elif fn_code == 4:
        msg = "Enter a string and the substring to be found below to execute a KMP search:"
        msg1 = "Mode: KMP Search"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="", padx=10, pady=10)
        lbl3 = Label(toplevel, text="", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Key", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        button1 = Button(toplevel, text="OK", command=fetch_src_res, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        e1.pack()
        Label(toplevel, text="").pack()
        lbl4.pack()
        e2.pack()
        lbl3.pack()
        button1.pack()
    elif fn_code == 5:
        msg = "Enter a string and the substring to be found below to execute a Rabin-Karp search:"
        msg1 = "Mode: Rabin-Karp Search"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="", padx=10, pady=10)
        lbl3 = Label(toplevel, text="", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Key", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        button1 = Button(toplevel, text="OK", command=fetch_src_res, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        e1.pack()
        Label(toplevel, text="").pack()
        lbl4.pack()
        e2.pack()
        lbl3.pack()
        button1.pack()
    elif fn_code == 6:
        msg = "Enter a graph and the starting node below to execute a BFS search:"
        msg1 = "Mode: Breadth First Search"
        lbl = Label(toplevel, text=msg, padx=10, pady=10)
        lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
        lbl2 = Label(toplevel, text="", padx=10, pady=10)
        lbl3 = Label(toplevel, text="", padx=10, pady=10)
        lbl4 = Label(toplevel, text="Starting node", padx=10, pady=10)
        lbl5 = Label(toplevel, text="Node", padx=10, pady=10)
        lbl6 = Label(toplevel, text="Edges (enter one at a time)", padx=10, pady=10)
        value1 = StringVar()
        e1 = Entry(toplevel, textvariable=value1)
        value2 = StringVar()
        e2 = Entry(toplevel, textvariable=value2)
        value3 = StringVar()
        e3 = Entry(toplevel, textvariable=value3)
        button1 = Button(toplevel, text="OK", command=fetch_src_res, width=30)
        button2 = Button(toplevel, text="Enter edge", command=enter_edge, width=30)
        button3 = Button(toplevel, text="Submit node and edges", command=submit_node_edges, width=30)
        lbl.pack()
        lbl1.pack()
        lbl2.pack()
        lbl5.pack()
        e1.pack()
        Label(toplevel, text="").pack()
        lbl6.pack()
        e2.pack()
        Label(toplevel, text="").pack()
        button2.pack()
        Label(toplevel, text="").pack()
        button3.pack()
        Label(toplevel, text="").pack()
        lbl4.pack()
        e3.pack()
        lbl3.pack()
        button1.pack()


def srt_handler(fn_code):

    global value, f_code, lbl2, array, e

    f_code = fn_code
    array = []
    msg = "Please enter a list of integers to sort below:"
    msg1 = ""
    if fn_code == 1:
        msg1 = "Mode: Bogo Sort"
    elif fn_code == 2:
        msg1 = "Mode: Bubble Sort"
    elif fn_code == 3:
        msg1 = "Mode: Cocktail Sort"
    elif fn_code == 4:
        msg1 = "Mode: Comb Sort"
    elif fn_code == 5:
        msg1 = "Mode: Gnome Sort"
    elif fn_code == 6:
        msg1 = "Mode: Heap Sort"
    elif fn_code == 7:
        msg1 = "Mode: Insertion Sort"
    elif fn_code == 8:
        msg1 = "Mode: Merge Sort"
    elif fn_code == 9:
        msg1 = "Mode: Quick Sort"
    elif fn_code == 10:
        msg1 = "Mode: Quick Sort in Place"
    elif fn_code == 11:
        msg1 = "Mode: Selection Sort"
    elif fn_code == 12:
        msg1 = "Mode: Shell Sort"
    toplevel = Toplevel()
    toplevel.title("Sorting input")
    toplevel.geometry("500x300")
    lbl = Label(toplevel, text=msg, padx=10, pady=10)
    lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
    lbl2 = Label(toplevel, text="", padx=10, pady=10)
    lbl3 = Label(toplevel, text="", padx=10, pady=10)
    value = StringVar()
    e = Entry(toplevel, textvariable=value)
    button = Button(toplevel, text="Enter integer", command=submit, width=30)
    button1 = Button(toplevel, text="OK", command=fetch_srt_res, width=30)
    lbl.pack()
    lbl1.pack()
    e.pack()
    lbl2.pack()
    button.pack()
    lbl3.pack()
    button1.pack()


def shf_handler():

    global value, lbl2, array, e

    array = []
    msg = "Please enter a list of integers to shuffle below:"
    msg1 = "Mode: Fisher-Yates/Knuth"
    toplevel = Toplevel()
    toplevel.title("Shuffling input")
    toplevel.geometry("500x300")
    lbl = Label(toplevel, text=msg, padx=10, pady=10)
    lbl1 = Label(toplevel, text=msg1, padx=10, pady=10)
    lbl2 = Label(toplevel, text="", padx=10, pady=10)
    lbl3 = Label(toplevel, text="", padx=10, pady=10)
    value = StringVar()
    e = Entry(toplevel, textvariable=value)
    button = Button(toplevel, text="Enter integer", command=submit, width=30)
    button1 = Button(toplevel, text="OK", command=fetch_shf_res, width=30)
    lbl.pack()
    lbl1.pack()
    e.pack()
    lbl2.pack()
    button.pack()
    lbl3.pack()
    button1.pack()


def fetch_fct_res():
    try:
        a = value.get()
        v = int(a)
        res = data_manipulation.fct_operations(f_code, v)
        lbl2.config(text="Result: " + str(res))
    except ValueError:
        msg = "Please enter an integer!"
        toplevel = Toplevel()
        toplevel.title("Error")
        toplevel.geometry("400x50")
        error = Label(toplevel, text=msg, padx=10, pady=10)
        error.pack()


def fetch_mth_res_1_input():
    try:
        a = value.get()
        v = int(a)
        res = data_manipulation.mth_operations_1_input(f_code, v)
        lbl2.config(text="Result: " + str(res))
    except ValueError:
        msg = "Please enter an integer!"
        toplevel = Toplevel()
        toplevel.title("Error")
        toplevel.geometry("400x50")
        error = Label(toplevel, text=msg, padx=10, pady=10)
        error.pack()


def fetch_mth_res_2_inputs():
    try:
        a = value1.get()
        v1 = int(a)
        b = value2.get()
        v2 = int(b)
        res = data_manipulation.mth_operations_2_inputs(f_code, v1, v2)
        lbl2.config(text="Result: " + str(res))
    except ValueError:
        msg = "Please enter an integer!"
        toplevel = Toplevel()
        toplevel.title("Error")
        toplevel.geometry("400x50")
        error = Label(toplevel, text=msg, padx=10, pady=10)
        error.pack()


def fetch_rnd_res():
    res = data_manipulation.rnd_operations(randint(0, 233189434359823))
    lbl2.config(text="Result: " + str(res))


def fetch_src_res():
    if f_code == 1:
        v1 = array
        a = value2.get()
        v2 = int(a)
    elif f_code == 2 or f_code == 4 or f_code == 5:
        v1 = value1.get()
        v2 = value2.get()
    else:
        v1 = graph
        v2 = value3.get()
    res = data_manipulation.src_operations(f_code, v1, v2)
    lbl2.config(text="Result: " + str(res))


def fetch_srt_res():
    res = data_manipulation.srt_operations(f_code, array)
    lbl2.config(text="Result: " + str(res))


def fetch_shf_res():
    res = data_manipulation.shf_operations(array)
    lbl2.config(text="Result: " + str(res))


def submit():
    try:
        a = value.get()
        v = int(a)
        array.append(v)
        e.delete(0, END)
    except ValueError:
        msg = "Please enter an integer!"
        toplevel = Toplevel()
        toplevel.title("Error")
        toplevel.geometry("400x50")
        error = Label(toplevel, text=msg, padx=10, pady=10)
        error.pack()


def src_submit():
    try:
        a = value1.get()
        v = int(a)
        array.append(v)
        e1.delete(0, END)
    except ValueError:
        msg = "Please enter an integer!"
        toplevel = Toplevel()
        toplevel.title("Error")
        toplevel.geometry("400x50")
        error = Label(toplevel, text=msg, padx=10, pady=10)
        error.pack()


def enter_edge():
    a = value2.get()
    array.append(a)
    e2.delete(0, END)


def submit_node_edges():
    node = value1.get()
    edges = array.copy()
    graph[node] = edges
    array.clear()
    e1.delete(0, END)
