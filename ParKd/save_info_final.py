def vehicle_info(username):
    registration = input("Please enter your vehicle registration number:")
    open("Vehicle.csv",'a').write(username + "," + registration + "\n")
    open("Vehicle.csv",'r').close()
    print("Vehicle info saved.")

def payment_info(username):
    card_name = input("Please enter the name on the card:")
    card_number = input("Please enter the Card number:")
    expiry = input("Please enter the expiry month: mm/yy:")
    ccv = input("Please enter the CCV:")
    
    open("pay_info.csv", "a").write(username + "," + card_name + "," + card_number + "," + expiry + "," + ccv + "\n")
    open("pay_info.csv", "r").close()
    print("Payment info saved.")



def host_rating(username):
    rating = 0
    rating_param = input("Do you have a ParKd verified or any security camera? #2 points (y/n)::")
    if rating_param == 'y':
        rating += 2

    rating_param = input("Is your spot available minimum 4 hours a day or 20 hours a week? #1 point (y/n)::")
    if rating_param == 'y':
        rating += 1

    rating_param = input("Is your parking spot an off-road parking? #1 point (y/n)::")
    if rating_param == 'y':
        rating += 1

    rating_param = input("Do you live in or within 5km of the CBD? #1 point (y/n)::")
    if rating_param == 'y':
        rating += 1

    print("Your current rating is ", rating)
    open("host_rating.csv", 'a').write(username + "," + str(rating) + "\n")
    open("host_rating.csv", 'a').close()



def choose_mode():
    username = input("Please enter the user name:")
    choice = input("Choose mode.\n(h)Host\t\t(r)Rider\n::")
    try:
        if choice == 'h':
            print("Host mode activated.")
            host_rating(username)
        elif choice == 'r':
            print("Rider mode activated.")
            choice_v2 = input("Options: (s)Save payment Info\t(v)Save vehicle info\n::")
            if choice_v2 == 's':
                payment_info(username)
            elif choice_v2 == 'v':
                vehicle_info(username)
            else:
                print("Invalid input. Try again.")
                choose_mode()
        else:
            raise ValueError
    
    except:
        print("Invalid input. Try again.")

choose_mode()
print("Press Enter to close")
import msvcrt as m
m.getch()
        
