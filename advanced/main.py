name = input("Enter your creature's name: ")
species = input("Enter its species: ")
while True:
    try:
        level = int(input("Enter its level: "))
        if level >= 0:
            break
        print("Level must be 0 or higher.")
    except ValueError:
        print("Enter a whole number, like 5.")
while True:
    try:
        health = float(input("Enter its health: "))
        if -float("inf") < health < float("inf"):
            break
        print("Health must be a finite number.")
    except ValueError:
        print("Enter a number, like 60 or 60.5.")
new_creature = Creature(name, species, level, health)
print("Your creature:")
print("Name:", new_creature.name)
print("Species:", new_creature.species)
print("Level:", new_creature.level)
print("Health:", new_creature.health)