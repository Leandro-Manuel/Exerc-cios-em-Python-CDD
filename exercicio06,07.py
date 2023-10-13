#Faça um código para ler 5 números e armazenar em um vetor.
#Após a leitura total dos 5 números, o código deve escrever esses 5 números
#lidos na ordem inversa.

numeros = [0]*5

for x in range (5):
    numeros[x] = int (input('Digite um número: '))

for y in range (4,-1,-1):
    print(numeros[y])