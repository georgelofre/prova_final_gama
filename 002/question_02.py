def menor10(num):
    if num < 10:
        print('O número é menor do que 10.')

def par(num):
    if num % 2 == 0:
        print('O número é par.')

def entre8e16(num):
    if 8 < num < 16:
        print('O número está entre 8 e 16.')

def numero51ou80(num):
    if num == 51 or num == 80:
        print('O número é 51 ou 80.')

while True:
    numero = input('Digite um número inteiro: ')
    if numero.isdigit():
        numero = int(numero)
        menor10(numero)
        par(numero)
        entre8e16(numero)
        numero51ou80(numero)
        continuar = input('Deseja verificar outro número? [S/N] ').strip()[0]
        if continuar in "Nn":
            break
    else:
        print('Digite apenas um número inteiro!')

