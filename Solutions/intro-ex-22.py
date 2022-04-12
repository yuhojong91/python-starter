# 
# File: intro-ex-22.py
# Auth: Martin Burolla
# Date: 8/22/2021
# Desc: Morse Codify It
#

def main():
  while True:
    inputString = input('Enter text: ').lower()
    morseCode = convertTextToMorseCode(inputString)
    print(f'Morse Code: { morseCode }')

def convertTextToMorseCode(text):
  retval = ''
  textToMorseDict = {
    'a' : '*-',
    'b' : '-***',
    'c' : '-*-*',
    'd' : '-**',
    'e' : '*',
    'f' : '**-*',
    'g' : '--*',
    'h' : '****',
    'i' : '**',
    'j' : '*---',
    'k' : '-*-',
    'l' : '*-**',
    'm' : '--',
    'n' : '-*',
    'o' : '---',
    'p' : '*--*',
    'q' : '--*-',
    'r' : '*-*',
    's' : '***',
    't' : '-',
    'u' : '**-',
    'v' : '***-',
    'w' : '*--',
    'x' : '-**-',
    'y' : '-*--',
    'z' : '--**'
  }

  for char in text:
    if char == ' ':
      retval += ' '
    else:
      retval += (textToMorseDict[char] + ' ')
  return retval

if __name__ == "__main__":  
  main()
