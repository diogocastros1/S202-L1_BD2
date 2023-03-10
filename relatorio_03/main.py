from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

tipos = ["Grass", "Poison"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })


writeAJson(pokemons, "pokemons")
