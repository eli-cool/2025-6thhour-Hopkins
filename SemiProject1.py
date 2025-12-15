#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: Semester Project 1

import random
import time

#Due to weird time travelling circumstances beyond explanation, you find yourself in 2018 or so
#working for Larian Studios. Currently, they are working on the early prototypes of the hype
#upcoming game "Baldur's Gate 3". BG3 is a game that uses the Dungeons & Dragons 5th edition rules
#as its framework for gameplay. You have been given a basic dictionary of some of the main hero
#characters and some of the enemies they may face, and are tasked with making an early prototype
#of one of the party members fighting against an enemy until one of them hits zero HP (dies).

partyDict = {
    "LaeZel" : {
        "HO" : 48,
        "Init" : 1,
        "AC" : 17,
        "AtkMod": 6,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 3
    },
    "Shadowheart" : {
        "HP" : 40,
        "Init" : 1,
        "AC" : 18,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 3,
    },
    "Gale" : {
        "HP" : 32,
        "Init" : 1,
        "AC" : 14,
        "AtkMod": 6,
        "Damage" : random.randint(1,10) + random.randint(1,10),
    },
    "Astarion" : {
        "HP" : 40,
        "Init" : 3,
        "AC" : 14,
        "AtkMod": 5,
        "Damage" : random.randint(1,8) + random.randint(1,6) + 4,
    }
}

enemyDict = {
    "Goblin" : {
        "HP" : 7,
        "Init" : 0,
        "AC" : 12,
        "AtkMod": 4,
        "Damage" : random.randint(1,6) + 2
    },
    "Orc": {
        "HP" : 15,
        "Init": 1,
        "AC" : 13,
        "AtkMod": 5,
        "Damage" : random.randint(1,12) + 3
    },
    "Troll": {
        "HP" : 84,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 4
    },
    "Mindflayer": {
        "HP" : 71,
        "Init": 1,
        "AC" : 15,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + 4
    },
    "Dragon": {
        "HP" : 127,
        "Init": 2,
        "AC" : 18,
        "AtkMod": 7,
        "Damage" : random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4
    },
}

#Combat consists of these steps:

#1. Rolling for 'initiative' to see who goes first. This is determined by rolling a
#20-sided die (d20) and adding their initiative modifier (If the roll is the same,
#assume the hero goes first).

hero = random.choice(list(partyDict.keys()))
villain = random.choice(list(enemyDict.keys()))

def attack(attacker_stats,attacker, atmod, victim,victim_stats):
    time.sleep(1)
    roll_attack = random.randint(0,20)
    attack_final = roll_attack + atmod
    print(attacker, "swings for", attack_final, victim, "dodges for", victim_stats["AC"])
    time.sleep(1)
    if attack_final < victim_stats["AC"]:
        print("swing and a miss")
        print(victim,"is now attacking",attacker)
        time.sleep(3)
        attack(victim_stats, victim, victim_stats["AtkMod"], attacker, attacker_stats)
    else:
        print("swing and a homerun!!")
        damage(attacker_stats,attacker, attacker_stats["Damage"], victim, victim_stats)

#DAMAGE HIT KILLIG PEOPLE DIE DIE DIE
def damage(attacker_stats,attacker, damage, victim, victim_stats):
    time.sleep(1)
    victim_stats["HP"] -= damage
    print(attacker,"deals",damage,"to",victim)
    print(victim,"now has",victim_stats["HP"],"hp")
    if victim_stats["HP"] <= 0:
        print(victim,"has",victim_stats["HP"],"hp","and dies")
        print(attacker,"wins with",attacker_stats["HP"],"hp")
    else:
        print(victim,"is now attacking",attacker)
        time.sleep(3)
        attack(victim_stats,victim, victim_stats["AtkMod"], attacker, attacker_stats)







print(hero, "is fighting the", villain)
time.sleep(1)
roll_initiative_h = random.randint(1,20)
roll_initiative_v = random.randint(1,20)
if roll_initiative_h >= roll_initiative_v:
    print("the hero is attacking")
    attack(partyDict[hero],hero,partyDict[hero]["AtkMod"],villain,enemyDict[villain])
else:
    print("the enemy is attacking")
    attack(enemyDict[villain],villain,enemyDict[villain]["AtkMod"],hero,partyDict[hero])


#2. Rolling to attack. This is determined by rolling a 20-sided die (d20) and adding their
#attack modifier. The attack hits if it matches or is higher than the target's Armor Class (AC).

#If the d20 rolled to attack is an unmodified ("natural") 20, the attack automatically hits and
#the character deals double damage. If the d20 rolled to attack is an unmodified ("natural") 1,
#the attack automatically misses




#3. If the attack hits, roll damage and subtract it from the target's hit points.

#4. The second in initiative rolls to attack (and rolls damage) afterwards.

#5. Repeat steps 2-5 until one of the characters is dead.

