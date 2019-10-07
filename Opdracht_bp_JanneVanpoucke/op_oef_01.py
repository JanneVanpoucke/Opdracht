#opdracht Python oefening 1
import random
eindGetal = int(input("Geef een eindgetal: "))
hoeveelGetallen = int(input("Hoeveel getallen dien ik te genereren: "))
nietGesorteerd = []
gesorteerd = []
aantalKeer = 1
invoer = "J"

while (invoer == 'J'):#while moet vanboven, enkel zo zal het programma opnieuw lopen als je J invoert. Je volledige programma moet genest zijn in de while. ZOLANG = KERNWOORD
    for x in range(0, hoeveelGetallen):#de for loop loopt tem de waarde van je hoeveelGetallen. Dus hoeveelGetallen keer. Telken maal de loop cycled wordt een waarde toegevoegd aan de arrays hieronder
        nietGesorteerd.append(random.randint(0, eindGetal))#hier wordt telkens een random getal (dankzij de randomfuntie)toegevoegd aan de nietGesorteerde array. Toevoeging gebeurd door de append-functie
    print("gegenereerde getallen:", nietGesorteerd)#hier wordt de nietGesorteerde array geprint
    
    list.sort(nietGesorteerd)#functie om de getallen te sorteren
    gesorteerd = nietGesorteerd#gesorteerd wordt gelijkgesteld aan niet gesorteerd voor de duidelijkheid dat het nu een gesorteerde array is
    print("Gesorteerde getallen: ", gesorteerd)#hier print je de gesorteerde array
    
    print("Het programma werd reeds " + str(aantalKeer) +  " keer uitgevoerd.")#aantal keer is hier onmiddelijk 1, want je hebt je variabele aantalKeer op 1 gezet bij de declaratie
    aantalKeer = aantalKeer + 1 #dit zet je pas onder de print. Erboven zal anders zorgen van een resultaat van 2 keer bij de eerste print omdat de waarde van aantalKeer start op 1
    
    nietGesorteerd = [] #hier reset je de array, anders stopt hij waardes die hij genereert in de tweede loop gewoon bij degene die al in de eerste loop staan.
    gesorteerd = [] #hier reset je de array, anders stopt hij waardes die hij genereert in de tweede loop gewoon bij degene die al in de eerste loop staan.
    
    invoer = (input("Wenst u het programma uit te voeren? Typ J/N: ")).upper()#wordt op het einde telkens gevraagd tot een andere waarde dan J wordt ingegeven. Dit is de conditie van je while (==J)