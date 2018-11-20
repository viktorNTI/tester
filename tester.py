import random

alternativ = 0
svar = 0

while alternativ !=100:
    try: 
        alternativ = int(input("Kommer det gå dåligt... eller ännu sämre med uppgiften?"))
    except:
        print("Nej, det kommer gå dåligt, vänligen ange antingen dåligt (1) eller sämre (2)")
    if alternativ == 1:
        svar = random.randint(1,4) 
        if svar == 1:
            print("Korrekt")
        elif svar == 2:
            print("Exakt")
        elif svar == 3:
            print("Precis")
        elif svar == 4:
            print("En slumpvis chans har lett dig till ett meningslöst Easter Egg")