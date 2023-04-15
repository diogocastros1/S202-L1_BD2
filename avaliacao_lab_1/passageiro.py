class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento
        
    def to_dict(self):
        return {
            "nome": self.nome,
            "documento": self.documento
        }