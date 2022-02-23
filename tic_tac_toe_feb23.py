"""
File: tic_tac_toe_feb23.py
Author: Xander Hunt
Purpose: Create a game of tic-tac-toe to prove knowledge of Python fundamentals and understanding of git and github
"""

from re import template


def main():
    game_board = {}
    for id in range(1, 10):
        game_board[id] = [id, "None"]
    
    counter = 0
    
    game_not_finished = True
    while game_not_finished:
        counter += 1
        draw_board(game_board)
        if (counter % 2) != 0:
            response = int(input("X's turn to choose a square (1-9): "))
            # put in the changing board here
        else:
            response = int(input("O's turn to choose a square (1-9):"))
        
        


def draw_board(game_board):
    list = []
    for id in game_board:
        temp_list = game_board[id]
        if temp_list[1] == "None":
            list.append(id)
        else:
            list.append(temp_list[1])
    print(f"""
{list[0]} | {list[1]} | {list[2]}
--+---+--
{list[3]} | {list[4]} | {list[5]}
--+---+--
{list[6]} | {list[7]} | {list[8]}""")

if __name__ == "__main__":
    main()