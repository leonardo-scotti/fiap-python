from aluno import Aluno
from disciplina import Disciplina

# criar/instanciar um aluno
aluno1 = Aluno('Leonardo', 'rm573305', 'Ciência da Computação')

# criar 2 disciplinas
cs = Disciplina('Computer Science', 'Lucas')
model_mat = Disciplina('Modelagem Matemática', 'Christiam')

aluno1.matricular(cs)
aluno1.matricular(model_mat)

# Adicionar notas do aluno referente a determinada disciplina
aluno1.adicionar_nota(cs, 10.0)
aluno1.adicionar_nota(cs, 8.0)
aluno1.adicionar_nota(model_mat, 5.0)
aluno1.adicionar_nota(model_mat, 4.0)

print(aluno1.calcular_media_geral())