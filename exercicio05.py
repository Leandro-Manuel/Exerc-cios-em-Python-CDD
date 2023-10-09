#Ler um vetor A de 10 números. logo em seguida, ler mais um número
# e guardar em uma variável X.

#Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo
# valor X. Logo após, imprimir o vetor M.

A = [0]*10

for x in range (10):
    A[x] = int (input('Digite um número (vetor A): '))

X = int (input('Digite um número (Multiplicador): '))

M = [0]*10

for y in range (10):
    M[y] = A[y] * X

print(M)
