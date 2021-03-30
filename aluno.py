class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome;
        self.matricula = matricula;

    def getMatricula(self):
        return self.matricula;

    def setMatricula(self,matricula):
        self.matricula = matricula

    def getNome(self):
        return self.nome;

    def setNome(self, nome):
        self.nome = nome

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Matricula: ", self.matricula)