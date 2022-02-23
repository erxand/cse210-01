"""
File: tic_tac_toe_feb23.py
Author: Xander Hunt
Purpose: Create a game of tic-tac-toe to prove knowledge of Python fundamentals and understanding of git and github
"""


def main():
    game_board = {}
    for id in range(1, 10):
        game_board[id] = [id, "None"]
    
    counter = 0
    draw_board(game_board)
    game_not_finished = True
    while game_not_finished:
        counter += 1
        if counter > 9:
            print("That's a draw folks. Feel free to play again!")
            break
        try:
            if (counter % 2) != 0:
                response = int(input("X's turn to choose a square (1-9): "))
                if game_board[response] == [response, "None"]:
                    game_board[response] = [response, "X"]
                else:
                    print("That spot is already taken bucko. Try again.")
                    counter -= 1
            else:
                response = int(input("O's turn to choose a square (1-9):"))
                if game_board[response] == [response, "None"]:
                    game_board[response] = [response, "O"]
                else:
                    print("That spot is already taken bucko. Try again.")
                    counter -= 1
        except:
            print("That input wasn't very cash money of you. Try again.")
            counter -= 1
        
        draw_board(game_board)
        
        if check_win(game_board) == "X":
            print("Player #1 won, congrats!")
            break
        elif check_win(game_board) == "O":
            print("Player #2 won, congrats!")
            break


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


def check_win(game_board):
    for i in range(2):
        if i == 0:
            token = "X"
        else:
            token = "O"

        if (game_board[1][1] == token) and (game_board[2][1] == token) and (game_board[3][1] == token):
            return token
        elif (game_board[4][1] == token) and (game_board[5][1] == token) and (game_board[6][1] == token):
            return token
        elif (game_board[7][1] == token) and (game_board[8][1] == token) and (game_board[9][1] == token):
            return token
        elif (game_board[1][1] == token) and (game_board[4][1] == token) and (game_board[7][1] == token):
            return token
        elif (game_board[2][1] == token) and (game_board[5][1] == token) and (game_board[8][1] == token):
            return token
        elif (game_board[3][1] == token) and (game_board[6][1] == token) and (game_board[9][1] == token):
            return token
        elif (game_board[1][1] == token) and (game_board[5][1] == token) and (game_board[9][1] == token):
            return token
        elif (game_board[3][1] == token) and (game_board[5][1] == token) and (game_board[7][1] == token):
            return token

    return "None"


if __name__ == "__main__":
    main()