def cs_service_bot():
    print("""Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer? \n [1] New Customer \n [2] Existing Customer""")
    response = input("Please enter the number corresponding to your choice:")
    if response == "1":
        new_customer()
        return
    elif response == "2":
        existing_customer()
        return
    else:
        print("Sorry, we didn't understand your selection.")
        cs_service_bot()
        return

def existing_customer():
    print("""What kind of support do you need? \n [1] Television Support \n [2] Internet Support \n [3]Speak to a support representative.""")
    response = input("Please enter the number corresponding to your choice:")
    if response == "1":
        return television_support()
    if response == "2":
        return internet_support()
    if response == "3":
        return live_rep("support")
    else:
        print("Sorry, we didn't understand your selection")
        return existing_customer()

def new_customer():
    print("""[1] Sign up for service. \n [2] Schedule a home visit. \n [3] Speak to a sales representative.""")
    response = input("We are excited to have you join the DNS family, how can we help you?")
    
    if response == "1":
        return sign_up()
    if response == "2":
        return home_visit()
    if response == "3":
        return live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection")
        return new_customer()

def television_support():
    print(""" [1] I can't access certain channels. \n [2] My picture is blurry. \n [3] I keep losing service. \n [4] Other issues.""")
    
    response = input("What is the nature of your problem?")
    
    if response == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        return did_that_help()
    
    if response == "2":
        print("Try adjusting the antenna above your television set.")
        return did_that_help()
    
    if response == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        return did_that_help()
    
    if response == "4":
        return live_rep("support")
    
    else:
        print("Sorry, we didn't understand your selection")
        return television_support()

def internet_support():
    print(""" [1] I can't connect to the internet. \n [2] My connection is very slow. \n [3] I can't access certain sites. \n [4] Other issues.""")
    
    response = input("What is the nature of your problem?")
    
    if response == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        return did_that_help()
    
    if response == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.")
        return did_that_help()
    
    if response == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        return did_that_help()
    
    if response == "4":
        return live_rep("support")
    
    else:
        print("Sorry, we didn't understand your selection")
        return internet_support()
   

def did_that_help():
    response1= input("Did it solve the problem? Y/N: ")
    
    if response1 == "Y" or "y":
        return print("Thank you")

    elif response1 == "N" or "n":
        response2 = input("Do you want to \n [1] Talk to representative \n [2] Schedule a home visit")
        if response2 == "1":
            return live_rep("support")
        if  response2 == "2":
            return home_visit("support")
        else:
            print("Sorry, we didn't understand your selection")
            return did_that_help()
    else:
        print("Sorry, we didn't understand your selection")
        return did_that_help()


def sign_up():
    print(""" Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for. \n [1] Bundle Deal (Internet + Cable) \n [2] Internet \n [3] Cable""")
    
    response == input("What is the nature of your problem?")
    
    if response == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        return home_visit("new_install")
    
    elif response == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        return home_visit("new_install")
    
    elif response == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        return home_visit("new_install")
    
    else:
        print("Sorry, we didn't understand your selection")
        return sign_up()


def home_visit(purpose = "none"):
    if purposes == "none":
        print("What is the purpose of your home visit:")    
        print("[1] New service installation.")
        print("[2] Existing service repair.")
        print("[3] Location scouting for unservices region.")
    
        response == input("What is the nature of your problem?")
    
        if response == "1":
            return home_visit("new_install")
        elif response == "2":
            return home_visit("support")
        elif response == "3":
            return home_visit("scout")
        else:
            visit_date == input("Please enter the date below when you are available for a technician to come your home and fix the issue.")
            print(" Wonderful! A technical will come visi you on " + str(visit_date) + ". Please be available between the hours of 1:00 am and 11:00 pm")
            return visit_date


def live_rep(purpose):
    if purpose == "sales":
        return print(" Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    if purpose == "support":
        return print("  Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")


print(cs_service_bot())

        