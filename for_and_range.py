# n = 10

# for cont in range(n):
#     print(cont)



# num = int(input('Digite um número para iniciar sua lista de pares: '))
# num2 = int(input('Digite um número para ser o último da sua lista de pares: '))

# for i in range(num, num2+1):
#     if i % 2 == 0:
#         print(i)



# for i in range(num, num2+1, 2):
#     print(i)


#Modeling of a lançamento de um foguete:

# print('\nLançamento!\n')
# for i in range(10, 0, -1):
#     print(f'Contagem regressiva: {i}')
# print('\nFoguete lançado!\n')


'''

RANGE ==> (começo, != fim, valor de incremento)


'''


# n = int(input('Digite a fatorial desejada: '))

# c = 1
# for i in range(n, 1, -1):
#     c*=i

# print(f'O fatorial de {n} é {c}.')


# n = 5

# for n in range(5, 51, 5):
#     print(n*(n+1)//2)



total = int(input('\nQual o número total de eleitores? '))

candidatoA = 0
candidatoB = 0
candidatoC = 0

for i in range(total):
    voto = int(input('Em quem você deseja votar? [1 - CandidatoA, 2 - Candidato B, 3- Candidato C:] '))
    while True:
        if voto > 3 or voto < 1:
            voto = int(input('Voto inválido! Digite um valor válido entre 1 e 3!'))
        else:
            break
    if voto == 1:
        candidatoA+=1
    elif voto == 2:
        candidatoB+=1
    else:
        candidatoC+=1
    
print('\n Votação encerrada! \n')

print('\nApuração dos votos:\n')

print(f'Quantidade de votos do candidato A: {candidatoA} votos.')
print(f'Quantidade de votos do candidato B: {candidatoB} votos.')
print(f'Quantidade de votos do candidato C: {candidatoC} votos.')

print('\nObrigado por participar dessa eleição!\n')