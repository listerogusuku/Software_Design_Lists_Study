
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



del numbers_list[0]


print(f'Sua lista foi {numbers_list} e o número que está na posição escolhida por você é o {numbers_list[pergunta2-1]}')
'''






lista1 = [0,1,2,3,10,12,17,21,33,45,50,75,100,87]
lista2 = [2,3,7,8,18,13,21,35,42,49,70,100,98,52]

lista3 = []
lista_repetidos = []

i = 0

while i < len(lista1):
    s = 0
    c = 0
    while c<len(lista2):
        if lista1[s] == lista2[c]:
            lista_repetidos.append(lista1[s])
            s+=1
            c+=1
        elif lista1[s] != lista2[c]:
            lista3.append(lista1[c])
            c+=1
        c+=1

    # i = 0
    # while i < len(lista1):
    #     lista3[i] = lista1[i]
    #     i+=1

    i+=1

# print(lista3)
print(lista_repetidos)
print(lista3)
