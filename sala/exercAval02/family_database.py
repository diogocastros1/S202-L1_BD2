
class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    def get_pessoas(self):
        query = "MATCH (p:Pessoa) RETURN p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_relacionamento(self, nome, relacionamento):
        query = "MATCH p=(a:Pessoa{nome: $nome})-[r:`%s`]-(b) RETURN a.nome, b.nome, r"
        formatted_query = query % relacionamento
        parameters = {"nome": nome}
        results = self.db.execute_query(formatted_query, parameters)
        return [(result["a.nome"], relacionamento, result["b.nome"]) for result in results]

    # def get_match_espc(self, numero):
    #     query = "MATCH (a:Match{numero:$numero})<-[part:PARTICIPOU]-(p:Player) RETURN p.name, part.pontos"
    #     parameters = {"numero": numero}
    #     results = self.db.execute_query(query, parameters)
    #     return [(result["p.name"], result["part.pontos"]) for result in results]

    # def update_player(self, old_name, new_name):
    #     query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
    #     parameters = {"old_name": old_name, "new_name": new_name}
    #     self.db.execute_query(query, parameters)

    # def delete_player(self, name):
    #     query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
    #     parameters = {"name": name}
    #     self.db.execute_query(query, parameters)
