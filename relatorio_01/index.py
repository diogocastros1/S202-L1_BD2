class Professor:
    def __init__(self, nome):
        self.nome = nome
    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} esta ministrando a aula sobre {assunto}.')

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def presenca(self):
        print(f'O aluno {self.nome} esta presente.')
        
class Aula:
    def __init__(self, professor, assunto, alunos = []):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def listar_presenca(self):
        print(f'Presenca na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}')
        for aluno in self.alunos:
            aluno.presenca()
    
aula = Aula(Professor('Renzo'), 'BD2')
aula.adicionar_aluno(Aluno('Diogo'))
aula.adicionar_aluno(Aluno('Giovanna'))
aula.listar_presenca()
