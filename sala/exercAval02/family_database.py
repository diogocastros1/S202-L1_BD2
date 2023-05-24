
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
