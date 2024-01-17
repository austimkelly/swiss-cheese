import os

filename = input("Please provide a file name to search and display:\n")

command = "cat " + filename
os.system(command)