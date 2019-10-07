# opdracht Python oefening 4
letter = input("Geef de laatste letter in die je op het scherm wil zien: ")
hoofdLetter = letter.upper()#letter sowieso omzetten naar een hoofdletter
letterNaarCijfer = ord(hoofdLetter)#letter via ord-functie omzetten naar getal die overeenkomt met waarde van de asciitabel
afdrukOpScherm = ""

for x in range(65,(letterNaarCijfer+1)):#starten aan 65, want dit is de ascii-waarde die overeenkomt met hoofdletter A. De for loop cycled tem de waarde van letterNaarCijfer 
	afdrukOpScherm = afdrukOpScherm + chr(x)#x wordt telkens afgedrukt en door de chr-functie wordt de numerieke waarde omgezet naar letterwaarde volgens de asciitabel
print(afdrukOpScherm)#deze print moet er staan want hieronder ga je telkens een waarde aftrekken.
	
for x in range(1,(len(afdrukOpScherm))):#met deze for loop draaien we de volgorde van afdrukken om en dat doen we door de lengte van afdrukOpScherm te gebruiken. Deze aOP heeft reeds door de eerste for loop gecycled dus start met lengte 5 als letter E is
	print(afdrukOpScherm[:-x])#hier trekken we x af van onze afdruk op scherm en dit doen we opnieuw tot de waarde van de lengte bereikt is. dus de eerste keer starten we van 1 tot 5 (niet tem 5) dus de loop zal in totaal 4 keer lopen. De eerste keer gebeurt er dus ABCDE - 1 = ABCD. De tweede keer ABCDE - 2 = ABC enz.