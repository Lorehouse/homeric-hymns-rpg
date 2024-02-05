
def intro(P1):
    print("You have arrived at the cost from your home in the hills. \nFor the entirety of your life (βίος) you have lived in a rough hut with your adoptive father and mother. \nToday you are of age, and setting out to seek your fortune across the seas.")
    #draw a picture of a Greek seaport here
    print("As you near the docks of the small fishing town near which you grew up, a weather-beaten man with wise eyes approaches \nHe speaks to your father, saying, 'The ναῦς is ready for your son and we are prepared to depart today.' When he says 'ναῦς', he motions to a small sailing ship.") 
    #draw a picture of the Uluburun Shipwreck recreation
    print("It is a merchant-style ship with low walls around a deck that contains some crates and ἀμφορεύς. /nThese ἀμφορεύς are of a rust-colored clay and lay stacked on their sides as they do not have a flat bottom on which to stand.")
    #draw a picture of the amphorae here

class Player:
    def __init__(self, name, weapon, strength, ἀσπίς):
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.shield = ἀσπίς

def create_player():
    name = input("It is time to create your character. \n Enter your character's name: ")
    weapon = input("In your life as a humble shepherd in the hills, \nyou have developed proficiency in fighting off wild animals and robbers with a weapon. \nPlease choose from the following weapons: ξίφος (a sword), or δόρυ (a spear).")

intro()