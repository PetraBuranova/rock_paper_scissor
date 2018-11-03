import random

def input_human_play(input=input):
    play = input("rock, paper, or scissors?")
    while not is_valid_play(play):
        play = input("rock, paper, or scissors?")
    return play

def is_valid_play(play):
    return play in ["rock", "paper", "scissor"]

def generate_computer_play():
    return random.choice(["rock", "paper","scissor"])

def evaluate_game(human, computer):
    if human == computer:
        return "tie"
    elif human == "rock":
        if computer == "paper":
            return "computer"
        elif computer == "scissor":
            return "human"
    elif human == "paper":
        if computer == "rock":
            return "human"
        elif computer == "scissor":
            return "computer"
    elif human == "scissor":
        if computer == "paper":
            return "human"
        elif computer == "rock":
            return "computer"



def main(input=input):
    human = input_human_play(input)
    computer = generate_computer_play()

    print(computer)
    game = evaluate_game(human, computer)
    if game == "tie":
        print("it's a tie")
    else:
        print(f'{game} won')


if __name__ == "__main__":
    main()