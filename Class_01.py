
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
'''


'''

#JACA WARS


import math


v = float(input('Digite a velocidade: '))
teta = float(input('Digite o ângulo: '))

convert_graus = (math.sin(math.radians(teta)))
multiplica_graus = 2*convert_graus

g = 9.8
d = ((v**2)*multiplica_graus)/g


if d < 98:
    print('Muito perto')
elif d > 102:
    print('Muito longe')
else:
    print('Acertou!')


'''

'''

def classifica_idade(x):
    if x <= 11:
        return 'crianca'
    elif x <= 17:
        return 'adolescente'
    else:
        return 'adulto'



'''
'''

velocity = float(input('Type the cars velocity: '))

if velocity > 80:
    print(f'Você foi multado! A multa será de R${((80-velocity)*5)*-1:.2f}')
else:
    print('Não foi multado')


'''


'''
def calcula_aumento(salary):
    aumento = 0
    if salary > 1250:
        aumento = salary*0.1
    elif salary <= 1250:
        aumento = salary*0.15
    return aumento
'''

'''
def calcula_pi(n):
    i = 1
    contador = 0
    while i <= n:
        formula = 6/(i**2)
        contador += formula
        i+=1
    resultado = contador**0.5
    return resultado
'''


'''
def maximo_divisor_comum(x, y):
    if x > y:
        divisao = x%y
        acumulador = divisao
        if divisao > 0:
            i=1
            while i > 0:
                divisao = y%divisao
                if divisao > 0:
                    acumulador = divisao
                else:
                    break

                if acumulador>0:
                    nova_divisao = (y-acumulador)/acumulador

                if nova_divisao > 0:
                    i+=1
                    y = y-acumulador
                else:
                    break
        else:
            acumulador = divisao

    else:
        divisao = y%x
        acumulador = divisao

        print(divisao)

        if divisao > 0:
            i=1
            while i > 0:
                divisao = x%divisao
                if divisao > 0:
                    acumulador = divisao
                else:
                    break

                if acumulador>0:
                    nova_divisao = (x-acumulador)/acumulador

                if nova_divisao > 0:
                    i+=1
                    x = x-acumulador
                else:
                    break
        else:
            acumulador = divisao

    return acumulador

valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))

print(maximo_divisor_comum(valor1, valor2))
'''


def eh_primo(n):
    if n == 0 or n == 1:# or n == 4:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        i = 3
        while i < n:
            verificador = n % i
            if verificador != 0:
                i+=1
            else:
                return False
        # return True
    return True


verifica = int(input('Digite um número a ser verificado: '))

print(eh_primo(verifica))

