
import random
import string

def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Função principal para interagir com o usuário
def main():
    comprimento = int(input("Digite o comprimento desejado para a senha: "))
    senha = gerar_senha(comprimento)
    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()
