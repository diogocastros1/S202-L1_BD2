# 1
~~~SQL
MATCH(:Dog)-[r]-(:Person) 
RETURN r;
~~~

# 2 
~~~SQL
MATCH (n:Person)-[:FAZ_PARTE]->(s:Serie)
WHERE n.sexo='F' AND s.nome='Scooby-Doo'
RETURN n
~~~

# 3
~~~SQL
MATCH (n:Person)-[:FAZ_PARTE{protagonista:false}]->(s:Serie)
WHERE (s)-[:PERTENCE]->(:Company{nome:'Walt Disney'})
RETURN n
~~~

# 4
~~~SQL
MATCH(c:Company) 
WHERE 'Pixar' IN c.subsidiarias
SET c.fundador='Walter Elias Disney'
RETURN c;
~~~