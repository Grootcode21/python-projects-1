master_pwd = input("What is the master password?")

def view():
    pass

def add():
    name = input("Account name: ")
    pswdd = input("Password: ")

    with open(name
while True:
    mode = input("Would you like to add a new password or view existing ones?(add|view)")

    if mode == "q":
        break

    if mode == "add":
        add()
    if mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue
