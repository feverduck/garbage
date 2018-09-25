#picking class
pick_class = input("What class are you wanting to play? ")
#lowercasing class for simplicity
pick_class = pick_class.lower()
#actually assigning the class
if pick_class == 'warrior':
    equipped = {
        "weapon" : "Rusty Sword",
        "gold" : 50,
        "armour" : "Mail Armour"
    }
elif pick_class == 'mage':
    equipped = {
        "weapon" : "Beaten Staff",
        "gold" : 50,
        "armour" : "Cloth Armour"
    }
elif pick_class == 'archer':
    equipped = {
        "weapon" : "Warped Bow",
        "gold" : 50,
        "armour" : "Leather Armour"
    }
else:
    print("Sorry we don't have support for that yet.")
#testing if this works
#print(equipped["weapon"])
#print(equipped["gold"])
#print(equipped["armour"])
