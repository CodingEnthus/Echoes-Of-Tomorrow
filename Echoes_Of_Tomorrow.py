import random
artifacts = ["Eclipse Shard","Chrono Compass","Nova Gauntlet","Aetheric Lens","Tempest Blade","Oracle Orb","Eternal Ember","Whispering Amulet","Soulstone Talisman","Starfall Pendant"]

def negotiate():
    print("You decided to negotiate with the scavengers and gain safe passage but you lose one artifacts.")
    artifacts.pop(random.randint(0,9))
    print()
    print("The artifacts left are:",artifacts)
def sneakpeak():
    print("You decided to sneak peak but in the attempt to sneak peak, you were injured by the scavengers.")
def desert(live,food):
    print("You encounter a fierce sandstorm that threatens to bury you alive unless you find shelter or endure the harsh conditions. ")
    if(live>0 and food>30):
        survival_probability=0.9
    else:
        survival_probability=0.3
    random_number=random.random()
    if(random_number<survival_probability):
        print()
        print("you survived the strom")
        print()
        print("you are rewarded with a hidden artifact Phoenix Feather ")
        artifacts.append("Phoenix Feather")
    else:
        print()
        print("The strom overwelms you.")
        live=live-random.randint(0,live)
def forest(live):
    print("You have to Navigate through a treacherous maze of thorny vines and hidden traps to reach a cache of supplies guarded by territorial creatures.")
    navigation_choice=input("Navigate carefully or Brave the danger:")
    if(navigation_choice=="carefully"):
        print("You navigated the maze successfully....")
        
    elif(navigation_choice=="bravely"):
        live=live-random.randint(0,live)
        if(live==0):
            print("Your live is over.")
            return
        else:
            print("You navigated the maze but the obstacle in the path has caused you harm")
            print("Your remaining live is:",live)
            
def elemental_obelisk_riddles():
    # Generate random riddles related to elements
    riddles ="The more you take, the more you leave behind."

    # Display random riddle
    print("Elemental obelisk riddle:")
    print(riddles)
def ancient_glyph_cipher():
    # Generate random glyphs
    glyphs = ["A", "B", "C", "D", "E"]
    encrypted_message = ["A", "B", "C", "D", "E"]  # Replace with actual encrypted message
    key = {"A": "X", "B": "Y", "C": "Z", "D": "W", "E": "V"}  # Replace with actual decryption key

    decrypted_message = [key[g] for g in encrypted_message]
    print("Decrypted message:", "".join(decrypted_message))

print("Welcome to The Echoes Of Tomorrow\nYou are a wanderer, scouring the wastelands in search of resources and remnants of the old world. One day, you stumble upon an ancient artifact pointing towards the Oasis. Driven by curiosity and hope, you set out on a quest to find it, facing the unknown that lies ahead.")
print()
live=100
food=100

#Chapter 1: The Ruined City
print("You have 10 artifacts. They are Eclipse Shard: A crystal fragment said to contain the power of an ancient celestial event, rumored to unlock hidden knowledge")
print()
print("Chrono Compass: A mystical device that allows the bearer to manipulate time, guiding them through the dangers of the wasteland.")
print()
print("Nova Gauntlet: A legendary glove imbued with the energy of a dying star, granting its wearer incredible strength and resilience.")
print()
print("Aetheric Lens: A mystical lens that reveals hidden truths and pathways invisible to the naked eye.")
print()
print("Tempest Blade: A sword forged from the heart of a raging storm, capable of summoning lightning and controlling the elements.")
print()
print("Oracle Orb: A crystal sphere that grants visions of the past, present, and future, offering guidance to those who seek it.")
print()
print("Eternal Ember: A glowing ember that never extinguishes, said to hold the key to eternal life and vitality.")
print()
print("Whispering Amulet: An amulet that whispers secrets and prophecies to its bearer, guiding them on their journey.")
print()
print("Soulstone Talisman: A talisman crafted from the essence of fallen heroes, granting its wearer protection against dark forces.")
print()
print("Starfall Pendant: A pendant adorned with a fragment of a fallen star, believed to bring luck and fortune to its owner.")
print()
print()
print()
print("Chapter 1: THE RUINED CITY")
print("Your journey begins in the ruins of a once-great city, now home to dangerous scavengers and mysterious creatures.")
print()
print("YOu Encounter a group of hostile scavengers who demand a valuable artifact in exchange for safe passage through the city. ")
print()
print("Do you want to Negotiate with the scavengers, risking the loss of the artifact, or attempt to sneak past them, facing the possibility of a violent confrontation.")
print()
citychoice=input("Enter negotiate or sneak:")
if(citychoice=="negotiate"):
    negotiate()
elif(citychoice=="sneak"):
    sneakpeak()
    live=live-random.randint(0,100)
    if(live==0):
        print("You are Dead Game over.")
        
    else:
        print("Your remaining live is:",live)
else:
    print("enter a valid input")
if(live>0):

#Chapter 2
    print("CHAPTER 2: The Forgotten Forest or The Desert of Echoes")
    print("Forest Scenario: A dense forest has overtaken a suburban area, hiding both peril and sanctuary within its depths.")
    print()
    print("Desert Scenario: The desert holds the ruins of a military base with potential resources and hazards.")
    print()
    naturechoice=input("Do you want to explore the desert or the forest?:")
    if(naturechoice=="desert"):
        desert(live,food)
    elif(naturechoice=="forest"):
        forest(live)
    else:
        print("Invalid input")
else:
    print("You are dead. Game over")
if(live>0):
    #Chapter 3
    print("CHAPTER 3: THE CROSSROADS")
    print()
    print("You arrive at a crossroads, where you must choose the path that will lead you to the Oasis.")
    print()
    print("You  Encounter a group of nomadic traders who offer rare items in exchange for the artifact obtained in the Ruined City.")
    print()
    tradechoice=input("Yes or No")
    if(tradechoice=="Yes"):
        artifacts.remove("Phoenix Feather")
    elif(tradechoice=="No"):
        live-=10
else:
    print("You are dead. Game Over")
if(live>0):
    print()
    print("FINAL CHAPTER: THE JOURNEY OF OASIS")
    print()
    print("With the necessary knowledge and resources gathered, you face the final leg of your journey. The Oasis is close, but so are the forces that wish to keep its location a secret.")
    print()
    elemental_obelisk_riddles()
    ans=input("Enter answer:")
    if(ans=="footsteps"):
        print("Congratulations! You have been granted the access to OASIS. You have won the game.")
    else:
        print("You played amazingly but you couldn't make it this time. Hard Luck. Try again next time.")