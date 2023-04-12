def bemvindo():
    print('Seja Bem Vindo')
    print('Espero que você goste de aprender com esses exercícios práticos')

bemvindo()

nome = str(input("Digite o seu nome: "))
curso = str(input("Digite a linguagem que está sendo utilizada: "))

def bemvindo(nome, curso):
    print(f'Seja Bem Vindo {nome}')
    print(f'Espero que você goste de aprender com esses exercícios práticos de {curso}')

def bemvindo(nome, curso='Python'):
    print(f'Seja Bem Vindo {nome}')
    print(f'Espero que você goste de aprender com esses exercícios práticos de {curso}')

bemvindo('Luis')
bemvindo('Maria')

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)

def calculadora(num1, num2, operação = '+'):
    if operação == '+':
        return num1 + num2
    elif operação == '-':
        return num1 - num2
    
valor = calculadora(3, 4)

print(valor)


