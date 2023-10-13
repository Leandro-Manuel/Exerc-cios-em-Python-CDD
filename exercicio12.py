# Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes,
# e que exiba a lista desses nomes na tela.

# Após exibir essa lista, o programa deve mostrar também os nomes na ordem
# inversa em que o usuário os digitou, um por linha.

nomes = [0]*5

for x in range (5):
    nomes[x] = str (input('Digite o seu nome: '))

print("Nomes digitados:", end=" ")

for y in range (5):
    print(nomes[y],end=" ")

print()

for z in range (4,-1,-1):
    print(nomes[z])