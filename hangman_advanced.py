import random
import linecache
#Variable für While-Schleife vom Game selbst
antwort = "YES"
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Methode zum Checken, ob Lösungswort bereits erraten wurde
def IstErraten(guesses, loesungsWort):
  counter = 0
  for i in range (len(guesses)):
    #Counter wird erhöht so oft wie der i'te guess im loesungsWort vorhanden ist
    counter = counter + loesungsWort.count(guesses[i])
    #Wenn so viele Buchstaben erraten wurden, wie das loesungsWort lang ist, wird true returnt
  if counter == len(loesungsWort):
    return True
  else:
    return False


#Methode für Grafik Output (Hangman und Lösungswort mit _ für unerratene Buchstaben)
def GrafikOutput(lebenCount, guesses, loesungsWort):
  #printet das aktuelle Hangmanpic
  print(HANGMANPICS[lebenCount], end=' ')
  #Bei Spielbeginn ist guesses noch leer, also wird mit dieser if-Bedingung das abgleichen mit
  #Loesungswort übersprungen und einfach _ geprintet für jeden Buchstaben im loesungsWort
  if len(guesses) == 0:
    for i in range(len(loesungsWort)-1):
      print(" _", end=" ")
    print(" _")
  #Else damit nur entweder oder gemacht wird und nicht beides auf einmal bei Spielbeginn
  else:
  #loesungswort wird Buchstabe für Buchstabe mit den guesses abgeglichen und entsprechend geprintet
    for i in range(len(loesungsWort)-1):
      #Variable zum testen, ob bereits ein Buchstabe geprintet wurde oder ob es ein _ braucht
        didPrint = "NO"
        for b in range(len(guesses)):
          if guesses[b] == loesungsWort[i]:
            print(' ' + guesses[b], end=' ')
            didPrint = "YES"
          elif b == len(guesses)-1 and didPrint == "NO":
            print(" _", end=' ')
    didPrint = "NO"
    #Damit am Ende ein Zeilenumbruch kommt, wird dieser Codeteil für den letzten Buchstaben von
    #Loesungswort durchgeführt
    for c in range(len(guesses)):
      if guesses[c] == loesungsWort[-1]:
        print(' ' + guesses[c])
        didPrint = "YES"
      elif c == len(guesses)-1 and didPrint == "NO":
        print(" _")

# Gesamter Spielcode
while antwort == "YES":
    anzLeben = 6
    lebenCount = 0
    guesses = []
    # Wählt zufällige Zeile und somit zufälliges Wort aus dem File mit Substantiven
    # und weist sie der variable loesungsWortGross zu und macht sie dabei uppercase
    loesungsWort = (linecache.getline("Substantive.txt", (random.randint(0, 14622)))).upper().strip()
    print("\033[H\033[J", end="")
    print(loesungsWort + "Apfel")
    GrafikOutput(lebenCount, guesses, loesungsWort)
    while(IstErraten(guesses, loesungsWort) == False):
      guess = str(input("Rate einen Buchstaben: ")).upper()
      while guess in guesses or ((len(guess))>1):
        print("Dieser Buchstabe wurde bereits geraten oder es handelt sich um mehr als 1 Zeichen.")
        guess = str(input("Rate einen Buchstaben: ")).upper()
      guesses.append(guess)
      if loesungsWort.find(guess) >= 0:
        print("\033[H\033[J", end="") 
        GrafikOutput(lebenCount, guesses, loesungsWort)
      else:
        print("Dieser Buchstabe ist leider nicht enthalten")
        lebenCount += 1
        if lebenCount < anzLeben:
          print("\033[H\033[J", end="") 
          GrafikOutput(lebenCount, guesses, loesungsWort)
        else:
          print("\033[H\033[J", end="")
          GrafikOutput(lebenCount, guesses, loesungsWort)
          print("You loose, gesucht war " + loesungsWort + "\nNoch ne Runde?")
          break
    if IstErraten(guesses, loesungsWort) == True:
      print("You Win :) \nNoch ne Runde?")
    answer = input("Tippe YES oder NO \n")
    if answer != "YES":
      print("\033[H\033[J", end="")
      print("Vielen Dank fürs Spielen")
      break
