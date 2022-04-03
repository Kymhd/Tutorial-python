"""
calculs des heures suplementaires au-delà de 40h, 
les heures supp sont payes en doubles du taux, 50%
"""

def calcul_paie(heures, taux):
    if heures > 40:
         heures_supplementaire = heures - 40
         majoration = heures_supplementaire *(taux * 1.50)
         return majoration + (40 * taux)
    else:
        return taux * heures

def heur():
    heure_int = 0
    while heure_int == 0:
        heure = input("Entrez les heures: ")
        try:
            heure_int = int(heure)
        except:
            print("Vous devez entrez un chiffre")
    return heure_int

entrez_heures = heur()
entrez_taux = (float(input("Entrez le taux: ")))

print("La réenumeration est de:",calcul_paie(entrez_heures, entrez_taux))

