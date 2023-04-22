# Questão 1
## 1) 
`MATCH(n) RETURN n;`

## 2) 
`MATCH(g:Game) WHERE g.ano > 2012 RETURN g;`

## 3)
`MATCH(g:Game) WHERE g.genero = "Terror" RETURN g;`

## 4)
~~~
MATCH (n) 
WHERE n.nota >= 7
RETURN DISTINCT "node" as entity, n.nota AS nota
UNION ALL 
MATCH ()-[r]-() 
WHERE r.nota >=7
RETURN DISTINCT "relationship" AS entity, r.nota AS nota;
~~~