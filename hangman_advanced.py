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
  #Loesungswort bis auf letzten Buchstaben durchgegangen und entsprechend Buchstabe oder _ geprintet
    for i in range(len(loesungsWort)-1):
      #Variable zum testen, ob bereits ein Buchstabe geprintet wurde oder ob es ein _ braucht
        didPrint = "NO"
        #guesses durchgehen und checken, ob im Wort vorhanden. Wenn ja: Buchstabe printen; sonst _
        for b in range(len(guesses)):
          if guesses[b] == loesungsWort[i]:
            print(' ' + guesses[b], end=' ')
            didPrint = "YES"
          elif b == len(guesses)-1 and didPrint == "NO":
            print(" _", end=' ')

    #Für Zeilenumbruch am Ende, wird nun noch dieser Codeteil für den letzten Buchstaben von
    #Loesungswort durchgeführt. Gleicher Mechanismus wie oben
    didPrint = "NO"
    for c in range(len(guesses)):
      #[-1] für letzten Buchstaben
      if guesses[c] == loesungsWort[-1]:
        print(' ' + guesses[c])
        didPrint = "YES"
      elif c == len(guesses)-1 and didPrint == "NO":
        print(" _")



# Spielcode
# While-Schleife, um erneuten Spielstart zu ermöglichen
while antwort == "YES":
    anzLeben = 6
    lebenCount = 0
    guesses = []
    # Wählt zufällige Zeile und somit zufälliges Wort aus dem File mit Substantiven und weist sie
    # loesungsWort zu und macht sie dabei uppercase und entfernt mit .strip() allfällige Leerzeichen
    loesungsWort = (linecache.getline("Substantive.txt", (random.randint(0, 14622)))).upper().strip()
    # cleart die Konsole
    print("\033[H\033[J", end="")
    #Printet Grafische Elemente gemäss eigener Methode mit hier definierten Variablen
    GrafikOutput(lebenCount, guesses, loesungsWort)
    #While-Schleife, damit während Wort noch nicht erraten wurde, immer wieder neu geguesst wird
    while(IstErraten(guesses, loesungsWort) == False):
      guess = str(input("Rate einen Buchstaben: ")).upper()
      # Verhindert erneute guesses, guesses mit mehr als 1 Zeichen oder leere Guesses
      # und lässt erneut guessen bis legitimer Guess
      while guess in guesses or ((len(guess))>1) or ((len(guess))==0):
        print("Dieser Buchstabe wurde bereits geraten oder es handelt sich um mehr als 1 oder um kein Zeichen.")
        guess = str(input("Rate einen Buchstaben: ")).upper()
      #Guess wird der Liste mit bereits geguessten Buchstaben hinzugefügt
      guesses.append(guess)
      #Wenn Buchstabe enthalten, dann wird er auf Console grafisch ergänzt
      if loesungsWort.find(guess) >= 0:
        print("\033[H\033[J", end="") 
        GrafikOutput(lebenCount, guesses, loesungsWort)
      # Wenn nicht enthalten, dann ausgaben dass nicht enthalten
      else:
        lebenCount += 1
        #Wenn noch Leben übrig sind, wird wieder der normale Screen geprintet
        if lebenCount < anzLeben:
          print("\033[H\033[J", end="") 
          GrafikOutput(lebenCount, guesses, loesungsWort)
        #Wenn es das letzte Leben war, wird Spiel beendet und nach neuer Runde gefragt
        else:
          print("\033[H\033[J", end="")
          GrafikOutput(lebenCount, guesses, loesungsWort)
          print("You loose, gesucht war " + loesungsWort + "\nNoch ne Runde?")
          break
    # Wenn gewonnen, wird Win geprintet und nach neuer Runde gefragt
    if IstErraten(guesses, loesungsWort) == True:
      print("You Win :) \nNoch ne Runde?")
    # Antwort für neue Runde, unabhängig von Win oder Loose
    answer = input("Tippe YES oder NO \n")
    # Wenn keine neue Runde gespielt wird, wird Danke geprintet und Spiel beendet
    if answer != "YES":
      print("\033[H\033[J", end="")
      print("Vielen Dank fürs Spielen")
      break
