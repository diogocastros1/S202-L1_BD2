from database import Database


# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.145.115.200:7687", "neo4j", "field-planes-bunks")
db.drop_all()




# Fechando a conexão com o banco de dados
db.close()