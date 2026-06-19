import random 
from llama import bot_ai

win = ("abc", "def", "ghi", "adg", "beh", "cfi", "aei", "ceg")
grid = list("abcdefghi")
a = b = c = d = e = f = g = h = i = " "
name = input("Enter your name : ")
def game(change, who):
    global a, b, c, d, e, f, g, h, i 
    if change in "abcdefghi":
        if change == "a": 
            a = "X" if who else "O"
        elif change == "b": 
            b = "X" if who else "O"
        elif change == "c": 
            c = "X" if who else "O"
        elif change == "d": 
            d = "X" if who else "O"
        elif change == "e": 
            e = "X" if who else "O"
        elif change == "f": 
            f= "X" if who else "O"
        elif change == "g": 
            g = "X" if who else "O"
        elif change == "h": 
            h = "X" if who else "O"
        elif change == "i": 
            i = "X" if who else "O"
        print(f"{name} played {change}" if who else f"Bot played {change}")
    else:
        print("Invalid Input")

    print(f"\n  {a} | {b} | {c} \n ___ ___ ___\n\n  {d} | {e} | {f} \n ___ ___ ___ \n\n  {g} | {h} | {i}\n")


def check_win(player):
    return any( all(c in player for c in combi) for combi in win)



# def bot_():
#     return random.choice(grid)




def start():

    print("\nThis is the grid for Tictactoe : ")
    print(f"\n\n  a | b | c \n ___ ___ ___\n\n  d | e | f \n ___ ___ ___ \n\n  g | h | i\n\n")

    print(f"\n  {a} | {b} | {c} \n ___ ___ ___\n\n  {d} | {e} | {f} \n ___ ___ ___ \n\n  {g} | {h} | {i}\n")

    player =""
    bot = ""
    while True:
        while True: 
            player_choice = input("\nEnter : ").lower()
            if player_choice in grid:
                player += player_choice
                grid.remove(player_choice)
                game(player_choice,True)
                break
            else : 
                print("Try again")
        if check_win(player=player): 
            print(name," Win .")
            break

        bot_choice = bot_ai(f"\n  {a} | {b} | {c} \n ___ ___ ___\n\n  {d} | {e} | {f} \n ___ ___ ___ \n\n  {g} | {h} | {i}\n")
        print(f"\n  {a} | {b} | {c} \n ___ ___ ___\n\n  {d} | {e} | {f} \n ___ ___ ___ \n\n  {g} | {h} | {i}\n")
        print(bot_choice)
        bot += bot_choice
        grid.remove(bot_choice)
        game(bot_choice,False)
        if check_win(bot):
            print("Bot Wins")
            break

start()