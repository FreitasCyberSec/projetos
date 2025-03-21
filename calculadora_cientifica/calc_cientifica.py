
import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def raiz_quadrada(a):
    return math.sqrt(a)

def potencia(a, b):
    return math.pow(a, b)

# Função principal para interagir com o usuário
def main():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz Quadrada")
    print("6. Potência")
    
    escolha = input("Digite o número da operação (1/2/3/4/5/6): ")
    
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        print(f"{num1} + {num2} = {somar(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    elif escolha == '5':
        num = float(input("Digite um número para calcular a raiz quadrada: "))
        print(f"Raiz quadrada de {num} é {raiz_quadrada(num)}")
    elif escolha == '6':
        num1 = float(input("Digite a base: "))
        num2 = float(input("Digite o expoente: "))
        print(f"{num1} elevado a {num2} é {potencia(num1, num2)}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
