def info(name,age):
    print("Name:",name,"Age:",age)

# Positionl Arguments -
info("monirul",25)

# it's the issue, python can't understand what is name and what is age
info(25,"monirul") 

# That's why we need to keywords arguments.
info(age=25, name="monirul")
