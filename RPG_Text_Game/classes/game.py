import random
from .magic import Spell

#Color codes that can be used with text to make it appear differently
# the ENDC code needs to be used at the end of each output to reset text back to normal font.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#represents the player
class Person:
    #Person class constructor
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.df = df
        self.max_mp = mp
        self.mp = mp
        self.magic = magic
        self.items = items
        self.action = ["Quick Attack", "Magic", "Items"]


    #get the player health
    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    #calculate the damage for a spell
    def generate_spell_damage(self, spell_index):
        magic_dmg_low = self.magic[spell_index]["dmg"] - 5
        magic_dmg_high = self.magic[spell_index]["dmg"] + 5
        return random.randrange(magic_dmg_low, magic_dmg_high)

    #subtract damaage from health
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, amt):
        self.hp += amt
        if self.hp>self.max_hp:
            self.hp = self.max_hp

    #get player hp
    def get_hp(self):
        return self.hp

    #get player max hp
    def get_max_hp(self):
        return self.max_hp

    #get player mp
    def get_mp(self):
        return self.mp

    #get player mp
    def get_max_mp(self):
        return self.max_mp

    #get the qty property of the item in the given items dictionary index
    def get_item_quantity(self, itemIndex):
        return self.items[itemIndex]["qty"]

    #reduce mp of player as result of casting a spell
    def reduce_mp(self, cost):
        self.mp -= cost

    #decrease the qty of the item with the given items dictionary index
    def remove_item(self, itemIndex):
        self.items[itemIndex]["qty"] -= 1

    def choose_action(self):
        index = 1
        print("\n" +self.name + "\nACTIONS")
        for act in self.action:
            print("    ",str(index) + ":" + act)
            index += 1

    def choose_magic(self):
        index = 1
        print("\n" + self.name + "\nMAGIC")
        for spell in self.magic:
            print("    ",str(index) + ":", spell.name, "(cost", str(spell.cost) + ")")
            index += 1

    def choose_items(self):
        index = 1
        print("\n" + self.name + "\nITEMS")
        for i in self.items:
            print("    ",str(index) + ":", i["item"].name,"(",i["item"].type,")",i["item"].description,"Qty x" + str(i["qty"]))
            index += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            #only want to allow targeting of dead enemies
            if(enemy.get_hp()>0):
                print("    " + str(i) + ": " + enemy.name)

            i += 1

        return int(input("Choose target: ")) - 1


    def get_stats(self):
        hpBar = ""
        hpBarTicks = (self.hp / self.max_hp) * 100 /4

        while hpBarTicks > 0:
            hpBar += "X"
            hpBarTicks -= 1

        while len(hpBar)<25:
            hpBar += " "

        mpBar = ""
        mpBarTicks = (self.mp / self.max_mp) * 100 / 10

        while mpBarTicks > 0:
            mpBar += "X"
            mpBarTicks -= 1

        while len(mpBar) < 10:
            mpBar += " "

        current_name = self.name

        if len(current_name) < 20:
            decreased = 20 - len(current_name)
            while decreased > 0:
                current_name += " "
                decreased -= 1


        hp_str = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_str) < 9:
            decreased = 9 - len(hp_str)
            while decreased>0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_str
        else:
            current_hp = hp_str

        mp_str = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_str) < 7:
            decreased = 7 - len(mp_str)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_str
        else:
            current_mp = mp_str

        print("                                ___________________________              ___________")
        print(bcolors.BOLD + current_name + current_hp +
              "   |" + bcolors.BOLD + bcolors.OKGREEN + hpBar + bcolors.ENDC + bcolors.BOLD +
              "|    " + current_mp + "   |" + bcolors.BOLD + bcolors.OKBLUE + mpBar +
              bcolors.ENDC + bcolors.BOLD + "|")

    def get_enemy_stats(self):

        current_name = self.name

        if len(current_name) < 20:
            decreased = 20 - len(current_name)
            while decreased > 0:
                current_name += " "
                decreased -= 1

        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 /2

        while bar_ticks > 0:
            hp_bar += "X"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_str = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_str) < 9:
            decreased = 9 - len(hp_str)
            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_str
        else:
            current_hp = hp_str

        print("                                ___________________________________________________")
        print(bcolors.BOLD + current_name + current_hp +
              "   |" + bcolors.BOLD + bcolors.FAIL + hp_bar + bcolors.ENDC + bcolors.BOLD + "|")

    def choose_enemy_spell(self,attempts):
        if attempts > 0:
            magic_choice = random.randrange(0, len(self.magic))
            spell = self.magic[magic_choice]
            spell_dmg = spell.generate_damage()

            if self.mp < spell.cost:
                self.choose_enemy_spell(attempts-1)
            else:
                return spell, spell_dmg
        else:
            return Spell("Harmless Static",0,0,"fail"), 0