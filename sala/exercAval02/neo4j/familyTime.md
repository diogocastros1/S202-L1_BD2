# Parte 1

## 1. Restrições de Nós (Nodes)
    a. O Grafo deverá ter ao menos 10 Nós;

    b. Cada Nó deverá possuir ao menos 2 Labels;
        i. Por exemplo, se for uma pessoa, poderá ter os Labels Pessoa e Engenheiro (o segundo Label veja que pode ser uma Profissão que ela possui). Se for um pet, poderá ter os Labels Pet e Cachorro, por exemplo;

    c. Cada Node deverá ter ao menos 3 Propriedades (Ex: nome, sexo, idade etc.);

---

### Criando nós

~~~SQL
CREATE(:Pessoa:Artista{nome:'Thammy',sexo:'F',idade:24});
CREATE(:Pessoa:Engenheiro{nome:'John',sexo:'M',idade:25});
CREATE(:Pessoa:Agronomo{nome:'Ana',sexo:'F',idade:55});
CREATE(:Pessoa:Fazendeiro{nome:'Edson',sexo:'M',idade:56});
CREATE(:Pessoa:Motorista{nome:'Vander',sexo:'M',idade:56});
CREATE(:Pessoa:Professora{nome:'Rita',sexo:'F',idade:57});

CREATE(:Animal:Gato{nome:'Bucky',sexo:'M',idade:2});
CREATE(:Animal:Gato{nome:'Kira',sexo:'F',idade:2});
CREATE(:Animal:Cachorro{nome:'Gaucho',sexo:'M',idade:2});
CREATE(:Animal:Cachorro{nome:'Tupan',sexo:'M',idade:3});
~~~

---
## 2. Restrições de Relacionamentos (Relationships):
    a. O Grafo deve ter pelo menos 4 tipos de relacionamentos diferentes;
    
        i. Por exemplo, PAI_DE, IRMAO_DE, DONO_DE, NAMORADO_DE, ESPOSO_DE etc;
    
        ii. A fim de facilitar e criar menos tipos de Relacionamentos, não os crie levando o sexo em consideração. Ex: em vez de criar PAI_DE e MAE_DE, use por exemplo apenas o PAI_DE para mostrar que alguém é pai ou mãe de alguém;

    b. Ao menos um dos Relacionamentos deverá ter ao menos uma Propriedade;

### Criando relacionamentos

~~~SQL
MATCH(pa:Pessoa{nome:'John'}),(pb:Pessoa{nome:'Thammy'})
CREATE(pa)-[:CASADO_COM{anos:2}]->(pb);
MATCH(pa:Pessoa{nome:'Vander'}),(pb:Pessoa{nome:'Rita'})
CREATE(pa)-[:CASADO_COM{anos:37}]->(pb);
MATCH(pa:Pessoa{nome:'Edson'}),(pb:Pessoa{nome:'Ana'})
CREATE(pa)-[:CASADO_COM{anos:36}]->(pb);

MATCH(pa:Pessoa{nome:'Edson'}),(pb:Pessoa{nome:'Thammy'})
CREATE(pa)-[:PAI_DE]->(pb);
MATCH(pa:Pessoa{nome:'Vander'}),(pb:Pessoa{nome:'John'})
CREATE(pa)-[:PAI_DE]->(pb);
MATCH(pa:Pessoa{nome:'Rita'}),(pb:Pessoa{nome:'John'})
CREATE(pa)-[:MAE_DE]->(pb);
MATCH(pa:Pessoa{nome:'Ana'}),(pb:Pessoa{nome:'Thammy'})
CREATE(pa)-[:MAE_DE]->(pb);

MATCH(pa:Pessoa{nome:'Rita'}),(pb:Pessoa{nome:'Thammy'})
CREATE(pa)<-[:NORA_DE]-(pb);
MATCH(pa:Pessoa{nome:'Vander'}),(pb:Pessoa{nome:'Thammy'})
CREATE(pa)<-[:NORA_DE]-(pb);
MATCH(pa:Pessoa{nome:'Edson'}),(pb:Pessoa{nome:'John'})
CREATE(pa)<-[:GENRO_DE]-(pb);
MATCH(pa:Pessoa{nome:'Ana'}),(pb:Pessoa{nome:'John'})
CREATE(pa)<-[:GENRO_DE]-(pb);

MATCH(pa:Pessoa{nome:'Edson'}),(pb:Pessoa{nome:'Ana'}), (ca:Cachorro{nome:'Gaucho'})
CREATE(pa)-[:DONO_DE]->(ca), (ca)<-[:DONO_DE]-(pb);
MATCH(pa:Pessoa{nome:'John'}),(pb:Pessoa{nome:'Thammy'}), (aa:Animal{nome:'Bucky'}), (ab:Animal{nome:'Kira'})
CREATE(pa)-[:DONO_DE]->(aa), (aa)<-[:DONO_DE]-(pb), (pa)-[:DONO_DE]->(ab), (ab)<-[:DONO_DE]-(pb);
MATCH(pa:Pessoa{nome:'Rita'}),(pb:Pessoa{nome:'Vander'}), (ca:Cachorro{nome:'Tupan'})
CREATE(pa)-[:DONO_DE]->(ca), (ca)<-[:DONO_DE]-(pb);

MATCH(aa:Animal{nome:'Tupan'}), (ab:Animal{nome:'Gaucho'})
CREATE(aa)-[:IRMAO_DE]->(ab);
MATCH(aa:Animal{nome:'Bucky'}), (ab:Animal{nome:'Kira'})
CREATE(aa)-[:IRMAO_DE]->(ab);

~~~

# Parte 2

    1. Por meio de uma linguagem de programação (de preferência o Python), criar um Client de consulta ao Grafo criado;
    2. O Client deverá responder, no mínimo, a 3 perguntas sobre sua família se baseando nas informações do Grafo;
    
        a. Exemplo de perguntas: “Quem da família é Engenheiro?”, “Fulano de tal é pai de quem?”, “Sicrana de 
        tal namora com quem desde quando?” etc