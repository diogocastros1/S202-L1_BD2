from database import Database
from family_database import FamilyDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.239.113.213:7687", "neo4j", "losses-tap-mile")

# Instanciando a classe GamesDatabase
fd = FamilyDatabase(db)

i = 1

print('\n' * 100)
while(i):
    i = input('O que deseja fazer? \n1 - para ver todas as pessoas \n2 - para buscar um relacionamento \n0 - para sair \n')

    if(i=='1'):
        print('Pessoas da familia')
        print(fd.get_pessoas())
    
    if(i=='2'):
        n = input('Digite o nome de uma das pessoas que deseja analisar o relacionamento:\n')
        r = input('Digite um dos relacionamentos disponiveis são: \nCASADO_COM \nDONO_DE \nGENRO_DE \nNORA_DE \nMAE_DE \nPAI_DE \n')
        print(fd.get_relacionamento(n,r))
    
    if(i=='0'):
        print('Bye! ;)')
        break
# Fechando a conexão com o banco de dados
db.close()