from random import randint
from random import choice

player1 = None
#make class where you can build your abilities. Make different powers and strengthen them.

class BuildPlayer:
        
    def __init__(self, name):
        self.name = name
        self.health = 5
        self.stamina = 10
        self.fireability = False
        self.strength = 0
        self.staminamax = 20
        
    def learn_fire_magic(self):
        self.magic_fire = 0
        self.fire_resistance = 0
        self.stamina -= 10
        self.fireability = True
        
        
    def ability_health(self):
        gain = randint(1,3)
        self.health += gain
        if self == player1:
            print(f"You gained {gain} extra health.")


    def strength_points(self):
        gain = randint(1,3)
        self.strength += gain
        if self == player1:
            print(f"You gained {gain} strength")


    def round_gain(self):
        if self.stamina >= (self.staminamax * 0.5):
            self.health += 1
        if self.stamina >= (self.staminamax * 0.75):
            self.strength +=1
        if self.stamina < self.staminamax:
            self.stamina += 1
        
        
    def rest(self):
        gain = randint(3, 5)
        self.stamina += gain
        if self == player1:
            print(f"You rested and gained {gain} stamina.")


    def ability_magic_fire(self):
        try:
            gainpower = randint(1,3)
            gainresistance = randint(0,1)
            self.magic_fire += gainpower
            self.stamina -= 2
            if self == player1:
                print(f"You gained {gainpower} fire magic power.")
            if gainresistance == 1:
                self.fire_resistance += gainresistance
                if self == player1:
                    print("You also gained 1 fire resistance.")
        except:
            print("You have not learned fire magic yet.")



#make class where you can buy and own land to grow different products that either can be sold for money or used to strenghthen abilities.


#make class for a pet companion that can learn powers and build strength.


def main_menu(menu):
    print()
    print("Check (S)tatus")
    print("(R)est")
    if player1.stamina > 1:
        print("(L)earn new ability")
        print("(T)rain abilities/powers")
        print("(B)attle")
    print("(Q)uit game")

    

def learn_menu(menu):
    print()
    print("The abilities below are available:")
    if player1.fireability == False:
        print("(F)ire magic - 10 stamina points")
    else:
        print("No available abilities at the moment.")
    print("(B)ack")
    



def train_menu(menu):
    print()
    print("*** The training fileds ***")
    print()
    print("You have the following powers available:")
    print("(S)trength")
    print("(H)ealth")
    if player1.fireability:
        print("(F)ire Magic")
        
    print("(B)ack to previous menu")

        
        
def status():
    print(f"\nStatus for {player1.name}:")
    print(f"Health: {player1.health}")
    print(f"Stamina: {player1.stamina}")
    print(f"Strength: {player1.strength}")
    try:
        print(f"Fire Magic: {player1.magic_fire}")
        print(f"Fire Resistance: {player1.fire_resistance}")
    except:
        pass
        

def user_prompt(menu, compturn):
    
    action = input("\nWhat do you want to do?\n").lower()


    ##main menu prompts
    

    if action == "r" and menu == "main":
        if player1.stamina <= (player1.staminamax * 0.7):
            player1.rest()
            player1.round_gain()
            compturn = True
        else:
            print("Your stamina is above 13, you are unable to rest.")

    elif action == "s" and menu == "main":
        status()
        ai_status()
        
    elif action == "l" and menu == "main" and player1.stamina > 1:
        menu = "learn"
    
    elif action == "t" and menu == "main":
        menu = "train"
        
    elif action == "b" and menu == "main":
        defender = choose_oponent()
        battle_main(player1, defender)
    
    elif action == "q" and menu == "main":
        print(f"Thank you for playing {player1.name}.")
        quit()
    
    # Train menu valid prompts:
    
    elif action == "f" and menu == "train" and player1.fireability:
        player1.ability_magic_fire()
        player1.round_gain()
        compturn = True
        
    elif action == "s" and menu == "train":
        player1.strength_points()
        player1.round_gain()
        compturn = True
    
    elif action == "h" and menu == "train":
        player1.ability_health()
        player1.round_gain()
        print(f"Your health is now {player1.health}.")
        compturn = True

    elif action == "b" and menu == "train":
        menu = "main"
        
    # Learn menu valid prompts:
        
    elif action == "f" and menu == "learn" and not player1.fireability:
        if player1.stamina > 12:
            player1.learn_fire_magic()
            player1.round_gain()
            print("You learned Fire Magic!")
            compturn = True
        else:
            print("Sorry, your stamina needs to be 13 or more to learn new abilities.")
    
    elif action == "b" and menu == "learn":
        menu = "main"
        
    else:
        print("Not a valid choice.")
        
    
    return menu, compturn
    

def create_new_ai_player(ai_list):
    name1 = ["Crazy", "Grose",  "Humble", "Big", "One-eyed", "Tall", "Short"]
    name2 = ["Joe", "Jane", "Jack", "Lily", "Ron", "Fury"]
    while True:
        name = choice(name1) + "-" + choice(name2)
        if name not in ai_list:
            
            print(f"\nSPY REPORT: Rumor says a new player\ncalled {name} have been spotted\nin the area.")
            name = BuildPlayer(name)
            ai_list.append(name)
            break
    
    return ai_list
    

def ai_player_move(ai_list):
    print("AI makes a move...")
    for i in ai_list:
        while True:
            ai_choice = randint(1,5)
            if i.stamina < 2:
                i.rest()
                break
            elif ai_choice == 1 and i.stamina > (i.staminamax * 0.7) and i.fireability == False:
                i.learn_fire_magic()
                i.round_gain()
                break
            
            elif ai_choice == 2:
                i.ability_health()
                i.round_gain()
                break
                
            elif ai_choice == 3:
                i.strength_points()
                i.round_gain()
                break
                
            elif ai_choice == 4 and i.stamina <= (i.staminamax * 0.7):
                i.rest()
                i.round_gain()
                break
                
            elif ai_choice == 5 and i.fireability:
                i.ability_magic_fire()
                i.round_gain()
                break
    
    
def ai_status():
    for i in ai_list:
        print()
        print(f"Status for AI {i.name}:")
        print(f"Health: {i.health}")
        print(f"Stamina: {i.stamina}")
        print(f"Strength: {i.strength}")
        try:
            print(f"Fire Magic: {i.magic_fire}")
            print(f"Fire Resistance: {i.fire_resistance}")
        except:
            pass
            
    
    # ****** BATTLE PART *****
    

def choose_oponent():
    
    print("Who do you want to fight?")
    count = 0
    for i in ai_list:
        count += 1
        print(f"{count}: {i.name}")
    
    while True:
        try:
            index = int(input("Choose number: "))

            if count >= index > 0:
                defender = ai_list[index-1]
                
                return defender
            else:
                print("invalid choice")
        except:
            print("invalid choice")
        

#def make_battle(index):
    
#    starter = randint(1,2)
#    print()
    
#    if starter == 1:
#        print(f"{player1.name} starts!")
#    else:
#        print(f"{ai_list[index].name} starts!")
    

def battle_menu():
    
    print("*** BATTLE FIELDS ***")
    print("A - Attack")
    print("R - Shield and rest")
    if player1.fireability and player1.stamina > 9:
        print("F - Fire attack")
    print("S - Analyze oponents status")
    print("W - Withdraw")
    
    
def regular_attack(attacker, defender):
    aatt = attacker.strength
    dhea = defender.health
    dsta = defender.stamina
    aatt *= ((randint(2,8))/12)
    aatt = max(int(aatt),1)
    
    dhealthloss = max(0,(aatt - int(dsta/4))-1)
    attacker.stamina -= 1
    defender.health -= dhealthloss

    
    
    
    
def make_battle(attacker, defender):
    while True:
    
        if attacker == player1:
            move = input("What is your move? ").lower()

        else:
            move = choice(["a", "r", "f"])

        if move == "a":
            print(f"{attacker.name} attacks!")
            regular_attack(attacker, defender)
            return False
            
        elif move == "r":
            print(f"{attacker.name} shields and rests")
            return False
            
        elif move == "f" and attacker.fireability and attacker.stamina > 9:
            print(f"{attacker.name} uses fire attack!")
            return False
            
        elif move == "s":
            print("Spying...")
            return False
            
        elif move == "w":
            print("Withdrawing...")
            return True
            
        else:
            print("No valid input...")

        


def battle_main(attacker, defender = player1):
    print()
    print(f"Attacker: {attacker.name}\nDefender: {defender.name}")
    print()
    if attacker == player1:
        while True:
            battle_menu()
            print()
            withdraw = make_battle(attacker, defender)
            
            if defender.health <= 0:
                print(f"{defender.name} died. You won!")
                battle_gain(defender)
                ai_list.remove(defender)
                return True
            
            if withdraw:
                break
            print()
    

def battle_gain(defender):
    gainstrength = int(defender.strength * (1 /(randint(3,8))))
    gainstaminamax = (int((defender.staminamax) / 10) -1)
    gainstaminamax = max(0, gainstaminamax)
    
    player1.staminamax += gainstaminamax
    player1.strength += gainstrength
    print(f"Your stamina max increased by {gainstaminamax}")
    print(f"Your strength increased by {gainstrength}")
    if player1.fireability and defender.fireability:
        gainfirestr = int(round((defender.magic_fire * (1 / randint(5,10))),0))
        gainfireres = int(round((defender.fire_resistance * (1 / randint(5,10))),0))

        if gainfirestr > 0:
            print(f"You gained {gainfirestr} fire magic power.")
            player1.magic_fire += gainfirestr
        
        if gainfireres > 0:
            print(f"You gained {gainfireres} fire magic power.")
            player1.fire_resistance += gainfireres

#Make spy option


#GAME MAIN BELOW!


player1 = BuildPlayer(input("What is your player name?\n"))

print(f"\n ** Welcome to the game {player1.name}! **")

print(" *** Below are some initial rules ***")
print("\nEach round your strenght will grow by 1\nas long as your stamina is 75% or more.")
print("\nYour health will grow by 1 as long\nas your stamina is 50% or more.")
print("\nYour stamina will grow by 1 each round\nto a initial maximum of 20, if your\nstamina drops below 2 you need to rest.\nYou can't rest if your stamina\nis above 70% of full strength.")
print()

menu = "main"
compturn = False
global ai_list
ai_list = []

create_new_ai_player(ai_list)

while True:
    if menu == "main":
        main_menu(menu)
    elif menu == "train":
        train_menu(menu)
    elif menu == "learn":
        learn_menu(menu)
    menu, compturn = user_prompt(menu, compturn)
    
    if compturn:
        print()
        ai_player_move(ai_list)
        compturn = False
        if randint(1,20) == 1:
            create_new_ai_player(ai_list)
    
    
    
    


            

