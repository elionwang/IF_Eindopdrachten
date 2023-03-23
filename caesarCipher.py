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