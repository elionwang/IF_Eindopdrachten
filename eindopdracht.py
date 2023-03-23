import random
import time

keuze = input('''
\033[1;36;40mKEUZEMENU\033[0m

\033[1;31;40m[1] = Hoger lager met 10 pogingen\033[0m
\033[1;32;40m[2] = Hoger lager met lingohints\033[0m
\033[1;34;40m[3] = Caesar cipher (encryption, decryption)\033[0m
\033[1;35;40m[4] = L33tspeak\033[0m
\033[1;36;40m[5] = Sudoku solver\033[0m
\033[1;37;40m[6] = ROT13 cipher\033[0m
''')

if int(keuze) == 1:
    randomVictory = ['Gefeliciteerd! Hopelijk ga je nu wat nuttigs doen.', 'Pffff, was het zo moeilijk?', 'Wow! Wil je een sticker?', 'Was dit je tijd waard?', 'Schiet de volgende keer een beetje op, dankjewel.', 'Helaas krijg je hier geen diploma voor, maar gefeliciteerd I guess.']

    randomLoss = ['hahaha hoe verlies je dat nou weer.', 'Dat is best wel teleurstellend eerlijk gezegd.', 'Ik heb spijt dat ik je een kans heb gegeven.', 'Volgende keer beter mag ik hopen.', 'Traumatische ervaring om dit aan te zien.']

    randomWrongGuess = ['Nope, dat is niet het juiste antwoord.', 'Is het zo moeilijk?', 'Nee, dat is niet eens dichtbij.', 'Idioot. Definitie: stompzinnig, achterlijk mens; belachelijk persoon; dwaas.', 'Duurt een beetje lang, vind je niet?']

    play = True

    while play == True:

        i = 0
        guessed = False
        print('\033[1;34;40mHOGER LAGER\033[0m')
        getalRange = int(input('Tot hoe hoog mag het getal zijn? '))
        print('- - - - - - - - - - - - -')

        
        randomInt = random.randint(1, getalRange)
    
        while i < 10:
            guess = int(input('Raad een getal: '))
            if guess == randomInt:
                print(f'\033[1;32;40m{random.choice(randomVictory)} Je hebt gewonnen na {i + 1} poging(en).\033[0m')
                print('- - - - - - - - - - - - -')
                guessed = True
                break
            elif guess < randomInt:
                print(f'⬆️ | {random.choice(randomWrongGuess)} Je hebt nog {9 - i} pogingen om het getal te raden.')
                print('- - - - - - - - - - - - -')
            elif guess > randomInt:
                print(f'⬇️ | {random.choice(randomWrongGuess)} Je hebt nog {9 - i} pogingen om het getal te raden.')
                print('- - - - - - - - - - - - -')
            i += 1
            
        if guessed != True:
            print(f'\033[1;31;40m{random.choice(randomLoss)} Helaas!\033[0m')

        time.sleep(5)
        print("\033c", end='')
        again = input('Wil je nog een keer spelen? (j/n) ')
        if again == 'j':
            print('Is goed, succes!')
            time.sleep(3)
            print("\033c", end='')
            continue
        else:
            print('Oke dan, ik zeg niks meer.')
            exit()
elif int(keuze) == 2:
    randomVictory = ['Gefeliciteerd! Hopelijk ga je nu wat nuttigs doen.', 'Pffff, was het zo moeilijk?', 'Wow! Wil je een sticker?', 'Was dit je tijd waard?', 'Schiet de volgende keer een beetje op, dankjewel.', 'Helaas krijg je hier geen diploma voor, maar gefeliciteerd I guess.']

    randomLoss = ['hahaha hoe verlies je dat nou weer.', 'Dat is best wel teleurstellend eerlijk gezegd.', 'Ik heb spijt dat ik je een kans heb gegeven.', 'Volgende keer beter mag ik hopen.', 'Traumatische ervaring om dit aan te zien.']

    randomWrongGuess = ['Nope, dat is niet het juiste antwoord.', 'Is het zo moeilijk?', 'Nee, dat is niet eens dichtbij.', 'Idioot. Definitie: stompzinnig, achterlijk mens; belachelijk persoon; dwaas.', 'Duurt een beetje lang, vind je niet?']

    play = True

    while play == True:

        i = 0
        guessed = False
        print('\033[1;34;40mHOGER LAGER\033[0m')
        print('- - - - - - - - - - - - -')

        
        randomInt = random.randint(100, 1000)
    
        while i < 10:
            guess = int(input('Raad een getal (100 t/m 999): '))
            if str(guess)[0] == str(randomInt)[0]:
                num1 = '\033[1;32;40mgroen\033[0m'
            elif str(guess)[0] in str(randomInt):
                num1 = '\033[1;33;40moranje\033[0m'
            else:
                num1 = '\033[1;31;40mrood\033[0m'

            if str(guess)[1] == str(randomInt)[1]:
                num2 = '\033[1;32;40mgroen\033[0m'
            elif str(guess)[1] in str(randomInt):
                num2 = '\033[1;33;40moranje\033[0m'
            else:
                num2 = '\033[1;31;40mrood\033[0m'

            if str(guess)[2] == str(randomInt)[2]:
                num3 = '\033[1;32;40mgroen\033[0m'
            elif str(guess)[2] in str(randomInt):
                num3 = '\033[1;33;40moranje\033[0m'
            else:
                num3 = '\033[1;31;40mrood\033[0m'
            
            if guess == randomInt:
                print(f'\033[1;32;40m{random.choice(randomVictory)} Je hebt gewonnen na {i + 1} poging(en).\033[0m')
                print('- - - - - - - - - - - - -')
                guessed = True
                break
            elif guess < randomInt:
                print(f'⬆️ | {random.choice(randomWrongGuess)} Je hebt nog {9 - i} pogingen om het getal te raden.')
                print('- - - - - - - - - - - - -')
                print(f'Hint: {num1} {num2} {num3}')
            elif guess > randomInt: 
                print(f'⬇️ | {random.choice(randomWrongGuess)} Je hebt nog {9 - i} pogingen om het getal te raden.')
                print('- - - - - - - - - - - - -')
                print(f'Hint: {num1} {num2} {num3}')
            i += 1
        
        if guessed != True:
            print(f'\033[1;31;40m{random.choice(randomLoss)} Helaas!\033[0m')

        time.sleep(5)
        print("\033c", end='')
        again = input('Wil je nog een keer spelen? (j/n) ')
        if again == 'j':
            print('Is goed, succes!')
            time.sleep(3)
            print("\033c", end='')
            continue
        else:
            print('Oke dan, ik zeg niks meer.')
            exit()
elif int(keuze) == 3:
    # vraag of user wil encrypten of decrypten
    encryptOrDecrypt = input('Wil je iets encrypten (enc) of decrypten (dec)? \n> ') 

    # check of user wil encrypten, voer dan code uit
    if encryptOrDecrypt.lower() == 'enc':
        txt = input('Wat wil je encrypten aan tekst? \n> ')
        shift = int(input('Hoeveel wil je shiften naar links (-1, -2...) of rechts (1, 2...)? \n> '))

        
        # maak functie voor encrypten van elk karakter in txt
        def encrypt(txt, shift):
            encryptedTxt = ''
            for i in range(len(txt)):
                if txt[i] == ' ':
                    encryptedTxt += ' '
                elif txt[i].isdigit() == True:
                    encryptedTxt += txt[i]
                elif txt[i].isupper() == True:
                    encryptedTxt += chr((ord(txt[i]) + shift-65) % 26 + 65) # gebruik nummer unicode om correcte karakter toe te voegen aan encryptedTxt
                elif txt[i].islower() == True:
                    encryptedTxt += chr((ord(txt[i]) + shift-97) % 26 + 97) # gebruik nummer unicode om correcte karakter toe te voegen aan encryptedTxt
                else:
                    encryptedTxt += txt[i]
                return encryptedTxt

        print(f'Normale tekst: {txt}')
        print(f'Shift: {shift}')
        print(f'Encrypted tekst: {encrypt(txt, shift)}')

    # check of user wil decrypten
    elif encryptOrDecrypt.lower() == 'dec':
        txt = input('Wat wil je decrypten aan tekst? \n> ')
        alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # maak string met elk letter in alfabet of index te kunnen gebruiken

        for i in range(len(alfabet)): # loop voor het aantal letters in alfabet (aantal verschillende shifts)
            decryptedTxt = ''
            for j in txt.upper():
                if j in alfabet:
                    num = alfabet.find(j)
                    num -= i
                    if num < 0:
                        num += len(alfabet)
                    decryptedTxt += alfabet[num]
                else: 
                    decryptedTxt += j
            print(f'Shift {i}: {decryptedTxt}, Experience is the teacher of all things.')
elif int(keuze) == 4:
    
    # taal = input('Vertalen vanuit tekst (txt) of leetspeak (lt)? ')

    leetspeak = {
        'A': '4',
        'B': '8',
    # 'C': '[',
    # 'D': ')',
        'E': '3',
    # 'F': '|=',
        'G': '9',
        'H': '#',
        'I': '1',
    # 'J': ',_|',
    # 'K': '>|',
        'L': '£',
    # 'M': '|V|',
    # 'N': '^/',
        'O': '0',
    # 'P': '|*',
    # 'Q': '(_,)',
        'R': '2',
        'S': '5',
        'T': '7',
        'U': '(_)',
        'V': '|/',
        'W': 'VV',
        'X': '><',
        'Y': 'j',
        'Z': '2'
    }

    # if taal == 'txt':
    woorden = input('Wat wil je vertalen naar 13375p33k (leetspeak)? \n> ')
    woorden = woorden.upper()

    
    # elif taal == 'lt':
    # woorden = input('Wat wil je vertalen naar tekst? \n> ')
    reversedLeetspeak = dict()
    key_list = list(leetspeak.keys())
    val_list = list(leetspeak.values())
    for i in range(len(key_list)):
        key = val_list[i]
        val = key_list[i]
        reversedLeetspeak[key] = val   
    leetspeak.update(reversedLeetspeak)

    
    translation = ''
    for karakter in woorden:
        translation += leetspeak.get(karakter, karakter)

    print(translation)
elif int(keuze) == 5:
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
elif int(keuze) == 6:
    # ROT13 Cipher

    txt = input('Wat wil je encrypten / decrypten aan tekst? \n> ')

    def rot13(txt):
        translation = ''
        for ch in range(len(txt)):
            if txt[ch] == ' ':
                translation += ' '
            elif txt.isdigit() == True:
                translation += ch
            elif txt[ch].isupper() == True:
                translation += chr((ord(txt[ch]) + (13 - 65)) % 26 + 65)
            elif txt[ch].islower() == True:
                translation += chr((ord(txt[ch]) + (13 - 97)) % 26 + 97)
            else:
                translation += txt[ch]
        return translation
    
    print("\033c", end='')
    print(f'Normale tekst: {txt}')
    print(f'Shift: (ROT)13')
    print(f'Output: {rot13(txt)}')