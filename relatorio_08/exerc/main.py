from database import Database
from games_database import GamesDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://52.90.58.51:7687", "neo4j", "stoppering-million-perforation")
db.drop_all()

# Instanciando a classe GamesDatabase
gd = GamesDatabase(db)

# Criando alguns jogadores
gd.create_player('Monica')
gd.create_player('Joey')
gd.create_player('Ross')
gd.create_player('Rachel')

# Criando Partidas
gd.create_match(1)
gd.create_match(2)
gd.create_match(3)

# Relacionando jogadores as partidas
gd.create_relacionando_player(1,'Monica',7)
gd.create_relacionando_player(1,'Rachel',9)
gd.create_relacionando_player(2,'Rachel',10)
gd.create_relacionando_player(2,'Ross',10)
gd.create_relacionando_player(2,'Ross',7)
gd.create_relacionando_player(3,'Monica',10)
gd.create_relacionando_player(3,'Joey',10)

# Fechando a conexão com o banco de dados
db.close()