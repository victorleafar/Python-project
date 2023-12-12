import random
import os

MAX_TENTATIVAS = 6

palavra = ""
dicaPalavra = ""
tamanho = 0
nomeVencedor = ''


class Jogador():
    def __init__(self, name: str):
        self.name = name
        self.tentativas_restantes = MAX_TENTATIVAS
        self.adivinhacao = ""
        self.jogo_continua = True


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def desenharArvore(tentativas):
    if tentativas >= 6:
        print("  _______\n"
              " |/      |\n"
              " |\n"
              " |\n"
              " |\n"
              " |\n"
              "_|___")
    elif tentativas == 5:
        print("  _______\n"
              " |/      |\n"
              " |      (_)\n"
              " |\n"
              " |\n"
              " |\n"
              "_|___")
    elif tentativas == 4:
        print("  _______\n"
              " |/      |\n"
              " |      (_)\n"
              " |       |\n"
              " |       |\n"
              " |\n"
              "_|___")
    elif tentativas == 3:
        print("  _______\n"
              " |/      |\n"
              " |      (_)\n"
              " |       |\n"
              " |       |\n"
              " |      /\n"
              "_|___")
    elif tentativas == 2:
        print("  _______\n"
              " |/      |\n"
              " |      (_)\n"
              " |       |\n"
              " |       |\n"
              " |      / \\\n"
              "_|___")
    elif tentativas == 1:
        print("  _______\n"
              " |/      |\n"
              " |      (_)\n"
              " |      /|\n"
              " |       |\n"
              " |      / \\\n"
              "_|___")
    else:
        print("  _______\n"
              " |/      |\n"
              " |      (_)\n"
              " |      /|\\\n"
              " |       |\n"
              " |      / \\\n"
              "_|___")

def definirPalavra():
    global palavra, dicaPalavra

    db_palavras = [
        ['Fruta', 'Laranja'],
        ['Fruta', 'Abacaxi'],
        ['Fruta', 'Melancia'],
        ['Animal', 'Cachorro'],
        ['Animal', 'Gato'],
        ['Animal', 'Rinoceronte'],
        ['Animal', 'Rinoceronte'],
        ['Cor', 'Vermelho'],
        ['Cor', 'Verde'],
        ['Cor', 'Roxo'],
        ['Cor', 'Amarelo'],
        ['País', 'Venezuela'],
        ['País', 'Hungria'],
        ['País', 'Eslovaquia'],
    ]
    escolhido = random.choice(db_palavras)
    dicaPalavra = escolhido[0]
    palavra = escolhido[1].lower()


def jogar(player: Jogador):
    global palavra, tamanho, nomeVencedor

    tamanho = len(palavra)

    player.adivinhacao = "_" * tamanho

    while player.jogo_continua:
        clear_screen()
        print(f"{player.name}, tente adivinhar a palavra (DICA: {dicaPalavra}): {player.adivinhacao}")

        print(f"Você tem {player.tentativas_restantes} tentativas restantes.")

        letra = input("Digite uma letra: ")

        encontrou = False
        if letra in palavra:
            for i in range(tamanho):
                if palavra[i].lower() == letra.lower():
                    player.adivinhacao = player.adivinhacao[:i] + letra + player.adivinhacao[i + 1:]
                    encontrou = True
            if encontrou:
                print(f"Letra correta!")
        else:
            print(f"A letra '{letra}' não faz parte da palavra.")
            player.tentativas_restantes -= 1
            if player.tentativas_restantes == 0:
                player.jogo_continua = False

        desenharArvore(player.tentativas_restantes)
        print(f"Palavra: {player.adivinhacao}")

        if palavra.lower() == player.adivinhacao.lower():
            nomeVencedor = player.name
            player.jogo_continua = False

    clear_screen()
    if len(nomeVencedor) > 0:
        print(f"Parabéns {nomeVencedor}, você venceu! A palavra era {palavra}.")
    else:
        print(f"Você perdeu! A palavra era {palavra}.")


def main():
    clear_screen()
    definirPalavra()
    player_nome = input("Digite seu nome: ")
    jogador = Jogador(player_nome)
    jogar(jogador)


if __name__ == "__main__":
    main()
