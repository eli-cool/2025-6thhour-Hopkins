#Name: Eli Hopkins
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

chars = {
    "enemy1": {
        "name":"pitbull named princess",
        "DMG":10,
        "HP":10,
        "AC":3,
    },
    "enemy2": {
        "name":"rodent",
        "DMG":5,
        "HP":24,
        "AC":3,
    },
    "enemy3": {
        "name":"Ally",
        "DMG":17,
        "HP":2007,
        "AC":5,
    },
    "enemy4": {
        "name":"the sun",
        "DMG":2000,
        "HP":25,
        "AC":0,
        #take it out as fast as you can
    },
    "enemy5": {
        "name":"skeleton zombie vampire",
        "DMG":0,
        "HP":1,
        "AC":0,
        #it's just a dead guy
    }
}
chars["enemy1"].update({dmg:"int(input("enemy 1's damage: ")})
chars["enemy2"]["DMG"] = int(input("enemy 2's damage: "))
chars["enemy3"]["DMG"] = int(input("enemy 3's damage: "))
chars["enemy4"]["DMG"] = int(input("enemy 4's damage: "))
chars["enemy5"]["DMG"] = int(input("enemy 5's damage: "))
print(chars)
#It is up to you to decide what properties are important and the theme of the game.
