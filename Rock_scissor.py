import random

def game():
        num_play = int(input("chose the number of attempts: "))

        num_init = 1
        while num_init != 0:
            choices = ["Stone","Paper", "Scissor"]
            rand_choice = random.choice(choices)
            user_choice = input("Enter your Choice: ").capitalize()
            print(f"Your Choice: {user_choice}")
            print(f"Computer's Choice: {rand_choice}")

            if user_choice == rand_choice:
                print(f"Tied!! Attempts left :{num_init}")

            elif (user_choice == "Stone" and rand_choice == "Scissor") or (user_choice == "Scissor" and rand_choice == "Paper") or (user_choice == "Paper" and rand_choice == "Stone"):
                print(f"You Win, Attempts left: {num_play}")

            elif (user_choice == "Paper" and rand_choice == "Scissor") or (user_choice == "Scissor" and rand_choice == "Stone") or (user_choice == "Stone" and rand_choice == "Paper"):
                print(f"You Lost, Attempts left: {num_play-1}")

            else:
                print("Enter a valid choice")
            num_play -= num_init

            if num_play == 0:
                break
                print("You attempts have been ran out, Please Try Again.")

        print("Attemtps Over\n Thanks for Playing")
game()
