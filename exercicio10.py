# Faça um código para ler um valor N qualquer (que será o tamanho
# dos vetores). após ler dois vetores A e B (de tamanho N cada um)
# e depois armazenar em um terceiro vetor Soma, a soma dos elementos A
# com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.

tmn = int (input('Digite o tamanho: '))

A = [0]*tmn
B = [0]*tmn

Soma = [0]*tmn

for x in range (tmn):
    A[x] = int(input('Digite um número: '))
    B[x] = int(input('Digite outro número: '))

for y in range (tmn):
    Soma[y] = A[y] + B[y]

print(Soma)



