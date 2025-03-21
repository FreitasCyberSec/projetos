
def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    for col in range(3):
        if all([tabuleiro[linha][col] == jogador for linha in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogadores[jogador_atual]} - Faça sua jogada")
        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))
        
        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada! Tente novamente.")
            continue
        
        tabuleiro[linha][coluna] = jogadores[jogador_atual]
        
        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogadores[jogador_atual]} venceu!")
            break
        
        jogador_atual = 1 - jogador_atual  # Alterna entre 0 e 1

if __name__ == "__main__":
    jogar()
