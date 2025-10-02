import random

def ssrp_game():
    print("WELCOME TO GALAXY KABOOOMMMM !!!\nBy Dhruv Chavan")
    print("*"*30)
    print("Rules: Avoid the asteroids by moving Left (a), Center (s), or Right (d)\nPress the right key before the asteroid hits you!!!!!")
    challenge = 10
    print (f"A small challenge... collect {challenge} stars.")
    print("⭐"*challenge)
    

    lanes = ["Left", "Center", "Right"]
    position = "Center" 
    score = 0
    target_score = 10

    while True:
        asteroid = random.choice(lanes) 
        print ("-"*30)
        print(f"Your spaceship is currently in {position} lane.")

        move = input("Move (a=Left, s=Center, d=Right): ").lower()

        if move == 'a':
            position = "Left"
        elif move == 's':
            position = "Center"
        elif move == 'd':
            position = "Right"
        else:
            print("Invalid move!! Your spaceship will stay in current lane.")

        if position == asteroid:
            print("\n*********** OHH NOOOOOO!!! The asteroid hit your spaceship. Game Over! :( ************")
            print(f"\nYour Final Score is: {score}")
            print ("⭐"*score)
            if target_score <= score:
                print("\nCongratsss you have completed the challenge given!!!!")
            else:
                print("\nTry again to complete the given challenge of scoring 10 points :)")
            break
        else:
            print("\n********** Yayyy you're safe! You dodged the asteroid.***********")
            score += 1 
            print(f"\nYour current score is: {score}")
            print ("⭐"*score)
if __name__ == "__main__":
     while True:
        ssrp_game()
        try_again = input("Say yes if you want to play again: ").lower()
        if try_again != "yes":
            print("Thanks for playing my game :)")
            break
