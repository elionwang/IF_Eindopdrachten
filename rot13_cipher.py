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

print(f'Normale tekst: {txt}')
print(f'Shift: (ROT)13')
print(f'Output: {rot13(txt)}')