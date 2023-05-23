test = 'hello world'
print(f"Oh, {test}") # printar incluindo uma variável
print(test) # printar somente variável
print("Hello World") # printar somente string
print(test[::-1]) # "velocidade" de impressão, número é a cada quantas index serão lidas, sinal é o sentido
print(test[0:4]) # slice, [start:end]
print(test.replace('l', 'j')) # troca uma letra pela outra, caseSensitive
print(test.split()) # transforma string de várias palavras em lista com strings
print('p'.join(test))
