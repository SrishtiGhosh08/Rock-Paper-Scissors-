import random

print("Welcome to Rock Paper Scissors Game")

choices = ["rock", "paper", "scissor"]

while True:
    print("\nMenu:")
    print("1. Play Game")
    print("2. Exit")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        user_score = 0
        comp_score = 0

        for round_no in range(1, 6):
            print(f"\n--- Round {round_no} ---")
            print("1. Rock\n2. Paper\n3. Scissor")
            user_input = input("Choose (1/2/3): ")

            if user_input == "1":
                user_choice = "rock"
            elif user_input == "2":
                user_choice = "paper"
            elif user_input == "3":
                user_choice = "scissor"
            else:
                print("Invalid input! Skipping this round.")
                continue

            comp_choice = random.choice(choices)

            print("You chose     :", user_choice)
            print("Computer chose:", comp_choice)

            if user_choice == comp_choice:
                print("Result: Draw")
            elif (user_choice == "rock" and comp_choice == "scissor") or \
                 (user_choice == "paper" and comp_choice == "rock") or \
                 (user_choice == "scissor" and comp_choice == "paper"):
                print("Result: You Win")
                user_score += 1
            else:
                print("Result: Computer Wins")
                comp_score += 1

        # Final result
        print("\n===== Final Result =====")
        print("Your Score     :", user_score)
        print("Computer Score :", comp_score)

        if user_score > comp_score:
            print("You Won the Game!")
        elif user_score < comp_score:
            print("Computer Won the Game!")
        else:
            print("It's a Draw!")

    elif choice == "2":
        print("Thanks for playing. Goodbye")
        break
    else:
        print("Invalid selection. Try again!")
