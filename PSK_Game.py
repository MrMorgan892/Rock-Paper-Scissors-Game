# Rock Paper Scissors game with UI(Tkinter)
# Author on GitHub: MrMorgan892
# Day 6 of learning python


import tkinter as tk, random
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("700x600")
window.resizable(False, False)
winner = "who"
bots_choise = "choose"
words = ["paper📄", "scissor✂️", "rock🪨"]
Round = 1
bot_wins = 0
player_wins = 0
score = f"Player: {player_wins} | Bot: {bot_wins}"

def update_score_display():
    global score, bot_wins, player_wins
    score_label.config(text=f"Player: {player_wins} | Bot: {bot_wins}")

def update_round_display():
    Round_label.config(text=f"ROUND:{Round}")

def rock_move():
    global winner, bots_choise, words, Round, player_wins, bot_wins
    bots_choise = random.choice(words)
    print("rock")
    if bots_choise == "rock🪨":
        winner = "A draw!🤝"
    elif bots_choise == "paper📄":
        winner = "Bot🤖"
        bot_wins += 1
    elif bots_choise == "scissor✂️":
        winner = "Player🏆"
        player_wins += 1
    winner_label.config(text=winner)
    bot_choise_text.config(text=bots_choise)
    Round += 1
    update_round_display()
    update_score_display()

def paper_move():
    print("paper")
    global winner, bots_choise, words, Round, player_wins, bot_wins
    bots_choise = random.choice(words)
    if bots_choise == "rock🪨":
        winner = "Player🏆"
        player_wins += 1
    elif bots_choise == "paper📄":
        winner = "A draw!🤝"
    elif bots_choise == "scissor✂️":
        winner = "Bot🤖"
        bot_wins += 1
    winner_label.config(text=winner)
    bot_choise_text.config(text=bots_choise)
    Round += 1
    update_round_display()
    update_score_display()

def scissors_move():
    print("scissors")
    global winner, bots_choise, words, Round, player_wins, bot_wins
    bots_choise = random.choice(words)
    if bots_choise == "rock🪨":
        winner = "Bot🤖"
        bot_wins += 1
    elif bots_choise == "paper📄":
        winner = "Player🏆"
        player_wins += 1
    elif bots_choise == "scissor✂️":
        winner = "A draw!🤝"
    winner_label.config(text=winner)
    bot_choise_text.config(text=bots_choise)
    Round += 1
    update_round_display()
    update_score_display()

Round_label = tk.Label(window, text=f"ROUND:{Round}", font=("Arial", 20))
Round_label.pack()

score_label = tk.Label(window, text="Score:", font=("Arial", 20))
score_label.pack()

label = tk.Label(window, text="Choose your move:", font=("Arial", 20))
label.pack()

rock_button = tk.Button(window, text="Rock🪨", command=lambda: rock_move(), width=6, height=2, font=("Arial", 20))
rock_button.place(x=300, y=150)

paper_button = tk.Button(window, text="Paper📄", command=lambda: paper_move(), width=6, height=2, font=("Arial", 20))
paper_button.place(x=500, y=150)

scissors_button = tk.Button(window, text="Scissors✂️", command=lambda: scissors_move(), width= 10, height=2, font=("Arial", 20))
scissors_button.place(x=100, y=150)

bot_choise_label = tk.Label(window, text="Bot's choice:", font=("Arial", 20))
bot_choise_label.place(x=250, y=250)

bot_choise_text = tk.Label(window, text="", font=("Arial", 20))
bot_choise_text.place(x=250, y=300)

round_won_label = tk.Label(window, text="ROUND WINNER:", font=("Arial", 20))
round_won_label.place(x=220, y=350)

winner_label = tk.Label(window, text="", font=("Arial", 20))
winner_label.place(x=260, y=400)

window.mainloop()