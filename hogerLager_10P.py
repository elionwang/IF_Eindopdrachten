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
  getalRange = int(input('Tot hoe hoog mag het getal zijn? '))
  print('- - - - - - - - - - - - -')

  
  randomInt = random.randint(1, getalRange + 1)
  
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