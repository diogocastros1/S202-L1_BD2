from database import Database
from teacher_crud import TeacherCRUD, TeacherCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.239.113.213:7687", "neo4j", "losses-tap-mile")


# Instanciando a classe GamesDatabase
tc = TeacherCLI(db)

# tc.create_teacher('Chris Lima', 1956, '186.052.396-66')

# print(tc.get_teacher('Chris Lima'))

# tc.update_cpf_teacher('Chris Lima', '162.052.777-77')

# print(tc.get_teacher('Chris Lima'))

tc.menu()

# Fechando conexão
db.close()