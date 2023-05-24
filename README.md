# S202-L1_BD2
Destinado para a entrega dos relatórios de banco de dados II.

# Criação de venv

1. No cmd acessar a pasta do projeto e digitar
~~~
python -m venv .venv
~~~

2. Ativar virtual env
~~~
.venv\Scripts\activate
~~~

3. Instalar pymongo
~~~
pip install pymongo
~~~

4. Instalar Neo4J
Crie um arquivo chamado `requirements.txt` e coloque o seguinte:

~~~python
neo4j==5.8.0
pytz==2023.3
~~~

Após isto digite o seguinte comando.

~~~
pip install -r requirements.txt
~~~