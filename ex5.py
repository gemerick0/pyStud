print('Este programa contém os exercícios do módulo 5 do curso de python na udemy, requisitado pela'
      'Tria Software. Aqui foram feitos os exercícios 30 a 40, visando a demnonstração. Selecione o'
      'exercício a ser resolvido a partir do input a seguir.')

x = int(input('Qual exercício? '))
if x == 30:
    a, b, c = input('Insira três números reais ').split()
    a = float(a)
    b = float(b)
    c = float(c)
    lis = [a, b, c]
    print(lis.sort())
if x == 31:
    a, p = input('Insira altura e peso ').split()
    a = float(a)
    p = float(p)
    if p < 60:
        if a < 1.2:
            print('A')
        elif a > 1.7:
            print('C')
        else:
            print('B')
    if p > 90:
        if a < 1.2:
            print('G')
        elif a > 1.7:
            print('I')
        else:
            print('H')
    else:
        if a < 1.2:
            print('D')
        elif a > 1.7:
            print('F')
        else:
            print('E')
if x == 32:
    a = int(input('Código do produto '))
    b = int(input('Quantidade '))
    lis = [1.2, 1.3, 1.5, 1.2, 1.7, 2.2, 1.0]
    print('O preço a se pagar é R$' + str(lis[a-100] * b))
if x == 33:
    a = float(input('Insira o preço antigo '))
    if a < 50:
        a = a * 105
    elif a > 100:
        a = a * 115
    else:
        a = a * 110
    if a < 80:
        print('O preço novo é barato, de R$' + str(a))
    elif 80 <= a <= 120:
        print('O preço novo é normal, de R$' + str(a))
    elif 120 <= a <= 200:
        print('O preço novo é caro, de R$' + str(a))
    else:
        print('O preço novo é muito caro, de R$' + str(a))
if x == 34:
    a, b = input('Digite a nota e o número de faltas ')
    a = float(a)
    b = int(b)
    lis = ['A', 'B', 'C', 'D', 'E']
    x = 0
    if b <= 20:
        if a <= 8.9:
            x += 1
        elif 5.0 <= a <= 7.4:
            x += 2
        elif 4.0 <= a <= 4.9:
            x += 3
        else:
            x += 4
    else:
        if a <= 8.9:
            x += 2
        elif 5.0 <= a <= 7.4:
            x += 3
        else:
            x += 4
    print(lis[x])
if x == 35:
    d, m, a = input('Digite a data ').split('/')
    d = int(d)
    m = int(m)
    a = int(a)
    state = ''
    lis = [False, True, False, True, True, False, False, True, False, True, False]
    if m <= 12 and d <= 31:
        if a % 4 != 0:
            if m == 2 and d == 29 or d == 30 or d == 31:
                state = 'DATA INVÁLIDA'
        elif m == 2 and d == 30 or d == 31:
            state = 'DATA INVÁLIDA'
        if lis[m] != 2:
            if lis[m] and d == 31:
                state = 'DATA INVÁLIDA'
            else:
                state = 'DATA VÁLIDA'
    else:
        state = 'DATA INVÁLIDA'
    print(state)