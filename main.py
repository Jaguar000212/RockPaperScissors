import tkinter as tk
from tkinter import messagebox
import random
import json

# Create the scores file if it doesn't exist
try:
    with open('scores.json', 'r') as f:
        pass
except FileNotFoundError:
    with open('scores.json', 'w') as f:
        json.dump({'player': 0, 'computer': 0, 'tie': 0}, f)

# Function to save the scores
def save_score(winner):
    with open('scores.json', 'r') as f:
        scores = json.load(f)

    if winner == 'player':
        scores['player'] += 1
    elif winner == 'computer':
        scores['computer'] += 1
    else:
        scores['tie'] += 1

    with open('scores.json', 'w') as f:
        json.dump(scores, f)



# Function to reset the scores
def reset_scores():
    with open('scores.json', 'w') as f:
        json.dump({'player': 0, 'computer': 0, 'tie': 0}, f)
    messagebox.showinfo("Done", "Successfully reset scores.")

# Function to get the scores
def get_scores():
    with open('scores.json', 'r') as f:
        scores = json.load(f)
    score = ''
    for key, value in scores.items():
        score += f'{key.capitalize()}: {value}\n'
    score += f'\nTotal Games: {sum(scores.values())}'
    messagebox.showinfo("Scores", score)

# Function to play the game
def play_game(player_choice):
    choices = ['🪨 Rock', '🗞️ Paper', '✂️ Scissors']
    computer_choice = random.choice(choices)

    # Check who won
    if player_choice == computer_choice:
        result = "It's a tie!"
        save_score('tie')
    elif (player_choice == '🪨 Rock' and computer_choice == '✂️ Scissors') or \
         (player_choice == '📰 Paper' and computer_choice == '🪨 Rock') or \
         (player_choice == '✂️ Scissors' and computer_choice == '🗞️ Paper'):
        result = "You win! 🍾"
        save_score('player')
    else:
        result = "Computer wins! 😭\nBetter luck next time! 👍🏻"
        save_score('computer')

    # Show the result
    messagebox.showinfo("Result", f"Player: {player_choice}\nComputer: {computer_choice}\n\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.resizable(False, False)


# Create the title
title = tk.Label(window, text="Rock Paper Scissors", anchor="center")
title.configure(font=("Arial", 24))
title.grid(columnspan=3, padx=100, pady=25)

# Create the choice label
choice = tk.Label(window, text="Choose your weapon!", anchor="center")
choice.configure(font=("Arial", 18))
choice.grid(columnspan=3, padx=50, pady=10)

# Create the buttons
rock_button = tk.Button(window, text="🪨 Rock", command=lambda: play_game('🪨 Rock'))
rock_button.configure(font=("Arial", 12))
rock_button.grid(row=2, column=0, padx=10, pady=10)

paper_button = tk.Button(window, text="📰 Paper", command=lambda: play_game('📰 Paper'))
paper_button.configure(font=("Arial", 12))
paper_button.grid(row=2, column=1, padx=10, pady=10)

scissors_button = tk.Button(window, text="✂️ Scissors", command=lambda: play_game('✂️ Scissors'))
scissors_button.configure(font=("Arial", 12))
scissors_button.grid(row=2, column=2, padx=10, pady=10)

# Create the menu
menu = tk.Menu(window)
window.config(menu=menu)

# Create the menu items
menu_item = tk.Menu(window)
menu_item.add_command(label='See Scores', command=get_scores)
menu_item.add_command(label='Reset Scores', command=reset_scores)
menu_item.add_command(label='Exit', command=window.quit)
menu.add_cascade(label='Menu', menu=menu_item)
help_item = tk.Menu(window)
help_item.add_command(label='Help', command=lambda: messagebox.showinfo("Help", "Choose your weapon and see if you can beat the computer!"))
help_item.add_command(label='About', command=lambda: messagebox.showinfo("About", "This game was created by @jaguar000212."))
menu.add_cascade(label='More', menu=help_item)

# Create the footer
footer = tk.Label(window, text="Made by @jaguar000212\n♥️♥️♥️", anchor="center")
footer.configure(font=("Arial", 10, "bold",), fg="red", cursor="hand2", pady=10, padx=10)
footer.grid(columnspan=3, padx=100, pady=25)

# Start the main loop
window.mainloop()
