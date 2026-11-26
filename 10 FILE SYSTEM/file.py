# Import Os Module -
import os

# Read Mode - 
with open("sample.txt","r") as file:
    print(file.read())

# Write Mode - It's Over Write -
with open("sample.txt","w") as file:
    file.write("I am Abadoth Ali Khan")
    file.write("\nWhat Is Your Name??")

# Append Mode - write data at the end of existing files content.
with open("sample.txt","a") as file:
    file.write("\nI am Python..")

# Deleting A File -
os.remove("temp.py")

