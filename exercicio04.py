# Escreva um código que permita a leitura das notas de uma turma
# de 5 alunos e guarde num vetor, calcular a média da turma e contar
# quantos alunos obtiveram nota acima desta média calculada.
# Escrever a média da turma e o resultado da contagem.

turma = 5

notas = [0]*turma
soma=0

cont =0

for x in range (turma):
    notas[x] = float (input(f'Informe a nota do {x+1}a aluno: '))
    soma += notas[x]

for y in range (turma):
    if notas[y] >= soma/turma:
        cont+=1

print(f'A média da turma foi: {soma/turma} e os alunos que tiraram nota igual ou superior foi: {cont}')
