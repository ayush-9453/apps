pwd = input("What is the master password? ")

def view():
    print("ayush")

def add():
    pass
while True:
    mode = input("Would you like to add a new password or view existing one (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode =="view":
        view()
    elif mode =="add ":
        add() 
    else: 
        print("Invalid mode.")
        continue