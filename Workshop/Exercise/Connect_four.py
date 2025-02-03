PLAYER_MOVE = 0
CURRENT_MOVE = 0


def make_matrix():
    """Create a 6x7 board with all spaces initialized to '0'."""
    matrix = []

    for i in range(6):
        matrix.append([])
        for j in range(7):
            matrix[i].append("0")
    for row in matrix:
        print(f"[ {', '.join(row)} ]")

    return matrix


def move(player_char: str, matrix: list):
    """Move the player's piece into the selected column."""
    global PLAYER_MOVE, CURRENT_MOVE
    while True:
        PLAYER_MOVE = int(input(f"Player {player_char} makes a move (1-7): ")) - 1
        col = PLAYER_MOVE
        if matrix[0][col] != "0":
            print("Row is full, please select another row")
        else:
            break
    for row in range(5, -1, -1):
        if matrix[row][col] == "0":
            matrix[row][col] = player_char
            CURRENT_MOVE += 1
            print_matrix(matrix)

            return matrix


def print_matrix(matrix: list):
    """Print the board with current moves made."""
    for row in matrix:
        print(f"[ {', '.join(row)} ]")


def check_for_match(player: str, matrix: list):
    """Check if a player has won by forming a line of 4 symbols (horizontal, vertical, diagonal)."""
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols - 3):
            if matrix[row][col] == matrix[row][col + 1] == matrix[row][col + 2] == matrix[row][col + 3] == player:
                return True

    for col in range(cols):
        for row in range(rows - 3):
            if matrix[row][col] == matrix[row + 1][col] == matrix[row + 2][col] == matrix[row + 3][col] == player:
                return True

    for row in range(rows - 3):
        for col in range(cols - 3):
            if matrix[row][col] == matrix[row + 1][col + 1] == matrix[row + 2][col + 2] == matrix[row + 3][
                col + 3] == player:
                return True

    for row in range(rows - 3):
        for col in range(3, cols):
            if matrix[row][col] == matrix[row + 1][col - 1] == matrix[row + 2][col - 2] == matrix[row + 3][
                col - 3] == player:
                return True

    return False


def main():
    matrix = make_matrix()

    while True:
        move(player1, matrix)
        if check_for_match("1", matrix):
            print(f"Player 1 wins!")
            exit()
        move(player2, matrix)
        if check_for_match("2", matrix):
            print(f"Player 2 wins!")
            exit()
        if CURRENT_MOVE == 42:
            print("It's a draw!")
            exit()


if __name__ == "__main__":
    main()
