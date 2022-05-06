class Carte :
    def __init__(self,Joueur,Mage,Cristal,Creature,Blast,Mana):
        self.Mage=Mage
        self.Joueur=Joueur
        self.Cristal=Cristal
        self.Creature=Creature
        self.Blast=Blast
        self.Mana=Mana

    def getCarte(self) :
        print(self.Cristal," C ",self.Creature," Creature ",self.Blast," B ",self.Mage," M ",self.Mana," M ")


class Mage :
    def __init__(self,Mana,PV):
        self.Mana=Mana
        self.PV=PV

    def getMage(self) :
        print(self.Mana," M "," Action ",self.PV," PV ")

class Creature : 
    def __init__(self,Mana,PV):
        self.Mana=Mana
        self.PV=PV

class Cristal : 
    def __init__(self,Mana):
        self.Mana=Mana

class Blast : 
    def __init__(self,Mana):
        self.Mana=Mana

#class Mana : 
#    def getMana(self):
#        return self.Mana 

 #   def getManaperdu(self, ManaPerdu):
  #      self.Mana = self.Mana - ManaPerdu

Tour1 = ["_","_","_","_","_"]

Joueur1 = Carte("Joueur1",0,0,0,0,20)
Joueur2 = Carte("Joueur2",0,0,0,0,20)

Joueur1.getCarte()
Joueur2.getCarte()

#NBmana = Mana
#PrixAction = 10
#Action1 = Creature
#Action1 = prixAction1 = 7
#Action2 = Mage
#Action2 = prixAction2 = 4
#Action3 = Blast
#Action3 = prixAction3 = 6
#Action4 = Cristal
#Action4 = prixAction4 = 0
#Action5 = Mana

def __init__ (self,Mana):
    self.Mana=Mana


print (Tour1)
    
if Joueur1.getCarte() > Mana :
    choixcase = int(input("Quel action ? \n 1 = Mage  2 = Cristal   3 = Blast   4 = Créature   5 = Mana"))
    choixAction = int(input("1/ Mage     2/ Cristal      3/ Blast      4/ Créature    5/ Mana \n Que veux tu faire"))
    if choixAction == 1:
        Tour1[choixcase] = "1 Mage"
        Joueur1.Mana(4)
    elif choixAction == 2:
        Tour1[choixcase] = "1 Cristal"
        Joueur1.Mana(0)
    elif choixAction == 3:
        Tour1[choixcase] = "1 Blast"
        Joueur1.Mana(6)
    elif choixAction == 4:
        Tour1[choixcase] = "1 Créature"
        Joueur1.Mana(7)
    elif choixAction == 5:
        Tour1[choixcase] = print("Mana")


    print(Joueur1.getCarte())
print(Tour1)
