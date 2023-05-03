# Criando Bandas, Albuns e Músicas
~~~SQL
CREATE(:Banda{nome:'Metalica', ano:1981, estilo:'Heavy Metal'});
CREATE(:Album{nome:'Black Album', ano:1986, faixas:12});
CREATE(:Musica{nome:'Enter Sandman', duracao:'5:30'});

CREATE(:Banda{nome:'Iron Maiden', ano:1975, estilo:'Heavy Metal'});
CREATE(:Album{nome:'Piece of Mind', ano:1983, faixas:9});
CREATE(:Musica{nome:'The Trooper', duracao:'4:12'});

CREATE(:Banda{nome:'Bon Jovi', ano:1983, estilo:'Rock'});
CREATE(:Album{nome:'Crush', ano:2000, faixas:13});
CREATE(:Musica{nome:'Its my Life', duracao:'3:45'});

~~~

# Relacionamentos entre Bandas, Albuns e Musicas
~~~SQL
MATCH(b:Banda{nome:'Metalica'}),(a:Album{nome:'Black Album'}), (m:Musica{nome:'Enter Sandman'})
CREATE(b)-[:POSSUI]->(a)-[:POSSUI]->(m);

MATCH(b:Banda{nome:'Iron Maiden'}),(a:Album{nome:'Piece of Mind'}), (m:Musica{nome:'The Trooper'})
CREATE(b)-[:POSSUI]->(a)-[:POSSUI]->(m);

MATCH(b:Banda{nome:'Bon Jovi'}),(a:Album{nome:'Crush'}), (m:Musica{nome:'Its my Life'})
CREATE(b)-[:POSSUI]->(a)-[:POSSUI]->(m);

MATCH(b:Banda{nome:'Metalica'}),(ba:Banda{nome:'Iron Maiden'})
CREATE(b)-[:RELACIONAMENTO_FORTE]->(ba);

MATCH(b:Banda{nome:'Metalica'}),(ba:Banda{nome:'Bon Jovi'})
CREATE(b)-[:RELACIONAMENTO_MEDIO]->(ba);

MATCH(b:Banda{nome:'Iron Maiden'}),(ba:Banda{nome:'Bon Jovi'})
CREATE(b)-[:RELACIONAMENTO_MEDIO]->(ba);

~~~