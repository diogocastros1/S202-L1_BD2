# Questão 2

## 1
~~~SQL
CREATE(g:Game{titulo:'Uncharted 4',genero:'Aventura',ano:2016});
CREATE(g:Game{titulo:'Star Wars Jedi: Fallen Order',genero:'Aventura',ano:2019});
CREATE(g:Game{titulo:'Need For Speed: Heat',genero:'Corrida',ano:2019});
CREATE(g:Game{titulo:'Fortnite',genero:'FPS',ano:2017});
~~~

## 2
~~~SQL
CREATE(j:Jurado{nome:'John'});
CREATE(j:Jurado{nome:'Jane'});
CREATE(j:Jurado{nome:'Bill'});
~~~

## 3
~~~SQL
MATCH(j:Jurado{nome:'John'}),(g:Game{titulo:'Uncharted 4'})
CREATE(j)-[:JOGOU{nota:10, horas:80}]->(g);

MATCH(j:Jurado{nome:'Jane'}),(g:Game{titulo:'Star Wars Jedi: Fallen Order'})
CREATE(j)-[:JOGOU{nota:9, horas: 100}]->(g);

MATCH(j:Jurado{nome:'Bill'}),(g:Game{titulo:'Need For Speed: Heat'})
CREATE(j)-[:JOGOU{nota:8, horas: 156}]->(g);

MATCH(j:Jurado{nome:'John'}),(g:Game{titulo:'Fortnite'})
CREATE(j)-[:JOGOU{nota:7, horas: 1000}]->(g);
~~~