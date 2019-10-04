import random

erg = random.randint(0, 100)
print("Bitte erraten sie die gesuchte Zahl, sie befindet sich zwischen 1 und 100", erg)
i = 1
while True:
    print("ihr " + str(i) + ". Versuch:")
    zahl = int(input())
    if zahl > erg:
        print("die gesuchte Zahl ist kleiner.")
    elif zahl < erg:
        print("die gesuchte Zahl ist größer.")
    elif zahl == erg:
        print("Glückwunsch die von Ihnen eingebene Zahl" , erg ,  "stimmt mit der gesuchten Zahl überein.")
    i += 1
