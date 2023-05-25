print('Este programa contém os exercícios do módulo 5 do curso de python na udemy, requisitado pela'
      'Tria Software. Aqui foram feitos os exercícios 30 a 37, visando a demnonstração. Selecione o'
      'exercício a ser resolvido a partir do input a seguir.')

x = int(input('Qual exercício? '))
if x == 30:
    a, b, c = input('Insira três números reais ').split()
    a = float(a)
    b = float(b)
    c = float(c)
    lis = [a, b, c]
    print(lis.sort())
elif x == 31:
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
elif x == 32:
    a = int(input('Código do produto '))
    b = int(input('Quantidade '))
    lis = [1.2, 1.3, 1.5, 1.2, 1.7, 2.2, 1.0]
    print('O preço a se pagar é R$' + str(lis[a-100] * b))
elif x == 33:
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
elif x == 34:
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
elif x == 35:
    d, m, a = input('Digite a data ').split('/')
    d = int(d)
    m = int(m)
    a = int(a)
    state = 'DATA VÁLIDA'
    lis = [False, True, False, True, True, False, False, True, False, True, False]
    if m <= 12 and d <= 31:
        if a % 4 != 0:
            if m == 2 and d == 29 or d == 30 or d == 31:
                state = 'DATA INVÁLIDA'
        elif m == 2 and d == 30 or d == 31:
            state = 'DATA INVÁLIDA'
        if m+1 != 2:
            if lis[m+1] and d == 31:
                state = 'DATA INVÁLIDA'
            else:
                state = 'DATA VÁLIDA'
    else:
        state = 'DATA INVÁLIDA'
    print(state)
elif x == 36:
    a = float(input('Insira o valor da venda'))
    b = a
    lis = [400.0 + 0.14 * a, 500.0 + 0.14 * a, 550.0 + 0.14 * a, 600.0 + 0.14 * a, 650.0 + 0.14 * a, 700.0 + 0.16 * a, ]
    if a > 100_000.0:
        b = 100_000.0
    if a < 20_000.0:
        b = 0
    print('O valor da comissão será de R$' + str(lis[int(b) // 20_000]))
elif x == 37:
    a = [int(x) for x in input('Insira o horário de chegada ').split(':')]
    b = [int(x) for x in input('Insira o horário de partida ').split(':')]
    p = 0
    lis = [1.0, 2.0, 3.4, 4.8]
    h = b[0] - a[0]
    if b[1] - a[1] > 0:
        h += 1
    if h >= 5:
        print(lis[3] + 2*(h-4))
    else:
        print(lis[h-1])