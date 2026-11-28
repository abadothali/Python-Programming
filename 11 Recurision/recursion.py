# Q) What is recursion??
# -> When function call it self repeatedly, it's call recursion.

def show(msg, time = 0):
    if time == 5 :
        return
    print(time,msg)
    show(msg,time = time+1)

show("Hey Wellcome..")

