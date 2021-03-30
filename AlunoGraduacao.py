from aluno import Aluno


class AlunoGraduacao(Aluno):

    def __init__(self, nome, matricula, semestre):
        Aluno.__init__(self ,nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        Aluno.imprimir(self)
        print("Semestre: ",self.semestre)
