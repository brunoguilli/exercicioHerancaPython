from aluno import Aluno


class AlunoEnsinoMedio(Aluno):

    def __init__(self,nome, matricula, ano):
        Aluno.__init__(self,nome, matricula)
        self.ano = ano

    def imprimir(self):
        Aluno.imprimir(self)
        print("Ano: ",self.ano)