#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: HW17

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

def rps_choice():
    global option
    print("say which one you choose:")
    print("1 for rock")
    print("2 for paper")
    print("3 for scissors")
    ask = int(input("pick here: "))
    if ask == 1:
        option = "rock"
    elif ask == 2:
        option = "paper"
    elif ask == 3:
        option = "scissors"
    else:
        rps_choice()

    confirm = input(f"is your choice {str(option)}? ")
    confirm = confirm.lower()
    if (confirm == "yes" or confirm == "y"
            or confirm == "yeah" or confirm == "yup" or confirm == "mhm"
            or confirm == "sure" or confirm == "maybe" or confirm == "ok"
            or confirm == "alright" or confirm == "right"
            or confirm == "you got it" or confirm == "you betcha"
            or confirm == "bet" or confirm == "you bet"
    #heck variants (very important)
            or confirm == "heck yeah" or confirm == "heck yup" or confirm == "heck mhm"
            or confirm == "heck sure" or confirm == "heck maybe" or confirm == "heck ok"
            or confirm == "heck alright" or confirm == "heck right"
            or confirm == "heck you got it" or confirm == "heck you betcha"
            or confirm == "heck bet" or confirm == "heck you bet"
    ):
        rps_enemy()
    else:
        rps_choice()

rps_choice()

def rps_enemy():
#enemy set up