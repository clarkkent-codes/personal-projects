board = []
rows, cols = 3, 3

def creating_board():
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(' ')
        board.append(col)

def print_board():
    print("Tic-Tac-Toe")
    for i in range(3):
        row = []
        for cell in board[i]:
            if cell == 1:
                row.append('X')
            elif cell == 2:
                row.append('O')
            else:
                row.append(' ')
        print(" | ".join(row))
        if i != 2:
            print("--+---+--")


def make_a_move(player):
    while True:
        try:
            row = int(input("Enter a row: "))
            col = int(input("Enter a column: "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Try again.")
                continue
            elif board[row][col] != ' ':
                print("Already taken. Try again")
                continue
            board[row][col] = player
            break
        except ValueError:
                    print("Please enter a valid number.")

creating_board()
print_board()
make_a_move(1)
print_board()
make_a_move(2)
print_board()