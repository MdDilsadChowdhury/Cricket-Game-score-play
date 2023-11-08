import random

def play_cricket():
    runs = 0
    wickets = 0
    overs = 0
    target_runs = random.randint(150, 250)
    
    while overs < 10 and wickets < 10:
        # Simulate a ball
        ball = random.randint(0, 6)
        player_shot = int(input("Enter your shot (0-6): "))
        
        if ball == player_shot:
            print("Out!")
            wickets += 1
        else:
            print(f"Runs scored: {ball}")
            runs += ball
        
        print(f"Score: {runs}/{wickets} ({overs} overs)")
        overs += 0.1

    if runs >= target_runs:
        print("Congratulations! You won!")
    else:
        print("You lost. Try again.")

if __name__ == "__main__":
    print("Welcome to ICC Cricket World Cup")
    play_cricket()
