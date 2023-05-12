
class GamesDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, numero):
        query = "CREATE (:Match {numero: $numero})"
        parameters = {"numero": numero}
        self.db.execute_query(query, parameters)

    def create_relacionando_player(self, numero_partida, player, pontos):
        query = "MATCH (p:Player {name: $player}), (m:Match {numero: $numero_partida}) CREATE (p)-[:PARTICIPOU {pontos: $pontos}]->(m)"
        parameters = {"numero_partida": numero_partida, "player": player, "pontos":pontos}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self):
        query = "MATCH (a:Match)<-[part:PARTICIPOU]-(p:Player) RETURN a.numero, p.name, part.pontos"
        results = self.db.execute_query(query)
        return [(result["a.numero"], result["p.name"], result["part.pontos"]) for result in results]
    
    def get_match_espc(self, numero):
        query = "MATCH (a:Match{numero:$numero})<-[part:PARTICIPOU]-(p:Player) RETURN p.name, part.pontos"
        parameters = {"numero":numero}
        results = self.db.execute_query(query, parameters)
        return [(result["p.name"], result["part.pontos"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)