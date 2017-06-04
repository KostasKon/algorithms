from tkinter import *

import input_handling

# the different popups that show the functions available, all are identical code-wise, the only thing that
# changes is the displayed messages


# popup for handling factorization
def factorization():

    global v

    toplevel = Toplevel()
    toplevel.title("Factorization")

    # add a greeting/instruction message
    t = 'This is the factorization module.' \
        ' Pick a factorization function, press OK\n' \
        'and proceed.'
    info = StringVar()
    info.set(t)
    msg = Label(toplevel, textvariable=info, justify=LEFT, padx=10, pady=10)
    msg.pack()

    v = IntVar()
    v.set(1)

    types = [
        ("Fermat: Fermat’s factorization method is based on the\n"
         "representation of an odd integer as the difference of two squares.", 1),
        ("Pollard Rho Algorithm: Pollard’s rho algorithm is a special-purpose\n"
         "integer factorization algorithm. It was invented by John Pollard in 1975.\n"
         "It is particularly effective for a composite number having a small prime factor.", 2),
        ("Trial Division: Trial division is the most laborious but easiest to understand of\n"
         "the integer factorization algorithms.\nTry to divide a number n by all prime numbers < sqrt(n).", 3),
    ]

    for txt, val in types:
        Radiobutton(toplevel,
                    text=txt,
                    justify=LEFT,
                    padx=20,
                    variable=v,
                    value=val).pack(anchor=W)

    button = Button(toplevel, text="OK", command=fct_choice, width=10)
    button.pack()


# popup for handling math
def math():

    global v

    toplevel = Toplevel()
    toplevel.title("Math")

    # add a greeting/instruction message
    t = 'This is the math module.' \
        ' Pick a math function, press OK\n' \
        'and proceed.'
    info = StringVar()
    info.set(t)
    msg = Label(toplevel, textvariable=info, justify=LEFT, padx=10, pady=10)
    msg.pack()

    v = IntVar()
    v.set(1)

    types = [
        ("Approximate Cumulative Distribution Function: Calculates\n"
         "the cumulative distribution function of the normal distribution.\n"
         "Uses a Taylor exponent to calculate this.", 1),
        ("Extended Greatest Common Divisor: Finds the greatest common divisor and returns it.", 2),
        ("Lowest Common Multiple: Finds the lowest common multiple and returns it.", 3),
        ("Primality Test: Takes a number as an input and determines if it is prime.", 4),
        ("Sieve of Atkin: Optimized version of the ancient sieve of Eratosthenes which does some\n"
         "preliminary work and then marks off multiples of the square of each prime, rather than multiples\n"
         "of the prime itself. It was created in 2004 by A. O. L. Atkin and Daniel J. Bernstein.", 5),
        ("Sieve of Eratosthenes: a simple, ancient algorithm for finding all prime numbers up\n"
         "to any given limit. It does so by iteratively marking as composite (i.e. not prime)\n"
         "the multiples of each prime, starting with the multiples of 2.", 6),
        ("Standard Normal Probability Density Function: Calculates the normal distribution’s\n"
         "probability density function (PDF). Calculates Standard normal PDF for mean=0, std_dev=1.", 7)
    ]

    for txt, val in types:
        Radiobutton(toplevel,
                    text=txt,
                    justify=LEFT,
                    padx=20,
                    variable=v,
                    value=val).pack(anchor=W)

    button = Button(toplevel, text="OK", command=mth_choice, width=10)
    button.pack()


# popup for handling random
def random():

    global v

    toplevel = Toplevel()
    toplevel.title("Random")

    # add a greeting/instruction message
    t = 'This is the random module.' \
        ' Pick a function, press OK\n' \
        'and proceed.'
    info = StringVar()
    info.set(t)
    msg = Label(toplevel, textvariable=info, justify=LEFT, padx=10, pady=10)
    msg.pack()

    v = IntVar()
    v.set(1)

    types = [
        ("Mersenne Twister: Generates high quality pseudo random integers\n"
         "with a long period. Used as the default random number generator\n"
         "for several languages (including Python).", 1),
    ]

    for txt, val in types:
        Radiobutton(toplevel,
                    text=txt,
                    justify=LEFT,
                    padx=20,
                    variable=v,
                    value=val).pack(anchor=W)

    button = Button(toplevel, text="OK", command=rnd_choice, width=10)
    button.pack()


# popup for handling searching
def searching():

    global v

    toplevel = Toplevel()
    toplevel.title("Searching")

    # add a greeting/instruction message
    t = 'This is the searching module.' \
        ' Pick a search function, press OK\n' \
        'and proceed.'
    info = StringVar()
    info.set(t)
    msg = Label(toplevel, textvariable=info, justify=LEFT, padx=10, pady=10)
    msg.pack()

    v = IntVar()
    v.set(1)

    types = [
        ("Binary Search: Takes a list of integers as an input and recursively\n"
         "partitions it until the key is found.", 1),
        ("BMH Search: Search that attempts to find a substring in a string.\n"
         "Uses a bad-character shift of the rightmost character of the window to compute shifts.", 2),
        ("Depth First Search: Recursive implementation of the depth first search algorithm\n"
         "used to traverse trees or graphs. Starts at a selected node (root) and explores\n"
         "the branch as far as possible before backtracking.", 3),
        ("KMP Search: Searches for occurrences of a “word” within a main “string”\n"
         "by employing the observation that when a mismatch occurs, the word itself\n"
         "embodies sufficient information to determine where the next match could begin,\n"
         "thus bypassing re-examination of previously matched characters.\n"
         "Uses a prefix function to reduce the searching time.", 4),
        ("Rabin-Karp Search: Search for a substring in a given string, by comparing hash\n"
         "values of the strings.", 5),
        ("Breadth First Search: Recursive implementation of the breadth first search algorithm\n"
         "used to traverse trees or graphs. Starts at a selected node (root) and explores\n"
         "its neighbors as far as possible before backtracking.", 6)
    ]

    for txt, val in types:
        Radiobutton(toplevel,
                    text=txt,
                    justify=LEFT,
                    padx=20,
                    variable=v,
                    value=val).pack(anchor=W)

    button = Button(toplevel, text="OK", command=src_choice, width=10)
    button.pack()


# popup for handling sorting
def sorting():

    global v

    toplevel = Toplevel()
    toplevel.title("Sorting")

    # add a greeting/instruction message
    t = 'This is the sorting module.' \
        ' Pick a sorting function, press OK\n' \
        'and proceed. Note that all functions work with integers only.\n'

    info = StringVar()
    info.set(t)
    msg = Label(toplevel, textvariable=info, justify=LEFT, padx=10, pady=10)
    msg.pack()

    v = IntVar()
    v.set(1)

    types = [
        ("Bogo Sort: A naive sorting that picks two elements at random and swaps them.\n"
         "WARNING: This algorithm may never sort the list correctly.", 1),
        ("Bubble Sort: A naive sorting that compares and swaps adjacent elements.", 2),
        ("Cocktail Sort: A bidirectional bubble sort. Walks the elements\n"
         "bidirectionally, swapping neighbors if one should come before/after the other.", 3),
        ("Comb Sort: Improves on bubble sort by using a gap sequence to remove turtles.", 4),
        ("Gnome Sort: A sorting algorithm similar to insertion sort except that\n"
         "the element is moved to its proper place by a series of swaps.", 5),
        ("Heap Sort: Uses the max heap data structure implemented in a list.", 6),
        ("Insertion Sort: A sort that uses the insertion of elements\n"
         "in to the list to sort the list.", 7),
        ("Merge Sort: Uses \'divide and conquer\' to recursively divide and sort the list.", 8),
        ("Quick Sort: Uses partitioning to recursively divide and sort the list.", 9),
        ("Quick Sort in Place: Uses partitioning to recursively divide and sort the list.", 10),
        ("Selection Sort: A sorting that uses in-place comparison.", 11),
        ("Shell Sort: Comparision sort that sorts far away elements first to sort the list.", 12)
    ]

    for txt, val in types:
        Radiobutton(toplevel,
                    text=txt,
                    justify=LEFT,
                    padx=20,
                    variable=v,
                    value=val).pack(anchor=W)

    button = Button(toplevel, text="OK", command=srt_choice, width=10)
    button.pack()


# popup for handling shuffling
def shuffling():

    global v

    toplevel = Toplevel()
    toplevel.title("Shuffling")

    # add a greeting/instruction message
    t = 'This is the shuffling module.' \
        ' Pick a shuffling function, press OK\n' \
        'and proceed.'
    info = StringVar()
    info.set(t)
    msg = Label(toplevel, textvariable=info, justify=LEFT, padx=10, pady=10)
    msg.pack()

    v = IntVar()
    v.set(1)

    types = [
        ("Fisher-Yates/Knuth: Takes a list of integers as an input and randomly\n"
         "swaps the elements in an unbiased manner.", 1),
    ]

    for txt, val in types:
        Radiobutton(toplevel,
                    text=txt,
                    justify=LEFT,
                    padx=20,
                    variable=v,
                    value=val).pack(anchor=W)

    button = Button(toplevel, text="OK", command=shf_choice, width=10)
    button.pack()


# the next 6 methods invoke the appropriate method for the function the user has selected

def fct_choice():
    choice = v.get()
    input_handling.fct_handler(choice)


def mth_choice():
    choice = v.get()
    input_handling.mth_handler(choice)


def rnd_choice():
    input_handling.rnd_handler()


def src_choice():
    choice = v.get()
    input_handling.src_handler(choice)


def srt_choice():
    choice = v.get()
    input_handling.srt_handler(choice)


def shf_choice():
    input_handling.shf_handler()
