from dataclasses import dataclass
@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float
spark = Creature("Spark", "Dragon", 5, 80.0)
frost = Creature("Frost", "Wolf", 3, 65.5)
moss = Creature("Moss", "Slime", 2, 40.0)
creatures = [spark, frost, moss]

print("Name, Species, Level, Health")
for creature in creatures:
    print(creature.name, creature.species, creature.level, creature.health, sep=", ")
spark.level = 6
spark.health = 90.0
print("After updating Spark:")
for creature in creatures:
    print(creature.name, creature.species, creature.level, creature.health, sep=", ")