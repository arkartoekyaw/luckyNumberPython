import random

print("Welcome to the game")

while True:
    choice = input("Enter your choice (1 to read rules, 2 to play game): ")
    
    if choice == "1":
        print("Age must be over 18")
        print("Show money must be more than 5000")
        print("You must bet more than or equal to 1000 each time")

    elif choice == "2":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        show_money = int(input("Enter your show money: "))
        print("Your show money is ", show_money)

        if name.strip() and age >= 18 and show_money >= 5000:
            print(f"You can play the game now, {name}")
            while True:
                bet = int(input("Enter your bet: "))
                
                if bet < 1000:
                    print("Your bet must be greater than or equal to 1000")
                    continue
                
                lucky_number = int(input("Enter your lucky number (1 to 10): "))
                system_number = random.randint(1, 10)

                if lucky_number == system_number:
                    print("The lucky number is ", system_number)
                    print("Congratulations, you win!")
                    show_money += bet
                    print(f"Your show money is {show_money}")

                else:
                    print("The lucky number is ", system_number)
                    print("Sorry, you lose.")
                    show_money -= bet
                    print(f"Your show money is {show_money}")

                if show_money < 1000:
                    print("You don't have enough money to play again.")
                    break
                
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() == "n":
                    break
                
        else:
            print("Your name length must be over 2 and age must be equal or over 18 and show money must be more than or equal to 5000.")
    else:
        print("Invalid choice. Please enter 1 to read rules or 2 to play game.")