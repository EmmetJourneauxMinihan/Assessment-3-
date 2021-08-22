##########This module is called by log_in_final.py#############
##########This module is called by log_in_final.py#############
##########This module is called by log_in_final.py#############

import smtplib
import random as r
import time



def sign_up():
    print("Welcome. PLease sign up with your email.")

    username = input("|-Please enter your email:")
    password = input("|-PLease enter a password:")
    
    return username, password




def verify(email):
    try: 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 
        print("|-Wait..........")
        
        smtp.starttls() 
        smtp.login("testparkd4@gmail.com","tess4tess4")
        verification_code = r.randint(100000,999999)
        
        
        message = "Hi, \nThis is a verfication email.\nYour verification code is"+ str(verification_code)
        smtp.sendmail("testparkd4@gmail.com", email, message) 
        smtp.quit() 
        
        for i in range(4):
            print("|------|")
            time.sleep(.1)
        print ("|-Email sent successfully!")
        return verification_code

    except Exception as ex: 
        print("Something went wrong....",ex) 
        return 1




def user_verification(var_check, username, password):
    print("---------------------")
    print("Please check your email for the varification code.")
    var = int(input("Once received please input the varification code here:"))
    temp = int(var_check)

    if var == temp:
        print("---------------------")
        print("User varified.")
        open("credentials.csv", 'a').write(username + "," + password + "\n")
        open("credentials.csv", 'a').close()
        
        return 0
    
    else:

        choice = input("Wrong input. Would you like to try again? (y/n) ::")
        if choice == 'y':
            return 1
        elif choice == 'n':
            return 2
        else:
            print("Invalid entry. Try again later.")


def new_user():
    (username, password) = sign_up()
    var_check = verify(username)
    result = 2
    if var_check != 1:
        result = user_verification(var_check, username, password)
    while result == 1 :
        print("Sending another email. Wait.......")
        var_check = verify(username)
        result = user_verification(var_check, username, password)
        

    if result == 0:
        return username , password
