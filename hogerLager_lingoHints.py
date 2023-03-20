import random
import time

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
      num1 = 'groen'
    elif str(guess)[0] in str(randomInt):
      num1 = 'oranje'
    else:
      num1 = 'rood'

    if str(guess)[1] == str(randomInt)[1]:
      num2 = 'groen'
    elif str(guess)[1] in str(randomInt):
      num2 = 'oranje'
    else:
      num2 = 'rood'

    if str(guess)[2] == str(randomInt)[2]:
      num3 = 'groen'
    elif str(guess)[2] in str(randomInt):
      num3 = 'oranje'
    else:
      num3 = 'rood'
    
    if guess == randomInt:
      print(f'\033[1;32;40m{random.choice(randomVictory)} Je hebt gewonnen na {i + 1} poging(en).\033[0m')
      print('- - - - - - - - - - - - -')
      guessed = True
      break
    else:
      print(f'{random.choice(randomWrongGuess)} Je hebt nog {9 - i} pogingen om het getal te raden.')
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
