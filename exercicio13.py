#Faça um algoritmo que leia 30 valores do tipo inteiro e o
# armazene-os em um vetor.

# A seguir, o algoritmo deverá informar:
# 1. Todos os números pares que existem no vetor.
# 2. O menor e o maior valor existente no vetor.
# 3. Quantos dos valores do vetor são maiores que a média desses valores.

numeros = [0]*30
soma = 0
for x in range (30):
    numeros[x] = int(input('Digite um número: '))
    soma+=numeros[x]

pares=0


for y in range (30):
    if numeros[y]%2==0:
        pares+=1

print(f'Numeros pares são: {pares}')

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')

media = soma/30
cont=0
for i in range(30):
    if numeros[i] >= media:
        cont+=1

print(f'A média dos valores é {media}')
print(f'A quantidade dos valores maiores que a média dos valores são: {cont}')

