
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

    def create_relacionando_player(self, numero_partida, nome_player, pontos):
        query = "MATCH (p:Player {name: $nome_player), (m:Match {numero_partida: $numero_partida}) CREATE (p)-[:PARTICIPOU{pontos: $pontos}]->(m)"
        parameters = {"numero": numero_partida, "name": nome_player, "pontos":pontos}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Players) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_match(self):
        query = "MATCH (a:Match)<-[part:PARTICIPOU]-(p:Player) RETURN a.name, p.name, part.pontos"
        results = self.db.execute_query(query)
        return [(result["a.name"], result["p.name"], result["part.pontos"]) for result in results]

    def update_professor(self, old_name, new_name):
        query = "MATCH (p:Professor {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_aluno_aula(self, aluno_name, aula_name):
        query = "MATCH (a:Aluno {name: $aluno_name}) MATCH (b:Aula {name: $aula_name}) CREATE (a)-[:ASSISTE]->(b)"
        parameters = {"aluno_name": aluno_name, "aula_name": aula_name}
        self.db.execute_query(query, parameters)
    
    def insert_professor_aula(self, professor_name, aula_name):
        query = "MATCH (a:Professor {name: $professor_name}) MATCH (b:Aula {name: $aula_name}) CREATE (a)-[:MINISTRA]->(b)"
        parameters = {"professor_name": professor_name, "aula_name": aula_name}
        self.db.execute_query(query, parameters)

    def delete_professor(self, name):
        query = "MATCH (p:Professor {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_aluno(self, name):
        query = "MATCH (a:Aluno {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_aula(self, name):
        query = "MATCH (a:Aula {name: $name})<-[:MINISTRA]-(p:Professor) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)