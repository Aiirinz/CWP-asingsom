def checkmate(board_str):
    board = board_str.split("\n")
    n = len(board)

    if n == 0 or any(len(row) != n for row in board):
        return

    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                kr, kc = r, c

    for r in range(n):
        for c in range(n):
            if board[r][c] in "PBRQ" and can_attack(
                board[r][c], r, c, kr, kc, board
            ):
                print("Success")
                return

    print("Fail")


def can_attack(piece, r, c, kr, kc, board):
    dr = kr - r
    dc = kc - c

    if piece == "P":
        return dr == -1 and abs(dc) == 1

    if piece == "R":
        straight = r == kr or c == kc
        return straight and clear_path(r, c, kr, kc, board)

    if piece == "B":
        diagonal = abs(dr) == abs(dc)
        return diagonal and clear_path(r, c, kr, kc, board)

    if piece == "Q":
        straight = r == kr or c == kc
        diagonal = abs(dr) == abs(dc)
        return (straight or diagonal) and clear_path(
            r, c, kr, kc, board
        )

    return False


def clear_path(r, c, kr, kc, board):
    dr = 1 if kr > r else -1 if kr < r else 0
    dc = 1 if kc > c else -1 if kc < c else 0

    r += dr
    c += dc

    while (r, c) != (kr, kc):
        if board[r][c] in "PBRQK":
            return False
        r += dr
        c += dc

    return True