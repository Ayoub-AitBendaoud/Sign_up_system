import time
def sign_up():
    #intialize an empty dict to store user info
    user_data = {}
    print("welcome to the simple sign up page of ayoub aitbendaoud")
    print("wait 5..4..3..2..1")
    for _ in range(5):
        print(".", end="")
        time.sleep(1)
    print()
 #my_linkedin : @ayoub_aitbendaoud
    user_data["name"]=input("enter your name:")
    user_data["email"]=input("enter your email address:")
    user_data["password"]=input("create a password:")
    user_data["phone"]=input("type your phone number:")
    user_data["age"]=input("enter your age:")
    user_data["gender"]=input("choose your gender (Female or Male:)").strip().lower()
    
    if user_data["gender"] == "female":
        print("you chose female")
    elif user_data["gender"] == "male":
        print("you chose male")
    else:
        print("invalid input. please choose between Female and Male")
    #my_linkedin : @ayoub_aitbendaoud
    confirmation = input("Is the above information correct?! (yes/no)").strip().lower()
    print("in progress 5..4..3..2..1")
    for _ in range(5):
        print(".", end="")
        time.sleep(1)
    print()
    if confirmation != "yes":
        print("please re-enter you information!")
        sign_up() # for restaring the sign up process if the info isn't correct
    else:
        print("\nThank you for signing up!! your account has been created.")
# Youtube and github: @Ayoub_aitbendaoud
    print("\nPlease review your information")
    print(f"Name:{user_data['name']}")
    print(f"Email:{user_data['email']}")
    print("password:**** (for Security reasons)")
    print(f"Phone Number:{user_data['phone']}")
    print(f"Gender:{user_data['gender'].capitalize()}")
    print(f"Age:{user_data["age"]}")

if __name__ == "__main__":
    sign_up()