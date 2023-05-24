class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create_teacher(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
    
    def get_teacher(self, name):
        query = "MATCH (a:Teacher{name:$name}) RETURN a.name, a.cpf;"
        parameters = {"name":name}
        results = self.db.execute_query(query, parameters)
        return [(result["a.name"], result["a.cpf"]) for result in results]
    
    def delete_teacher(self, name):
        query = "MATCH (p:Teacher {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update_cpf_teacher(self, name, cpf):
        query = "MATCH (p:Teacher {name: $name}) SET p.cpf = $cpf"
        parameters = {"name": name, "cpf": cpf}
        self.db.execute_query(query, parameters)


class TeacherCLI:
    def __init__(self, database):
        self.teacher_crud = TeacherCRUD(database)

    def criar(self):
        name = input('Digite o nome do professor: ')
        cpf = input('Digite o CPF do professor: ')
        ano_nasc = int(input('Digite o ano de nascimento: '))
        
        self.teacher_crud.create_teacher(name, ano_nasc, cpf)
        
        print('Professor criado!')

    def ler(self):
        name = input('Entre com o nome do professor: ')
        print(self.teacher_crud.get_teacher(name))

    def atualizar(self):
        name = input('Entre com nome: ')
        cpf = input('Entre com novo CPF: ')
        self.teacher_crud.update_cpf_teacher(name, cpf)
        
    def deletar(self):
        name = input('Entre com o nome do professor para deleta-lo: ')
        self.teacher_crud.delete_teacher(name)

    def menu(self):
        while True:
            print('MENU PRINCIPAL:')
            print('1 - Criar teacher')
            print('2 - Consultar teacher')
            print('3 - Atualizar teacher')
            print('4 - Deletar teacher')
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