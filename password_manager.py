master_pwd = input("What is the master password?")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip().split("|")[0])
            


def add():
    name = input("Account name: ")
    pswd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pswd + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones?(add|view , press q to quite)")

    if mode == "q":
        break

    if mode == "add":
        add()
    if mode == "view":
        view()
    else:
        print("Invalid mode.")
        continue
