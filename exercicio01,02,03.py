# Perguntar ao usuário quantos alunos tem na sala e criar um array,
# unidimensional (vetor) com o nome de todos os alunos da sala.

# Altere o exercício anterior e mostre na tela, ao final, o nome de cada aluno
# e sua respectiva posição no array.

#altere o exercicio para permitir achar o nome de um aluno na lista

qtd = int (input('Informe a quantidade de alunos: '))

alunos = [0]*qtd

for x in range (qtd):
    alunos[x] = str (input(f'Qual é o nome do {x+1}a aluno? '))

for y in range (qtd):
    print(f'{alunos[y]} está na {y+1}a posição!')



