# pip install cryptography
from cryptography.fernet import  Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password?")



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:",Fernet.decrypt(passw.encode()).decode())
            
#Learn more about cryptography on https://cryptography.io/en/latest/

def add():
    name = input("Account name: ")
    pswd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + str(Fernet.encrypt(pswd.encode()).decode()) + "\n")



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
