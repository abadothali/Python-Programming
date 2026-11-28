# Q) What is Modules??
# -> A module is simply a Python file (.py) that contains reusable code such as: Functions, Variables, Classes, Statements.
# -> We use modules to organize code and reuse it in different programs instead of writing everything again.


import details, msg
acces_details = details.info("monirul",25,"kolkata")
acces_msg = msg.hello("Ram")

print(acces_details)
print(acces_msg)

print(type(acces_msg))
print(type(acces_details))
