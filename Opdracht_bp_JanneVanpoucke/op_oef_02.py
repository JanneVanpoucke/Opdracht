#opdracht Python oefening 2

# START DEFINITIE
def wegMetKlinkers(string): 
    klinkers = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') #DEFINEER DE KLINKERS 
    for x in string: #ELKE LETTER IN STRING WORDT OVERLOPEN. DIT IS DE RANGE
        if x in klinkers: #ALS DE LETTER VOORKOMT IN ARRAY KLINKERS DAN...
            string = string.replace(x, "") #...WORDT DE KLINKER VERVANGEN DOOR 'NIKS'           
    print(string)#UITKOMST VAN JE FOR LOOP: PRINT DE STRING ZONDER KLINKER
  
# START PROGRAMMA
string = input("Geef een zin in: ")
wegMetKlinkers(string)