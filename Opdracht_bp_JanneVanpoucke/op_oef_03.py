#opdracht Python oefening 3
#getal in voorbeeld wordt maal 1 gedaan en geprint, de print wordt genomen en maal 2 gedaan, die print wordt genomen en maal 3 gedaan enz.
#getal*1 7*2 14*3 enz.
startGetal = int(input("Geef een getal in:"))
aantalGetallenOpScherm = int(input("Geef het aantal weer te geven getalen in:"))
afdrukOpScherm = ""

for x in range(1, aantalGetallenOpScherm + 1):#loopen van 1 tem waarde aantal weer te geven getallen
	startGetal = startGetal * x#bv. startgetal is 7. Eerste loop is 7*1, tweede loop is 7*2, derde loop is 14*3 WANT je startgetal wordt telkens overschreven doordat hij opnieuw gedefinieerd wordt
	afdrukOpScherm = afdrukOpScherm + str(startGetal) + ','

print(afdrukOpScherm[:-1])