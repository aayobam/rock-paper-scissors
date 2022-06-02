import random


def user_response():
    
    response = input("Do you wish to play on? type Y for YES or N for NO: ").capitalize()

    if response == "Y":
        start_game()

    elif response == "N":
        print(f"{'*' * 20}Thanks for playing, Good Bye.{'*' * 20}")
        exit()
    else:
        print("Invalid value supplied, please try again")
        user_response()
        

def start_game():
    option_list = ['R', 'P', 'S']
    cpu_input = random.choice(option_list)
   
    print(f"{'*' * 20}WELCOME TO ROCK PAPER SCISSORS GAME APP{'*' * 20}")

    user_input = input("Type any of the following options: R, P or S to play: ").capitalize()
   
    if user_input == cpu_input:
        print(F"CPU selected: {cpu_input}\nYou selected: {user_input}\nRESULT: it's a TIE.")
        user_response()
    
    elif user_input == 'R' and cpu_input == 'S':
        print(F"CPU selected: {cpu_input}\nYou selected: {user_input}\nRESULT: You WIN.")
        user_response()
    
    elif user_input == 'S' and cpu_input == 'P':
        print(F"CPU selected: {cpu_input}\nYou selected: {user_input}\nRESULT: You WIN.")
        user_response()

    elif user_input == 'P' and cpu_input == 'R':
        print(F"CPU selected: {cpu_input}\nYou selected: {user_input}\nRESULT: You WIN.")
        user_response()

    elif user_input == 'S' and cpu_input == 'R':
        print(F"CPU selected: {cpu_input}\nYou selected: {user_input}\nRESULT: CPU WINs.")
        user_response()

    elif user_input == 'P' and cpu_input == 'S':
        print(F"CPU selected: {cpu_input}\nYou selected: {user_input}\nRESULT: CPU WINs.")
        user_response()

    elif user_input == 'R' and cpu_input == 'P':
        print(F"CPU selected: {cpu_input}\nYou selected: {user_input}\nRESULT: CPU WINs.")
        user_response()
    
    else:
        print("Error input, please try again")
        start_game()
start_game()