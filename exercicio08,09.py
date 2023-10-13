# Faça um código para ler 5 nomes de usuários e suas respectivas
# senhas, e armazenar cada lista em um array diferente, após
# oompletar a digitação, imprimir o nome, senha e posição dos dados no array.

# Altere o sistema anterior e faça um sistema de login, pedindo a senha
# do usuário e mostrando seu nome e a mensagem, login efetuado com sucesso.

usuarios = [0]*5
senhas = [0]*5

for x in range (5):
    usuarios[x] = input(f'Digite o seu login ({x+1}): ')

for y in range (5):
    senhas[y] = input(f'Digite sua senha ({y+1}): ')

for z in range(5):
    print(f'Login: {usuarios[z]}, senha: {senhas[z]}, posição: {z+1}')

verif = input('Digite a sua senha: ')

for t in range(5):
    if verif == senhas[t]:
        print(f'Login: {usuarios[t]}, login efetuado com sucesso!')