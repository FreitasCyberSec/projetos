
def converter_moeda(valor, de, para):
    taxas_de_conversao = {
        ('BRL', 'USD'): 0.20,
        ('USD', 'BRL'): 5.15,
        ('BRL', 'EUR'): 0.18,
        ('EUR', 'BRL'): 5.55,
        # Adicione mais taxas de conversão conforme necessário
    }

    chave = (de, para)
    
    if chave not in taxas_de_conversao:
        return "Conversão não disponível para essas moedas."

    taxa = taxas_de_conversao[chave]
    return valor * taxa


def main():
    print("Bem-vindo ao Conversor de Moeda!")

    valor = float(input("Digite o valor a ser convertido: "))
    de = input("Digite a moeda de origem (BRL, USD, EUR): ").upper()
    para = input("Digite a moeda de destino (BRL, USD, EUR): ").upper()

    resultado = converter_moeda(valor, de, para)

    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"{valor} {de} é igual a {resultado:.2f} {para}.")


if __name__ == "__main__":
    main()
