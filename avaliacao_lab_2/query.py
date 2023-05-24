# ## Questão 01

# 1. Busque pelo professor `“Teacher”` cujo nome seja **“Renzo”**, retorne o **ano_nasc** e o **CPF**.
# 2. Busque pelos professores `“Teacher”` cujo nome comece com a letra **“M”**, retorne o **name** e o **cpf**.
# 3. Busque pelos nomes de todas as cidades `“City”` e retorne-os.
# 4. Busque pelas escolas `“School”`, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.

# ## Questão 02

# 1. Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
# 2. Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade **“population”**.
# 3. Encontre a cidade cujo **CEP** seja igual a **“37540-000”** e retorne o nome com todas as letras **“a”** substituídas por **“A”** .
# 4. Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do
# nome.


from database import Database

db = Database("bolt://34.239.113.213:7687", "neo4j", "losses-tap-mile")


# Q1 - a)
query = "MATCH(t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf;"
print(db.execute_query(query))

# Q1 - b)
query = "MATCH(t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS Nome, t.cpf AS CPF;"
print(db.execute_query(query))

# Q1 - c)
query = "MATCH(c:City) RETURN c.name AS Nome;"
print(db.execute_query(query))

# Q1 - d)
query = "MATCH(s:School) WHERE s.number >= 150 AND s.number <= 550  RETURN s.name AS Nome, s.address AS Endereco, s.number AS Num;"
print(db.execute_query(query))

# Q2 - a)
query = "MATCH(t:Teacher) RETURN MAX(t.ano_nasc) AS Mais_Novo, MIN(t.ano_nasc) AS Mais_Velho;"
print(db.execute_query(query))

# Q2 - b)
query = "MATCH (n:City) RETURN AVG(n.population)"
print(db.execute_query(query))

# Q2 - c)
query = "MATCH (n:City{cep:'37540-000'}) RETURN REPLACE(toUpper(n.name), 'a', 'A') AS nome"
print(db.execute_query(query))

# Q2 - d)
query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS caractere"
print(db.execute_query(query))

db.close()