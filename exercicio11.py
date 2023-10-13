# Faça um código para ler um vetor de 30 números.
# Após isto, ler mais um número qualquer, calcular e escrever quantas vezes
# esse número aparece no vetor.

A = [0]*30

for x in range(30):
    A[x] = int(input(f'Digite um número qualquer ({x+1}): '))

numero_verificador = int(input('Digite um número para verificar: '))

cont = 0
for y in range(30):
    if numero_verificador == A[y]:
        cont+=1

print(f'A quantidade de vezes que o número verificador esteve no array foi: {cont}.')

