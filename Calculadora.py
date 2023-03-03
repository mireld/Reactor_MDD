num1 = 5
num2 = 2

def suma(numero1, numero2):
    total = numero1 + numero2
    return total

def resta(numero1, numero2):
    total = numero1 - numero2
    return total

resultado = [suma(num1,num2),resta(num1,num2)]
print('El resultado de la suma es: ', resultado[0], ', y la resta es: ',resultado[1])