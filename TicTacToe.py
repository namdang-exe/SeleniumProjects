"""
This is tic tac toe game
This is what the board looks like

 | |
-+-+-
 | |
-+-+-
 | |

"""
the_board = {
    "top-L": 'O', 'top-M': 'O', 'top-R': 'O',
    'mid-L': 'X', 'mid-M': 'X', 'mid-R': '',
    'bot-L': '', 'bot-M': '', 'bot-R': 'X'
}


def fill_board(board):
    for k in board.keys():
        if not board.get(k):
            board[k] = " "


def print_board(board):
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print("-+-+-")
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print("-+-+-")
    print(f"{board['bot-L']}|{board['bot-M']}|{board['bot-R']}")


fill_board(the_board)
print_board(the_board)
