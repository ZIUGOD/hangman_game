from os import system, name
from utils.data import *
from random import choice
from time import sleep


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def press_enter():
    input("Pressionte `ENTER` para continuar.")
    clear()


def header():
    print(
        f"{color['warning']}Dica sobre as palavras sorteadas:{color['end']}\n"
        f"As palavras fáceis são menores e com letras mais comuns,\n"
        f"enquanto as mais difíceis são maiores com letras menos comuns.\n"
    )


def pick_difficulty():
    clear()
    while True:
        try:
            header()
            value = int(
                input(
                    f"{color['green']}[1] - Fácil\n"
                    f"{color['warning']}[2] - Média\n"
                    f"{color['red']}[3] - Difícil{color['end']}\n\n"
                    f"Opção: "
                )
            )

            clear()

            if value in range(1, 4):
                return value
            else:
                print(
                    f"{color['red']}[Erro] - Insira apenas valores entre 1 e 3.{color['end']}"
                )
                press_enter()
                continue

        except ValueError:
            clear()
            print(
                f"{color['red']}[Erro] - Insira apenas valores inteiros.{color['end']}"
            )
            press_enter()
            continue


def hangmanGame():
    clear()
    print(f"{color['green']}Olá! Bem-vindo ao jogo da forca do ZIUGOD!{color['end']}")
    press_enter()

    game_difficulty = pick_difficulty()
    sorted_word = choice(game_vocab[game_difficulty - 1])

    guessed_letters = []
    current_word = "_" * len(sorted_word)

    while "_" in current_word and len(guessed_letters) < 6:  # limite de 6 tentavias
        print(
            f"Dificuldade escolhida: {difficulties[game_difficulty - 1]}\n"
            f"Letras escolhidas: {', '.join(guessed_letters)}\n\n"
            f"Palavra: {current_word}  ({len(sorted_word)} letras)"
        )

        guess = input("\nInsira uma letra: ").lower()
        clear()

        if len(guess) != 1:
            print(
                f"{color['red']}[Erro] - É necessário inserir pelo menos uma letra.{color['end']}"
            )
            continue

        if len(guess) > 1:
            print(
                f"{color['red']}[Erro] - Favor, insira apenas uma letra por vez!{color['end']}"
            )
            press_enter()
            continue

        if not guess.isalpha():
            print(
                f"{color['red']}[Erro] - Favor, insira uma letra válida!{color['end']}"
            )
            press_enter()
            continue

        if guess in guessed_letters:
            print(f"{color['warning']}Você já escolheu esta letra.{color['end']}")
            press_enter()
            continue

        if guess in sorted_word:
            clear()
            new_word = [len(sorted_word)]
            for i in range(len(sorted_word)):
                if sorted_word[i] == guess:
                    current_word[i] = sorted_word[i]
                else:
                    new_word += current_word[i]
            current_word = new_word
        else:
            guessed_letters.append(guess)

    # fim de jogo #
    if "_" not in current_word:
        print(
            f"{color['green']}Parabéns!! Você venceu!!{color['end']}\n"
            f"A palavra era: {sorted_word}\n"
        )
        sleep(2)
        play_again()

    else:
        print(
            f"{color['red']}Você perdeu. A palavra sorteada foi: {sorted_word}{color['end']}\n"
        )
        sleep(2)
        play_again()


def play_again():
    while True:  # Loop para lidar com a decisão do jogador
        try:
            play_choice = int(
                input(
                    f"Gostaria de jogar novamente?\n"
                    f"[1] - Sim\n"
                    f"[2] - Não\n\n"
                    f"Opção: "
                )
            )

            if play_choice == 1:
                hangmanGame()
            elif play_choice == 2:
                clear()
                print(
                    f"{color['green']}Obrigado por jogar! Até a próxima. :)\n{color['end']}"
                )
                break
            else:
                clear()
                print(
                    f"{color['red']}[Erro] - Insira apenas os valores `1` ou `2`.{color['end']}"
                )
                press_enter()

        except ValueError:
            print(
                f"{color['red']}[Erro] - Insira apenas os valores `1` ou `2`.{color['end']}"
            )
            press_enter()


if __name__ == "__main__":
    hangmanGame()
