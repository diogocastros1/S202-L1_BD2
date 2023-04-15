from bson.objectid import ObjectId
from corrida import Corrida
from passageiro import Passageiro

class Motorista:
    def __init__(self, id: int, nome: str):
        self._id = id
        self.nome = nome
        self.nota = 0.0
        self.corridas = []

    def add_corrida(self, corrida: Corrida):
        self.corridas.append(corrida)


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def criar(self, motorista):
        try:
            res = self.db.collection.insert_one(motorista.__dict__)
            print(f'Motorista adicionado com sucesso! {res.inserted_id}')
            return res.inserted_id
        except Exception as e:
            print(f'Erro ao adicionar motorista: {e}')
            return None

    def ler(self, id: int):
        try:
            res = self.db.collection.find_one({'_id': id})
            print(f'Motirista encontrado!')
            return res
        except Exception as e:
            print(f'Erro na leitura do motorista: {e}')
            return None

    def atualizar(self, id: int, nome: str):
        try:
            res = self.db.collection.update_one(
                {'_id': id}, {'$set': {'nome': nome}})
            print(f'Nome atualizado!')
            return res
        except Exception as e:
            print(f'Erro ao atualizar: {e}')
            return None
    
    def atualizar_nota(self, id: int, nota: float):
        try:
            res = self.db.collection.update_one(
                {'_id': id}, {'$set': {'nota': nota}})
            print(f'Nota do motorista atualizada')
            return res
        except Exception as e:
            print(f'Erro ao atualizar nota do motorista: {e}')
            return None
    
    def adicionar_corrida(self, id: int, corrida: Corrida):
        try:
            res = self.db.collection.update_one(
                {'_id': id}, {'$push': {'corridas': corrida.to_dict()}})
            print(f'Corrida adicionada!')
            return res
        except Exception as e:
            print(f'Erro ao adicionar corrida: {e}')
            return None

    def deletar(self, id: int):
        try:
            res = self.db.collection.delete_one({'_id': id})
            print(
                f'Motorista deletado: {res.deleted_count} documento deletado')
            return res.deleted_count
        except Exception as e:
            print(f'Erro ao deletar motorista: {e}')
            return None


class MotoristaCLI:
    def __init__(self, database):
        self.motorista_dao = MotoristaDAO(database)

    def criar(self):
        id = int(input('Digite o id do motorista: '))
        nome = input('Digite o nome do motorista: ')

        motorista = Motorista(id, nome)
        count = 0
        nota_mot = motorista['nota']
        while True:
            nome_passageiro = input('Digite o nome do passageiro: ')
            documento = input('Digite o documento do passageiro: ')
            nota = float(input('Digite a nota do motorista: '))
            distancia = float(input('Digite a distancia da corrida: '))
            valor = float(input('Digite o valor da corrida: '))
            passageiro = Passageiro(nome_passageiro, documento)
            corrida = Corrida(nota, distancia, valor, passageiro)
            motorista.add_corrida(corrida.to_dict())
            count = count + 1
            nota_mot = (nota_mot + corrida.nota) / count
            continuar = input('Deseja adicionar mais corridas? (S/N)')
            if continuar.lower() == 'n':
                break
        result = self.motorista_dao.criar(motorista)
        self.motorista_dao.atualizar_nota(motorista._id, nota_mot)
        print(f'{result} motoristas foram criados!')

    def ler(self):
        id = int(input('Entre com o id do motorista: '))
        motorista = self.motorista_dao.ler(id)
        
        if motorista:           
            print(f"Id: {motorista['_id']}")
            print(f"Nome: {motorista['nome']}")
            print(f"Nota: {motorista['nota']}")
            print(f"Corridas: {len(motorista['corridas'])}")

    def atualizar(self):
        id = int(input('Entre com o id: '))
        nome = input('Entre com novo nome: ')
        self.motorista_dao.atualizar(id, nome)
        add_corrida = input('Deseja adicionar corrida:(S/N)')
        if(add_corrida.lower() != 'n'):
            motorista = self.motorista_dao.ler(id)
            count = len(motorista['corridas'])
            nota_mot = motorista['nota']
            while True:
                nome_passageiro = input('Digite o nome do passageiro: ')
                documento = input('Digite o documento do passageiro: ')
                nota = float(input('Digite a nota do motorista: '))
                distancia = float(input('Digite a distancia da corrida: '))
                valor = float(input('Digite o valor da corrida: '))
                passageiro = Passageiro(nome_passageiro, documento)
                corrida = Corrida(nota, distancia, valor, passageiro)
                self.motorista_dao.adicionar_corrida(id, corrida)
                count = count + 1
                nota_mot = (nota_mot + corrida.nota) / count
                print(nota_mot)
                continuar = input('Deseja adicionar mais corridas? (S/N)')
                if continuar.lower() == 'n':
                    break
            self.motorista_dao.atualizar_nota(id, nota_mot)

    def deletar(self):
        id = int(input('Entre com o id par deleta-lo: '))
        self.motorista_dao.deletar(id)

    def menu(self):
        while True:
            print('MENU PRINCIPAL:')
            print('1 - Criar motorista')
            print('2 - Consultar motorista')
            print('3 - Atualizar motorista')
            print('4 - Deletar motorista')
            print('0 - Sair')
            opcao = input('Digite a opção desejada: ')
            if opcao == '1':
                self.criar()
            elif opcao == '2':
                self.ler()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.deletar()
            elif opcao == '0':
                break
            else:
                print('Opção inválida!')
        print('Programa encerrado.')
