import random

player = 0
computer = 0
user_inputs = []
abbreviations = {
    "p":"Paper",
    "r":"Rock",
    "s":"Scissors"
}

def predict():
    rock = user_inputs.count("r")
    paper = user_inputs.count("p")
    scissors = user_inputs.count("s")
    if (rock > paper) and (rock > scissors) : return "p"
    if (paper > rock) and (paper > scissors): return "s"
    if(scissors > rock) and (scissors > paper): return "r"

    return random.choice(["r","p","s"])

def display_score(user, prediction):
    global player
    global computer
    possible_win_situations = {
        "p":"r",
        "r":"s",
        "s":"p"
    }
    user = user.lower()

    if user == prediction: return f"Draw.\nYour Score: {player}\nComputer Score: {computer}"

    for situation in possible_win_situations:
        if(user == situation) and (prediction == possible_win_situations[situation]):
            player += 1 
            return f"Your point.\nYour Score: {player}\nComputer Score: {computer}"

        if (user==possible_win_situations[situation]) and (prediction==situation):
            computer += 1
            return f"Computer's point.\nYour Score: {player}\nComputer Score: {computer}"
            

def main():
    while True:
        possible_answers = ["r","p","s"]
        user_input = input('Use "r" for rock\n"p" for paper\n"s" for scissors: ')
        prediction = predict()
        outcome = display_score(user_input, prediction)

        while user_input not in possible_answers:
            print("Invalid input")
            user_input = input("What do you choose?: ")
            outcome = display_score(user_input, prediction)
           
        print(f"\nComputer chooses {abbreviations[prediction]}\n")
        print(outcome)
        user_inputs.append(user_input)

        if(player==10):
            print("You won")
            break
        elif(computer==10):
            print("Computer won")
            break

main()