def calculadora(num1, num2, operação = '+'):
    if operação == '+':
        return num1 + num2
    elif operação == '-':
        return num1 - num2
    elif operação == '*':
        return num1 * num2
    elif operação == '/':
        return num1/num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
sinal = str(input("Digite o sinal da operação matemática que deseja fazer: "))
    
resultado = calculadora(num1, num2, sinal)

print(resultado)
