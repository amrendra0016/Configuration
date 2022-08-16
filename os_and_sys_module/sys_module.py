"""The sys module in Python provides various functions and variables that are used to manipulate
different parts of the Python runtime environment.
It allows operating on the interpreter as it provides access to the variables and functions that interact
strongly with the interpreter.
"""

import sys
print(sys.version)

# stdin: It can be used to get input from the command line directly.
# It is used for standard input. It internally calls the input() method.

a=sys.stdin
print(a)

# stdout is used to display output directly to the screen console. Output can be of any form,
# it can be output from a print statement, an expression statement, and even a prompt direct for input.

sys.stdout.write('Geeks')

# stderr: Whenever an exception occurs in Python it is written to sys.stderr.

# sys.argv is a command line argument.
n = len(sys.argv)
print("Total count of sys arguments", n)

#sys.argv[0] is the name of the current Python script.
print("sys.argv[0] is the python script name =",sys.argv[0])
print(sys.argv[1])

# sys.path is a built-in variable within the sys module
# that returns the list of directories that the interpreter will search for the required module.
print(sys.path)

# sys.modules return the name of the Python modules that the current shell has imported.
print(sys.modules)

# sys.exit([arg]) can be used to exit the program.
print(sys.exit("Exiting Program"))
