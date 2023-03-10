from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

tipos = ["Grass", "Poison"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })

fraquezas = ["Psychic", "Ice"]
pokemons = db.collection.find({"weaknesses": {"$all": fraquezas}})

writeAJson(pokemons, "pokemons")

def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")

def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})

types = ["Fighting"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_by_type")