from database import Database
from school_database import SchoolDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://52.90.58.51:7687", "neo4j", "stoppering-million-perforation")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
school_db = SchoolDatabase(db)

# Criando alguns professores
school_db.create_professor("João")
school_db.create_professor("Maria")
school_db.create_professor("José")

# Criando alguns alunos
school_db.create_aluno("Ana")
school_db.create_aluno("Carlos")
school_db.create_aluno("Beatriz")

# Criando algumas aulas e suas relações com os professores
school_db.create_aula("Matemática", "João")
school_db.create_aula("Português", "Maria")
school_db.create_aula("História", "José")

# Atualizando o nome de um professor
school_db.update_professor("João", "Pedro")

school_db.insert_aluno_aula("Ana", "Matemática")
school_db.insert_aluno_aula("Ana", "Português")
school_db.insert_aluno_aula("Carlos", "História")
school_db.insert_aluno_aula("Beatriz", "História")


school_db.insert_professor_aula("Maria", "Matemática")
school_db.insert_professor_aula("José", "Português")
school_db.insert_professor_aula("José", "Matemática")

# Deletando um aluno e uma aula
school_db.delete_aluno("Beatriz")
school_db.delete_aula("História")

# Imprimindo todas as informações do banco de dados
print("Professores:")
print(school_db.get_professores())
print("Alunos:")
print(school_db.get_alunos())
print("Aulas:")
print(school_db.get_aulas())

# Fechando a conexão com o banco de dados
db.close()