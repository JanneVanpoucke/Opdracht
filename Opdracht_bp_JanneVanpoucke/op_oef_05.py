#opdracht Python oefening 5
import random
getal = 0
reeks = []
eindGetal = int(input("Geef een eindGetal: "))
einde = ""
afdruk = ""
teller = random.randint(0,3)

for x in range(0,eindGetal):
    if(x < 1):#als x kleiner is dan 1...
        getal = teller#...wordt getal de waarde van de teller. Getal is hier dus 0,3.
    else:
        getal = x * teller#dus de eerste waarde in je teller maal x en de tweede waarde in teller maal x 
    einde = "(" + str(x) + "," + str(getal)+")"+","#einde wordt 'gevuld' met string(x) en string(getal) plus de haakjes en komma's die je geprint wil zien. Einde is (0,0)
    afdruk = afdruk + einde#afdruk plus je verschillende 'eindes' naast elkaar te printen. Afdruk = (ei,nde), plus (ei,nde) tem eindgetal
    reeks.append(einde)#de eind-waarde wordt in array reeks gestopt
    
print("Resultaat:")
print("mijn reeks =",einde[:-1])#er wordt pas geprint nadat de for loop opnieuw gelopen heeft tot eindGetal, daarom staat print op zelfde niveau van for loop, maar niet in de for loop