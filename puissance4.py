import numpy as np

"""
This code implements a simple tic-tac-toe game.

The game is played on a 3x3 grid. Players take turns placing their marks (X or O) on the grid. The first player to get three of their marks in a row, column, or diagonal wins the game.

The code uses the following functions:

* `game_over()`: Checks if the game is over.
* `draw()`: Checks if the game is a draw.
* `cases_jouables()`: Returns a list of the playable cells on the grid.
* `play()`: Plays the game.
* `get_move_ai()`: Gets the next move for the AI.
* `minimax()`: Performs a minimax search to find the best move for the AI.

To run the code, simply save it as a Python file and run it from the command line.
"""


def game_over(M):
    """
    Checks if the game is over.

    Args:
        M: The game board.

    Returns:
        True if the game is over, False otherwise.
    """

    for i in range(0, 3):
        if M[i][0] == M[i][1] == M[i][2] != '-':
            return True
        if M[0][i] == M[1][i] == M[2][i] != '-':
            return True
        if M[i][0] == M[i+1][1] == M[i+2][2] != '-':
            return True
        if M[i+2][0] == M[i+1][1] == M[i][2] != '-':
            return True
    return False


def draw(M):
    """
    Checks if the game is a draw.

    Args:
        M: The game board.

    Returns:
        True if the game is a draw, False otherwise.
    """

    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == '-':
                return False
    return True


def cases_jouables(M):
    """
    Returns a list of the playable cells on the grid.

    Args:
        M: The game board.

    Returns:
        A list of the playable cells.
    """

    cases_jouables = []

    for j in range(len(M[0])):
        colonne_pleine = True
        for i in range(0, len(M)):
            if M[len(M)-1-i][j] == '-':
                ligne = len(M)-i
                cases_jouables.append(ligne)
                colonne_pleine = False
                break
        if colonne_pleine == True:
            cases_jouables.append(0)
    return cases_jouables


def play():
    """
    Plays the game.
    """

    M = [['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-'],
         ['-', '-', '-', '-', '-', '-', '-']]
    while True:
        print(np.array(M))
        # tour de l'humain
        lignes_jouables = cases_jouables(M)
        colonne = int(
            input("Choisissez la colonne de votre prochain coup : "))
        M[lignes_jouables[colonne-1]-1][colonne-1] = 'X'
        print(np.array(M))
        if game_over(M):
            print("L'humain a gagné")
            break
        if draw(M):
            print("Match nul")
            break

        # tour de l'IA
        i = get_move_ai(M)
        lignes_jouables = cases_jou
