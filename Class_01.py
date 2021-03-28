
# lista = []

# i = 0
# c = 0

# while i < 5:
#     n = float(input(f'Digite a nota do aluno {i+1}: '))
#     c += n
#     lista.append(n)
#     i+=1

# print(f'A média do aluno foi: {c/5}')

# ------


'''
notas = [0]

i = 0
s = 0
while i < len(notas):
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)
    s += nota
    pergunta = input('Deseja adicionar mais alguma nota? [S/N]: ')
    if pergunta == 'S':
        i+=1
    else:
        break

print(f'A média do aluno foi: {s/(len(notas)-1)} ')

'''

numbers_list = [0]

i = 0

while i < len(numbers_list):
    number = float(input(f'Digite um número para ser armazenado na posição {i+1} da lista: '))
    numbers_list.append(number)
    pergunta = input('Deseja adicionar mais algum número na lista? [S/N]: ')
    if pergunta == 'S':
        i+=1
    else:
        print('Sua lista está pronta! \n')
        c = 1
        while c > 0:
            pergunta2 = int(input('Você deseja ver o número guardado em qual posição da lista? '))
            if pergunta2 > len(numbers_list):
                print('Número Inválido! Maior do que a quantidade de elementos existente na lista!')
                c+=1
            else:
                break
        break

            # pergunta2 = int(input('Você deseja ver o número guardado em qual posição da lista? ')
        # if pergunta2 <= len(numbers_list):

del numbers_list[0]


print(f'Sua lista foi {numbers_list} e o número que está na posição escolhida por você é o {numbers_list[pergunta2-1]}')
