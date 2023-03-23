
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