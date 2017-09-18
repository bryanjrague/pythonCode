
import random

from RPG_Text_Game.classes.inventory import Item
from RPG_Text_Game.classes.game  import Person, bcolors
from RPG_Text_Game.classes.magic  import Spell

#enhancement ideas!
#TODO: log stats for battles for each player
#TODO: implement the ability to save progress for a battle, load character progress, stats, etc.
#TODO: add experience points and levels that increment when defeating enenmies, scale enemy difficulty
#TODO: have enemies drop items when defeated


#list of items
healPotion = Item("Healing Potion", "potion", "Heals 100 HP", 100)
greaterHealPotion = Item("Greater Healing Potion", "potion", "Heals 250 HP", 250)
superHealPotion = Item("Super Healing Potion", "potion", "Heals 350 HP", 350)
elixer = Item("Elixer", "elixer", "Fully Heals HP/MP of a single party member", 9999)
megaElixir = Item("MegaElixir", "elixer", "Fully restores party's HP/MP",9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)
magicPotion = Item("Magic Potion", "magic", "Revives 100 MP", 100)

#list of action dicstionaries
actions = []

#list of valid spells that player and enemy can use
fireball = Spell("Fireball", 55, 250, "Black Magic")
lightning = Spell("Lightning", 40, 205, "Black Magic")
blizzard = Spell("Blizzard", 30, 150, "Black Magic")
meteor = Spell("Meteor", 60, 300, "Black Magic")
cure = Spell("Cure", 20, 250, "White Magic")

#instantiate player and enemy with items and magic

mage_magic = [fireball,lightning,cure,blizzard]
rogue_magic = [cure,meteor,lightning]
cat_magic = [blizzard,lightning]
mage_items = [{"item": healPotion,"qty":2},
              {"item": magicPotion,"qty":3},
              {"item": greaterHealPotion,"qty":1},
              {"item": megaElixir, "qty":1}]

rogue_items = [{"item": superHealPotion,"qty":2},
              {"item": grenade, "qty":1}]

cat_items = [{"item": greaterHealPotion,"qty":3},
             {"item": magicPotion, "qty":2}]

enemy_boss_magic = [fireball, meteor]
enemy_boss_items = [{"item": superHealPotion,"qty":1}]
enemy_imp_magic = [lightning]
enemy_imp_items = [{"item":healPotion,"qty":1}]

player1 = Person("Mage", 500, 205, 60, 30, mage_magic, mage_items)
player2 = Person("Rogue", 500, 65, 110, 100, rogue_magic, rogue_items)
player3 = Person("Steve The Cat", 500, 85, 90, 70, cat_magic, cat_items)

enemy1 = Person("Magmaximus", 2000, 415, 195, 25, enemy_boss_magic, enemy_boss_items)
enemy2 = Person("Lava Imp", 400, 100, 100, 15, enemy_imp_magic, enemy_imp_items)
enemy3 = Person("Lava Imp", 400, 100, 100, 15, enemy_imp_magic, enemy_imp_items)

#instantiate list of players
players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

#game continues looping until this control flag is False
running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

#loop for as long as the game is valid.
while running:

    validPlayerChoice = False

    print("============================")
    print("NAME                              HP                                     MP")
    for player in players:
        player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats()

    #each alive player gets a chance to attack, use magic, or use an item
    for player in players:
        print(bcolors.UNDERLINE + "\n *** Next Turn = " + player.name + bcolors.ENDC)
        player.choose_action()
        action_choice = int(input("Choose action: ")) - 1

        #attack for damage using player damage stats
        if action_choice == 0:
            dmg = player.generate_damage()
            enemy_idx = player.choose_target(enemies)
            enemies[enemy_idx].take_damage(dmg)
            print(bcolors.OKGREEN + player.name + " attacks",enemies[enemy_idx].name,
                  "and deals",dmg,"points of damage." + bcolors.ENDC)
            validPlayerChoice = True

            if enemies[enemy_idx].get_hp()<=0:
                print(bcolors.FAIL + bcolors.BOLD + str(enemies[enemy_idx].name) + " has died!")
                del enemies[enemy_idx]

        #use a spell
        elif action_choice == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            #verify magic choice is valid
            if (magic_choice>=0 and magic_choice<len(player.magic)):
                validPlayerChoice = True
                spellName = player.magic[magic_choice].name
                spellCost = player.magic[magic_choice].cost
                spellType = player.magic[magic_choice].type
                print("You chose", spellName, "with cost",spellCost)

                current_mp = player.get_mp()

                #check if player has enough mp
                if spellCost <= current_mp:
                    dmg = player.magic[magic_choice].generate_damage()

                    #heal or deal damage based on spell type
                    if spellType=="White Magic":
                        player.heal(dmg)
                        print(bcolors.OKBLUE + player.name + "'s spell", spellName, "revives", dmg,
                              "points HP." + bcolors.ENDC)
                    else:
                        enemy_idx = player.choose_target(enemies)
                        enemies[enemy_idx].take_damage(dmg)
                        print(bcolors.OKBLUE + player.name + "'s spell", spellName, "causes", dmg,
                              "points of damage to",enemies[enemy_idx].name," ." + bcolors.ENDC)

                        if enemies[enemy_idx].get_hp() <= 0:
                            print(bcolors.FAIL + bcolors.BOLD + str(enemies[enemy_idx].name) + " has died!")
                            del enemies[enemy_idx]
                    #reduce mp due to cost of spell
                    player.reduce_mp(spellCost)

                #spell fails if not enough mp
                else:
                    print(bcolors.FAIL + player.name + " does not have enough MP!:",current_mp,"The spell fails!" + bcolors.ENDC)
                    validPlayerChoice = True
            else:
                validPlayerChoice = False

        #get an item and implement it
        elif action_choice == 2:
            player.choose_items()
            item_choice = int(input("Choose item: ")) - 1

            #option to return to the main action menu
            if item_choice == -1:
                continue
            #use the item selected
            elif item_choice>=0 and item_choice<len(player.items):
                item = player.items[item_choice]["item"]
                if player.get_item_quantity(item_choice)>0:
                    validPlayerChoice = True

                    if item.type == "potion":
                        player.heal(item.prop)
                        print(bcolors.OKGREEN + "\n" + item.name + " heals for",str(item.prop), "HP" + bcolors.ENDC)
                    elif item.type == "magic":
                        player.heal(item.prop)
                        print(bcolors.OKGREEN + "\n" + item.name + " revives ", str(item.prop), "MP" + bcolors.ENDC)
                    elif item.type == "elixer":
                        if item.name == "MegaElixir":
                            for i in players:
                                i.hp = player.max_hp
                                i.mp = player.max_mp
                        else:
                            player.hp = player.max_hp
                            player.mp = player.max_mp
                            print(bcolors.OKGREEN + "\n" + item.name + " fully restores player MP and HP" + bcolors.ENDC)
                    elif item.type == "attack":
                        enemy_idx = player.choose_target(enemies)
                        enemies[enemy_idx].take_damage(item.prop)

                        enemies[enemy_idx].take_damage(item.prop)
                        print(bcolors.OKBLUE + "\n" + item.name + " deals ", item.prop,
                              "points of damage to",enemies[enemy_idx].name,"." + bcolors.ENDC)

                        if enemies[enemy_idx].get_hp() <= 0:
                            print(bcolors.FAIL + bcolors.BOLD + str(enemies[enemy_idx].name) + " has died!")
                            del enemies[enemy_idx]

                    player.remove_item(item_choice)
                else:
                    print(bcolors.BOLD + "You do not have any",item.name,"left to use.")
                    validPlayerChoice = False

            #invlaid choice, show error message and go back to menu
            else:
                validPlayerChoice = False

        #incorrect option causes for turn to be lost
        if validPlayerChoice == False:
            print(bcolors.BOLD + player.name + " tries to do something unknown and does nothing!" + bcolors.ENDC)

        #check if there are still enemies alive
        if(len(enemies)<=0):
            break


    #count the number of defeated enemies so we know if we have won.
    defeated_enemies = 0
    for e in enemies:
        if e.get_hp() == 0:
            defeated_enemies +=1

    # count the number of defeated players so we know if we have lost
    defeated_players = 0
    for p in players:
        if p.get_hp() == 0:
            defeated_players += 1

    #check the hp of player and enemy, end the game if all players are dead.
    if defeated_enemies == len(enemies):
        print(bcolors.OKGREEN + bcolors.BOLD + "*** All enemies defeated! You win! ***" + bcolors.ENDC)
        running = False
        continue


    if defeated_players == len(players):
        print(bcolors.FAIL + bcolors.BOLD + "*** All players have died! You lose! ***" + bcolors.ENDC)
        running = False
        continue

    # if battle is still going on, each enemy chooses player, attacks and deals damage
    for e in enemies:
        # if enemy is low health, they will consider using health potion
        if e.get_hp() <= (e.get_max_hp() * 0.30):
            itemCount = 0
            for i in e.items:
                if i["item"].type == "potion":
                    chance = random.randrange(1, 101)
                    if chance > 60:
                        e.heal(i["item"].prop)
                        print(bcolors.FAIL + bcolors.BOLD + e.name + " uses " + i["item"].name + " and heals " + str(i["item"].prop))
                        e.remove_item(itemCount)
                        # enemy uses turn healing
                        continue
                itemCount += 1

        # else enemy chooses attack and who to attack
        enemy_choice = random.randrange(0,2)
        enemy_target = random.randrange(0, len(players))
        #enemy quick attack
        if enemy_choice == 0:
            enemy_dmg = enemies[0].generate_damage()
            players[enemy_target].take_damage(enemy_dmg)
            print(bcolors.FAIL + e.name, "attacks", players[enemy_target].name, "for",
                  str(enemy_dmg) + bcolors.ENDC)
        #enemy magick attack
        elif enemy_choice == 1:
            #enemy will attempt to get a spell working within X tries
            spell, spell_dmg = e.choose_enemy_spell(10)
            players[enemy_target].take_damage(spell_dmg)
            e.reduce_mp(spell.cost)
            print(bcolors.FAIL + bcolors.BOLD + e.name,"uses",spell.name,"against",players[enemy_target].name,"and causes",
                  spell_dmg,"damage!" + bcolors.ENDC)

        # alert if a player has died.
        if players[enemy_target].get_hp() <= 0:
            print(bcolors.WARNING + bcolors.BOLD + players[enemy_target].name + " is dead!" + bcolors.ENDC)
            del players[enemy_target]