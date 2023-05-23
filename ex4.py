x = int(input('Qual exercício? '))
if x == 1:
    y = int(input('Digite um número inteiro '))
    print('Você digitou ' + str(y))
elif x == 2:
    y = float(input('Digite um número real '))
    print('Você digitou ' + str(y))
elif x == 3:
    a, b, c = input('Digite três números separados por espaço ').split()
    print('Esta é a soma ' + str(int(a) + int(b) + int(c)))
elif x == 4:
    a = float(input('Digite um número real '))
    print('Este é o quadrado deste número ' + str(a ** 2))
elif x == 5:
    a = float(input('Digite um número real '))
    print('Esta é a quinta parte deste número ' + str(a / 5))
elif x == 6:
    a = float(input('Digite uma temperatura em Celsius '))
    print('Esta é a temperatura equivalente em Farenheit ' + str(a * 9 / 5 + 32))
elif x == 7:
    a = float(input('Digite uma temperatura em Farenheit '))
    print('Esta é a temperatura equivalente em Farenheit ' + str(a - 32 * 5 / 9))
elif x == 8:
    a = float(input('Digite uma temperatura em Kelvin '))
    print('Esta é a temperatura equivalente em Celsius ' + str(a - 273.15))
elif x == 9:
    a = float(input('Digite uma temperatura em Celsius '))
    print('Esta é a temperatura equivalente em Kelvin ' + str(a + 273.15))
elif x == 10:
    a = float(input('Digite uma velocidade em km/h '))
    print('Esta é a velocidade equivalente em m/s ' + str(a / 3.6))
elif x == 11:
    a = float(input('Digite uma velocidade em m/s '))
    print('Esta é a velocidade equivalente em km/h ' + str(a * 3.6))
elif x == 12:
    a = float(input('Digite uma distância em milhas '))
    print('Esta é a distância equivalente em quilômetros ' + str(a * 1.61))
elif x == 13:
    a = float(input('Digite uma distância em quilômetros '))
    print('Esta é a distância equivalente em milhas ' + str(a / 1.61))
elif x == 14:
    a = float(input('Digite um ângulo em graus '))
    print('Este é o ângulo equivalente em radianos ' + str(a * 3.14 / 180))
elif x == 15:
    a = float(input('Digite um ângulo em radianos '))
    print('Este é o ângulo equivalente em graus ' + str(a / 3.14 * 180))
elif x == 16:
    a = float(input('Digite um comprimento em polegadas '))
    print('Este é o comprimento equivalente em centímetros ' + str(a * 2.54))
elif x == 17:
    a = float(input('Digite um comprimento em centímetros '))
    print('Este é o comprimento equivalente em polegadas ' + str(a / 2.54))
elif x == 18:
    a = float(input('Digite um volume em metros cúbicos '))
    print('Este é o volume equivalente em litros ' + str(a * 1000))
elif x == 19:
    a = float(input('Digite um volume em litros '))
    print('Este é o volume equivalente em metros cúbicos ' + str(a / 1000))
elif x == 20:
    a = float(input('Digite um valor de massa em quilogramas'))
    print('Este é o valor da massa equivalente em libras ' + str(a / 0.45))
elif x == 21:
    a = float(input('Digite um valor de massa em libras'))
    print('Este é o valor da massa equivalente em quilogramas ' + str(a * 0.45))
elif x == 22:
    a = float(input('Digite um comprimento em jardas '))
    print('Este é o comprimento equivalente em metros ' + str(a * 0.91))
elif x == 23:
    a = float(input('Digite um comprimento em metros '))
    print('Este é o comprimento equivalente em jardas ' + str(a / 0.91))
elif x == 24:
    a = float(input('Digite uma área em metros quadrados '))
    print('Esta é a área equivalente em acres ' + str(a * 0.000247))
elif x == 25:
    a = float(input('Digite uma área em acres '))
    print('Esta é a área equivalente em metros ' + str(a / 0.000247))
elif x == 26:
    a = float(input('Digite uma área em metros '))
    print('Esta é a área equivalente em hectares ' + str(a * 0.0001))
elif x == 27:
    a = float(input('Digite uma área em hectares '))
    print('Esta é a área equivalente em metros ' + str(a / 0.0001))
elif x == 28:
    a, b, c = input('Digite três números separados por espaço ').split()
    print('Esta é a soma de seus quadrados ' + str(float(a) ** 2 + float(b) ** 2 + float(c) ** 2))
elif x == 29:
    a, b, c, d = input('Digite quatro notas separadas por espaço ').split()
    print('Esta é a sua média aritmética ' + str((float(a) + float(b) + float(c) + float(d)) / 4))
elif x == 30:
    a, b = input('Digite um valor em reais e a cotação do dólar separados por espaço ').split()
    print('Este é o valor equivalente em dólares ' + str(float(a) * float(b)))
elif x == 31:
    a = int(input('Digite um número inteiro '))
    print(str(a - 1) + ' e ' + str(a + 1) + ' são, respectivamente, o antecessor e sucessor desse número.')
elif x == 32:
    a = int(input('Digite um número inteiro '))
    print(str(
        a * 2 - 1 + a * 3 + 1) + ' é o resultado da soma do antecessor do dobro com o sucessor do triplo desse número.')
elif x == 33:
    a = float(input('Digite um número real como lado de um quadrado '))
    print(str(a ** 2) + ' é o valor de sua área.')
elif x == 34:
    a = float(input('Digite um número real como raio de um círculo '))
    print(str(a ** 2 * 3.141592) + ' é o valor de sua área.')
elif x == 35:
    a, b = input('Digite os valores dos catetos de um triângulo retângulo ').split()
    print(str((float(a) ** 2 + float(b) ** 2) ** (1 / 2)) + ' é o valor de sua hipotenusa.')
elif x == 36:
    a, b = input('Digite os valores da altura e raio de um cilindro ').split()
    print(str(float(a) * float(b) ** 2 * 3.141592) + ' é o valor de seu volume.')
elif x == 37:
    a = float(input('Digite o valor do produto para cálculo do desconto '))
    print(str(a * 0.88) + ' é o valor do produto com desconto.')
elif x == 38:
    a = float(input('Digite o valor do salário para cálculo do aumento '))
    print(str(a * 1.25) + ' é o valor do salário com aumento.')
elif x == 39:
    a = float(780_000.00)
    print('O primeiro vencedor ganhará R$' + str(a * 0.46) + ', o segundo vencedor ganhará R$'
          + str(a * 0.32) + ' e o terceiro vencedor ganhará R$' + str(a * (1 - 0.46 - 0.32)) + '.')
elif x == 40:
    a = int(input('Quantos dias ele trabalhou? '))
    print('Hão de ser pagos R$' + str(float(a) * 0.92 * 30) + '.')
elif x == 41:
    a, b = input('Digite o valor da hora de trabalho e as horas trabalhadas pelo funcionário ').split()
    print('Hão de ser pagos R$' + str(a * b * 1.1) + ' ao trabalhador.')
elif x == 42:
    a = float(input('Digite o salário-base do funcionário '))
    print('O salário total é de R$' + str(a * 0.98))
elif x == 43:
    a = float(input('Digite o valor total '))
    print('O valor com desconto aplicado é de R$' + str(a * 0.9) + '\nO valor das parcelas será de R$'
          + str(a / 3) + '\nA comissão na compra a vista há de ser de R$' + str(a * 0.9 * 0.05)
          + '\nA comissão na compra parcelada há de ser de R$' + str(a * 0.05))
elif x == 44:
    a, b = input('Digite a altura dos degraus e a altura desejada ').split()
    print('O número de degraus que hão de ser subidos é ' + str(int(float(b) / float(a))))
elif x == 45:
    a = input('Digite uma letra maiúscula ')
    print('Essa letra minúscula é: ' + a.lower())
elif x == 46:
    a = int(input('Digite um número inteiro positivo de três números '))
    if 99 < a < 1000:
        print(str(a)[::-1] + ' É o aferido número invertido.')
    else:
        print('Siga as regras')
elif x == 47:
    a = input('Digite um número inteiro positivo de quatro dígitos ')
    if 999 < int(a) < 10000:
        char = list(a)
        for n in char:
            print(n)
    else:
        print('Siga as regras')
elif x == 48:
    a = int(input('Digite uma quantidade de segundos '))
    print(str(a // 3600) + ":" + str(a // 60) + ":" + str(a % 60))
elif x == 49:
    h, m, s = input('Digite horas, minutos e segundos correspondentes ao horário de início ').split()
    a = int(input('Digite uma quantidade de segundos '))
    ah: int = int(h) + a // 3600
    d: int = 0
    am: int = int(m) + a // 60
    an: int = int(s) + a % 60
    if an > 60:
        an = an % 60
        am += int(s) // 60
    if am > 60:
        am = am % 60
        ah += int(m) // 60
    if ah > 24:
        d += ah // 24
        ah = ah % 24
    print(str(ah) + ":" + str(am) + ":" + str(an) + " depois de " + str(d) + ' dias.')
elif x == 50:
    a, b = input('Digite a idade e o ano atual ').split()
    boo = bool(input('Já fez aniversário esse ano? (responda com True ou False)'))
    if boo:
        print('Seu ano de nascimento é ' + str(b - a))
    elif boo:
        print('Seu ano de nascimento é ' + str(b - a - 1))
elif x == 51:
    a, b = input('Insira as coordenadas ').split()
    print('A distância da origem é ' + str((int(a) ** 2 + int(b) ** 2) ** (1 / 2)))
elif x == 52:
    a, b, c, p = input('Insira os valores investidos e o valor do prêmio ').split()
    a = float(a)
    b = float(b)
    c = float(c)
    p = float(p)
    print('O valor recebido pelo primeiro amigo será de R$' + str(a / (a + b + c) * p)
          + ' e o valor recebido pelo segundo amigo será de R$' + str(b / (a + b + c) * p)
          + ' e o valor recebido pelo terceiro amigo será de R$' + str(c / (a + b + c) * p))
elif x == 53:
    c, L, p = input('Insira o comprimento, largura e preço por metro da tela ').split()
    c = float(c)
    L = float(L)
    p = float(p)
    print('O preço de cercar este terreno será de R$' + str(2 * (c + L) * p))

