import time # import time library

# maak een sudoku board met arrays voor elke rij binnen 1 array
board = [
  [4, 7, 0, 2, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 4, 5],
  [0, 0, 1, 0, 0, 0, 7, 2, 0],
  [5, 0, 0, 0, 0, 7, 9, 0, 0],
  [3, 0, 2, 9, 1, 0, 0, 0, 0],
  [0, 0, 0, 6, 8, 3, 0, 0, 0],
  [0, 0, 0, 1, 0, 2, 0, 0, 9],
  [7, 3, 4, 5, 0, 8, 1, 0, 0],
  [2, 0, 0, 0, 0, 0, 0, 0, 0]
]

# maak een functie om het sudoku board goed te kunnen printen naar de console
def print_board(board): 
  for i in range(len(board)): # loop voor elke rij (elk element in de 'board' array)
    if i % 3 == 0 and i != 0: # check of i (rijnummer) deelbaar is door 3, (elke derde rij behalve bovenaan)
      print('- - - - - - - - - - - -') # print lijn naar console, om elk blok te verdelen (rij)
    for j in range(len(board[0])): # loop voor elke element
      if j % 3 == 0 and j != 0: # check of j (kolomnummer) deelbaar is door 3, (elke derde rij behalve bovenaan)
        print(' | ', end = "") # print verticaal lijntje naar console, om elk blok te verdelen (kolom), end voor new line

      if j == 8: # check of j gelijk staat tot 8 (laatste line)
        print(board[i][j]) # print line en ga terug naar begin van loop
        print    
      else:
        print(str(board[i][j]) + " ", end = "") # print line, gebruik str functie, want anders heb je een int 


# maak een functie om elk leeg vakje te vinden
def find_empty(board):
  for i in range(len(board)): # loop voor elke rij (elk element in de 'board' array)
    for j in range(len(board[0])): # loop voor elk element
      if board[i][j] == 0: # check of vakje een waarde heeft van 0
        return (i, j) # return coördinaat (rij, kolom)

  return None # anders 'None' returnen


# maak een functie om te checken of er een geldige sudoku gegeven is
def is_valid(board, num, pos):
  for i in range(len(board[0])): # loop voor elke rij
    if board[pos[0]][i] == num and pos[1] != i: # check of positie al eerder is opgelost en of het nummer 2x voorkomt in de rij
      return False 

  for i in range(len(board)): # loop voor elke rij (check kolom)
    if board[i][pos[1]] == num and pos[0] != i: # check of positie al eerder is opgelost en of het nummer 2x voorkomt in de rij
      return False

  box_x = pos[1] // 3 # floor division om te checken op welke box [verticaal] (0 t/m 2, 3 t/m 5, 6 t/m 8) het getal staat
  box_y = pos[0] // 3 # floor division om te checken op welke box [horizontaal] (0 t/m 2, 3 t/m 5, 6 t/m 8) het getal staat

  for i in range(box_y * 3, box_y * 3 + 3): # loop door alle elementen in de box, vermenigvuldig met 3 om de correcte indexen te krijgen;
    for j in range(box_x * 3, box_x * 3 + 3):
      if board[i][j] == num and (i, j) != pos: # check of nummer 2x voorkomt in de box
        return False 

  return True # als deze condities niet kloppen, return True

# maak een functie om de sudoku op te lossen
def solve(board):
  find = find_empty(board) # zoek lege vakjes in de sudoku
  if not find: # bij geen positieve waarde voor find
    return True # return True als sudoku al opgelost is
  else:
    row, col = find 

  for i in range(1, 10):
    if is_valid(board, i, (row, col)): # check wat het werkende getal is voor die positie
      board[row][col] = i # vul het in in de positie

      if solve(board): # check of er een werkend getal is in die positie
        return True

      board[row][col] = 0 # als er geen werkend getal is, maak de waarde 0

  return False # bij geen werkend, getal, return False


print('\033[3;37;40mGegeven sudoku board:\033[0m', end = '\n')
print_board(board)
time.sleep(2)
print("\033c", end='')
print('\033[1;34;40mOplossen...\033[0m')
solve(board)

time.sleep(2)
tijd = time.time()
solve(board)
print("\033c", end='')
print('\033[1;32;40mOpgeloste sudoku:\033[0m')
print_board(board)
print('________________________')
print(f'Sudoku opgelost in {time.time() - tijd} seconden.') 