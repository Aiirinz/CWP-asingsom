straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def find_first_piece(board_rows, r, c, step_r, step_c):
  r, c = r + step_r, c + step_c
  while 0 <= r < len(board_rows) and 0 <= c < len(board_rows):
    if board_rows[r][c] in "PBRQK":
      return board_rows[r][c]
    r, c = r + step_r, c + step_c
  return None

def checkmate(board):
  board_rows = board.splitlines()

  if not board_rows or any(len(r) != len(board_rows) for r in board_rows):
    print("Error")
    return

  king_count = sum(row.count("K") for row in board_rows)
  if king_count != 1:
    print("Error")
    return

  k_row = next(i for i, row in enumerate(board_rows) if "K" in row)
  k_col = board_rows[k_row].index("K")

  pawn_positions = [
      (k_row - 1, k_col - 1),
      (k_row - 1, k_col + 1),
      (k_row + 1, k_col - 1),
      (k_row + 1, k_col + 1),
  ]
  is_checked = any(
      0 <= r < len(board_rows)
      and 0 <= c < len(board_rows)
      and board_rows[r][c] == "P"
      for r, c in pawn_positions
  )

  
  for step in straight_directions:
    if find_first_piece(board_rows, k_row, k_col, *step) in ("R", "Q"):
      is_checked = True

  
  for step in diagonal_directions:
    if find_first_piece(board_rows, k_row, k_col, *step) in ("B", "Q"):
      is_checked = True

 
  if is_checked:
    print("Success")
  else:
    print("Fail")