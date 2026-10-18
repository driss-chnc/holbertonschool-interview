#!/usr/bin/python3

import sys


def n_not_valid():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return True

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return True

    if n < 4:
        print("N must be at least 4")
        return True

    return False


def solve_nqueens(n, row=0, positions=None):
    if positions is None:
        positions = []

    # Toutes les reines sont placees : solution trouvee
    if row == n:
        print(positions)
        return

    # Essayer chaque colonne de la ligne actuelle
    for col in range(n):
        valid = True

        # Verifier les reines deja placees
        for prev_row, prev_col in positions:

            # Meme colonne ou meme diagonale
            if (prev_col == col or
                    abs(prev_row - row) == abs(prev_col - col)):
                valid = False
                break

        # Si la position est sure, placer la reine
        if valid:
            positions.append([row, col])

            # Passer a la ligne suivante
            solve_nqueens(n, row + 1, positions)

            # Backtracking : retirer la reine pour essayer
            # une autre colonne
            positions.pop()


if __name__ == "__main__":
    if n_not_valid():
        sys.exit(1)

    n = int(sys.argv[1])
    solve_nqueens(n)
