#Classes: Mage, Warrior, Archer
#Start For Mage: Beaten Staff, 50g, Cloth Armour
#Start For Warrior: Rusty Sword, 50g, Mail Armour
#Start For Archer: Warped Bow, 50g, Leather Armour

mage_equipped = {
    "weapon" : "Beaten Staff",
    "gold" : 50,
    "armour" : "Cloth Armour"
}

print(mage_equipped["weapon"])
print(mage_equipped["gold"])
print(mage_equipped["armour"])

#First gold pickup
mage_equipped["gold"] = mage_equipped["gold"] + 15

print(mage_equipped["gold"])

