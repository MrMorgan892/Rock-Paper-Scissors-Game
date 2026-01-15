import tkinter as tk, random
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("700x600")
window.resizable(False, False)
winner = "who"
bots_choise = "choose"
words = ["paper", "scissor", "rock"]
Round = 1
bot_wins = 0
player_wins = 0
score = f"Player: {player_wins} | Bot: {bot_wins}"
Rounds_chosen = {"value": 0}
game_winner = "You haven't played yet!"

def game_winner_update():
    global player_wins, bot_wins, game_winner
    if player_wins > bot_wins:
        game_winner = "🏆PLAYER WINS🏆"
        return game_winner
    elif bot_wins > player_wins:
        game_winner = "🤖BOT WINS🤖"
        return game_winner
    elif player_wins == bot_wins:
        game_winner = "🤝DRAW!🤝"
        return game_winner
    return None


def rounds_check():
    global Rounds_chosen
    Rounds_chosen["value"] -= 1
    if Rounds_chosen["value"] == 0:
        setup()
    else:
        print("continue")

def game():
    global Rounds_chosen
    move_choose_label.pack()
    score_label.pack()
    Round_label.pack()
    paper_button.place(x=500, y=150)
    scissors_button.place(x=100, y=150)
    bot_choise_label.place(x=250, y=250)
    rock_button.place(x=300, y=150)
    bot_choise_text.place(x=250, y=300)
    round_won_label.place(x=220, y=350)
    winner_label.place(x=260, y=400)
    Rounds_num.pack_forget()
    ten_rounds.place_forget()
    fifteen_rounds.place_forget()
    five_rounds.place_forget()
    game_winner_label.place_forget()
    game_winner_text.place_forget()


Rounds_num = tk.Label(window, text="How many rounds do you want?", font=("Arial", 30))

five_rounds = tk.Button(window, text="5", command=lambda: [Rounds_chosen.update({"value": 5}), game()], width=7, height=3, font=("Arial", 20))
ten_rounds = tk.Button(window, text="10", command=lambda: [Rounds_chosen.update({"value": 10}), game()], width=7, height=3, font=("Arial", 20))
fifteen_rounds = tk.Button(window, text="15", command=lambda: [Rounds_chosen.update({"value": 15}), game()], width=7, height=3, font=("Arial", 20))


def update_score_display():
    global score, bot_wins, player_wins
    score_label.config(text=f"Player: {player_wins} | Bot: {bot_wins}")

def update_game_winner_display():
    global game_winner,game_winner_text
    game_winner_text.config(text=game_winner)

def update_round_display():
    Round_label.config(text=f"ROUND:{Round}")

def rock_move():
    global winner, bots_choise, words, Round, player_wins, bot_wins
    bots_choise = random.choice(words)
    print("rock")
    if bots_choise == "rock":
        winner = "A draw!🤝"
    elif bots_choise == "paper":
        winner = "Bot🤖"
        bot_wins += 1
    elif bots_choise == "scissor":
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
    if bots_choise == "rock":
        winner = "Player🏆"
        player_wins += 1
    elif bots_choise == "paper":
        winner = "A draw!🤝"
    elif bots_choise == "scissor":
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
    if bots_choise == "rock":
        winner = "Bot🤖"
        bot_wins += 1
    elif bots_choise == "paper":
        winner = "Player🏆"
        player_wins += 1
    elif bots_choise == "scissor":
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

move_choose_label = tk.Label(window, text="Choose your move:", font=("Arial", 20))
move_choose_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: [rock_move(), rounds_check()], width=6, height=2, font=("Arial", 20))
rock_button.place(x=300, y=150)

paper_button = tk.Button(window, text="Paper", command=lambda: [paper_move(), rounds_check()], width=6, height=2, font=("Arial", 20))
paper_button.place(x=500, y=150)

scissors_button = tk.Button(window, text="Scissors", command=lambda: [scissors_move(), rounds_check()], width=6, height=2, font=("Arial", 20))
scissors_button.place(x=100, y=150)

bot_choise_label = tk.Label(window, text="Bot's choice:", font=("Arial", 20))
bot_choise_label.place(x=250, y=250)

bot_choise_text = tk.Label(window, text="", font=("Arial", 20))
bot_choise_text.place(x=250, y=300)

round_won_label = tk.Label(window, text="ROUND WINNER:", font=("Arial", 20))
round_won_label.place(x=220, y=350)

winner_label = tk.Label(window, text="", font=("Arial", 20))
winner_label.place(x=260, y=400)

game_winner_label = tk.Label(window, text="🏆THE WINNER OF THE GAME:", font=("Arial", 20))
game_winner_text = tk.Label(window, text=game_winner, font=("Arial", 30))


def setup():
    global Round, Rounds_chosen, bot_wins, player_wins
    game_winner_update()
    update_game_winner_display()
    Round = 1
    bot_wins = 0
    player_wins = 0
    update_round_display()
    update_score_display()
    move_choose_label.pack_forget()
    score_label.pack_forget()
    Round_label.pack_forget()
    paper_button.place_forget()
    scissors_button.place_forget()
    bot_choise_label.place_forget()
    rock_button.place_forget()
    bot_choise_text.place_forget()
    round_won_label.place_forget()
    winner_label.place_forget()
    Rounds_num.pack()
    game_winner_label.place(x=160, y=300)
    game_winner_text.place(x=200, y=380)
    ten_rounds.place(x=300, y=150)
    fifteen_rounds.place(x=500, y=150)
    five_rounds.place(x=100, y=150)

setup()





window.mainloop()