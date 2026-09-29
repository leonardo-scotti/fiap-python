from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []
        self.notas_disciplinas = {}

    def exibir_infos(self):
        print(f"Nome: {self.nome} | Matrícula: {self.matricula}")

    def matricular(self, disciplina: Disciplina):
        """Adicionar a disciplina na lista de disciplinas do aluno"""
        if disciplina not in self.notas_disciplinas:
            self.disciplinas.append(disciplina)

        self.notas_disciplinas.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        """Adicionar uma nota do aluno referente a uma disciplina"""
        self.notas_disciplinas[disciplina.nome].append(nota)

    def calcular_media_d(self, d: Disciplina) -> float:
        notas = self.notas_disciplinas.get(d.nome)
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def calcular_media_geral(self) -> float:
        medias = []

        for d in self.disciplinas:
            media_d = self.calcular_media_d(d)
            medias.append(media_d)

        return sum(medias) / len(medias)

    def gerar_boletim(self):
        self.exibir_infos()
        