#!/usr/bin/env python3

import numpy
import sympy

# Name: Keith Hernandez
# Student ID: ID_HERE
# Email: CHAPMAN_EMAIL_HERE
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: HOMEWORK_OR_CLASSWORK_NUMBER

"""Module Description (Replace with your documentation)
The first docstring at the top of the file appears in the "Description" field 
of the help command. That is, if you load a python interpreter the following 
makes the docstring visible:

$ python
import fibonacci
help(fibonacci)

Note the name "your_module" is just the filename without the .py extension.
You can check this field for any other python module (numpy, sympy, etc.) 
to get an idea about how module documentation is usually formatted, and what
information is usually included.

This docstring should contain an overview and purpose of the code being
written below, as well as example uses (if appropriate).
"""


# This is the body of the module.  Place all global constants, function 
# definitions, and class definitions here.  No free-floating executable
# code should appear in a module.

def fibonacci(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(b)
        a, b = b, a+b
    return result

    """Function docstring
    This fibonacci n will take the number n then add the values before it starting with one up to n.
    """

    """Main function
    See below for why this would exist. The local_argv argument lists command
    line arguments taken from sys.argv within the protected main block below.
    """
    """Test function for nosetests
    Any function name starting with prefix test_ will be automatically run
    by nose. Ideally these should be put in a separate file that also
    begins with the prefix test_.
    
    In a test function, use an assert command to test a Boolean statement
    about how your code executed.  If the assert fails, it throws
    an exception, which is caught by nose and reported as a failure.
    Anything that is printed to the screen during this function is
    suppressed unless there is a failure, where it can be used for
    debugging.
    """
    

# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code.

if __name__ == "__main__":
    main()
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.

