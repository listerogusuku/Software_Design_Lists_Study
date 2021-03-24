
lista = []

i = 0
c = 0

while i < 5:
    n = float(input(f'Digite a nota do aluno {i+1}: '))
    c += n
    lista.append(n)
    i+=1

print(f'A média do aluno foi: {c/5}')

