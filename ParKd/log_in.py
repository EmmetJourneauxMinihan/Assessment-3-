from cryptography.fernet import Fernet
import signup



def produce_key():
    key = Fernet.generate_key()
    open("master.key", 'wb').write(key)
    open("master.key", 'rb').close()
    return key


def key_load():
    try:
        key = open("master.key", 'rb').read()
        open("master.key", 'rb').close()
        hash_key = Fernet(key)
    except:
        produce_key()
        hash_key = key_load()
    return hash_key



    
def encp(username, password):
    user_pass = "pass_vault/" + username + ".txt"
    key_prep = key_load()
    f_encp = key_prep.encrypt(password)
    open(user_pass, "wb").write(f_encp)
    open(user_pass, "rb").close()




def decp(username):
    
    try:
        user_pass = "pass_vault/" + username + ".txt"
        f_encp = open(user_pass, "rb").read()
        key_prep = key_load()
        raw = key_prep.decrypt(f_encp)
        return raw

    except:
        print("No user found. Please create an account.")
        return 1




class ui:
    username = None
    password = None


    def __init__(self):
        self.username = input("PLease enter username:")
        self.password = input("Please enter password:")


    def pass_check(self):
        raw = decp(self.username)
        if raw != 1:
            raw_pass = raw.decode()
            if raw_pass == self.password:
                print("login successful")
                return 1 
    
            else:
                choice = input("Invalid credentials. Choose an option.\n(t)Try again\t(x)Exit")
                if choice == "t":
                    tempv2 = ui().pass_check()
                    return tempv2
               
                elif choice == "x":
                    exit(0)
                
                else:
                    print("Invalid input. Try again")
        
    

   
    @staticmethod
    def guest():
        username = "guest"
        password = "password"
        user = input("Please enter username:")
        key = input("Please enter password:")
        
        if username == user:
            if key == password:
                print("Login successful.")
                print("This is just a test.")
                        
        else:
            print("Invalid credentials. Access denied.")


def user_access():
    choice = input("Login as: (g)Guest\t(u)User login\t\t(n)New user\t(x)Exit\n::")

 
    if choice == 'x':
        exit(0)    


    elif choice == 'n':
        (username, password) = signup.new_user()
        password = password.encode()
        encp(username, password)
        

    elif choice == 'g':
        ui.guest()
        

    elif choice == 'u':
        var = ui().pass_check()
        return var
    else:
        print("Invalid input. Try again later.")
            
    user_access()


def main():
    print("-----------------------------")
    print("Welcome to the dashboard.")
    print("-----------------------------")
    
    #More modules to be added in this section

        

user_pass = user_access()
if user_pass == 1:
    main()
    
import msvcrt as m
m.getch()