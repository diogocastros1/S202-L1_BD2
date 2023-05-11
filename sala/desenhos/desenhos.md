# Deletar relacionamento de um nó
~~~SQL
MATCH(:Dog{nome:'Pateta'})-[fp:FAZ_PARTE]->()
DELETE fp;
~~~

# Para Atualizar/Adicionar
~~~SQL
MATCH(d:Dog{nome:'Pateta'})
SET d.nome_filho = 'Max'
~~~