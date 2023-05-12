from database import Database
from games_database import GamesDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.239.53.11:7687", "neo4j", "thing-flanges-rust")
db.drop_all()

# Instanciando a classe GamesDatabase
gd = GamesDatabase(db)

# Criando alguns jogadores
gd.create_player('Monica')
gd.create_player('Xandler')
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
gd.create_relacionando_player(3,'Ross',7)
gd.create_relacionando_player(3,'Monica',10)
gd.create_relacionando_player(3,'Xandler',5)

# Requisitando Informações
print(f'Jogadores \n{gd.get_players()}\n')
print(f'Numero da partida, Nome e Pontuação \n{gd.get_match()}\n')
print(f'Competidores e pontuação \n{gd.get_match_espc(1)}\n')

# Atualização do nome do jogador
gd.update_player('Ross', 'Joey')
print(f'Jogadores atualizados \n{gd.get_players()}\n')

# Deletando jogador
gd.delete_player('Xandler')
print(f'Jogadores atualizados \n{gd.get_players()}\n')

# Fechando a conexão com o banco de dados
db.close()