
def save(username):
    vehicle_model = input("Please enter the device model:")
    vehicle_number = input("Please enter the vehicle number:")
    
    open("Vehicle.csv",'a').write(username + "," + vehicle_model + "," + vehicle_number + "\n")


def payment_info(username):
    card_name = input("Please enter the name on the card:")
    card_number = input("Please enter the Card number:")
    expiry = input("Please enter the expiry month: mm/yy")
    ccv = input("Please enter the CCV:")
    
    file_name = "pay" + username + ".txt"
    
    open(file_name, "w").write(card_name + "," + card_number + "," + expiry + "," + ccv)
    #then encryt the file

def rider():
    choice = input("(s)Scan QR code\t(v)Vehicle Info\t(p)Save payment info")
    if choice == 's':
        #qr_scanner.py
    if choice == 'v':
        #


def choose_mode():
    #username = collect from the log_in module
    choice = input("Choose mode.\n(h)Host\t(r)Rider")
    try:
        if choice == 'h':
            print("Host mode activated.")
        elif choice == 'r':
            print("Rider mode activated.")
        else:
            raise ValueError
    
    except:
        print("Invalid input. Try again.")
        