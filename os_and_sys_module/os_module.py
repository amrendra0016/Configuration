# The OS module in Python provides functions for interacting with the operating system.

import os

# Get the current working directory (CWD)
cwd = os.getcwd()
print("Current Working Directory",cwd)

# Changing Directory
print(os.chdir('../')) # equals to cd ..

os.rmdir("test_dir")
os.mkdir("test_dir")
print(os.listdir())

# os.makedirs() method in Python is used to create a directory recursively
os.makedirs("./test_dir/test1/test2")

# os.rmdir() method in Python is used to remove or delete an empty directory.
# OSError will be raised if the specified path is not an empty directory.

# os.remove() method in Python is used to remove or delete a file path.
# This method can not remove or delete a directory.

# os.path.join(parent_dir, directory)  is used to join two paths.
