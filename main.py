import random
from time import sleep


def main():
    menu()


def menu():
    selected_option = input("""\nMENU

ESCOLHA UMA OPÇÃO:

[1] - JOGAR
[2] - SAIR

SUA OPÇÃO - """)
    if selected_option == "1":
        play()
    else:
        print("\nOBRIGADO PELA MORAL!")
        exit()


def login():
    sleep(1)
    name = input("\nDIGITE O SEU USUÁRIO: ").upper().strip()
    with open("user_data.txt", "a+"):
        pass
    n = 0
    with open("user_data.txt", "r+") as doc:
        doc_lines = doc.readlines()
        for line in doc_lines:
            if name in line:
                n += 1
                score = int(line.strip().split(";")[1])
                right_words = line.strip().split(";")[2].split(",")
                sleep(1)
                print(f"""\nDADOS:

USUÁRIO: {name}
SCORE TOTAL: {score}
PALAVRAS ACERTADAS: {right_words}""")
                return name, score, right_words, doc_lines
    if n == 0:
        score = 0
        right_words = []
        with open("user_data.txt", "a+") as doc:
            doc.write(f"{name};{score};\n")
        sleep(1)
        print(f"""\nDADOS:

NOVO USUÁRIO!
USUÁRIO: {name}
SCORE TOTAL: {score}
PALAVRAS ACERTADAS: {right_words}""")
        return name, score, right_words, doc_lines


def play():
    name, score, right_words, doc_lines = login()
    life = 6
    words_list = []
    tried_letters = []
    with open("banco_de_palavras.txt", "r") as doc:
        lines = doc.readlines()
        for line in lines:
            words_list.append(line.split(";"))
    for i, v in enumerate(words_list):
        if i != len(words_list) - 1:
            words_list[i][1] = words_list[i][1][0:len(words_list[i][1]) - 1]
    while True:
        n = random.randint(0, len(words_list) - 1)
        word = words_list[n][0].upper()
        if len(right_words) == len(words_list):
            sleep(1)
            print("\nNÃO EXISTEM MAIS PALAVRAS JOGÁVEIS, AGUARDE A PRÓXIMA ATUALIZAÇÃO!")
            sleep(1)
            print("\nOBRIGADO PELA MORAL!")
            with open("user_data.txt", "r") as doc:
                doc_lines = doc.readlines()
            for line in doc_lines:
                if line.split(";")[0] == name:
                    doc_lines.pop(doc_lines.index(line))
            doc_lines = "".join(doc_lines)
            with open("user_data.txt", "w") as doc:
                doc.write(doc_lines)
            sleep(1)
            print(f'\nUSUÁRIO "{name}" EXCLUÍDO!')
            exit()
        if word in right_words:
            continue
        l_shadow_w = []
        for ltr in word:
            if ltr.isalnum():
                l_shadow_w.append("#")
            elif ltr == " ":
                l_shadow_w.append("-")
        shadow_word = "".join(l_shadow_w)
        tip = words_list[n][1].upper()
        c = True
        if c:
            sleep(1)
            print("\nA RODADA COMEÇARÁ EM INSTANTES...")
            sleep(1)
            c = False
        while True:
            sleep(1)
            letter = input(f"""\nVOCÊ AINDA POSSUI {life} TENTATIVA(S)!

EIS A PALAVRA ESCOLHIDA PARA A RODADA: {shadow_word}.

A DICA PARA A PALAVRA É A SEGUINTE: {tip}.

TENTE UMA LETRA: """).upper()
            if letter not in tried_letters:
                tried_letters.append(letter)
                if letter in word:
                    score = int(score) + 10
                    for i, v in enumerate(word):
                        if v == letter:
                            list_shadow_w = list(shadow_word)
                            list_w = list(word)
                            list_shadow_w[i] = list_w[i]
                            shadow_word = "".join(list_shadow_w)
                else:
                    life -= 1
            else:
                sleep(1)
                print("\nVOCÊ JÁ TENTOU ESSA LETRA!")
                continue
            if "#" not in shadow_word:
                life = 6
                sleep(1)
                print(f"\nVOCÊ VENCEU ESSA RODADA! A PALAVRA ESCOLHIDA FOI {word}!")
                right_words.append(word)
                save_str = f"{name};{score};{','.join(right_words)}\n"
                
                with open("user_data.txt", "r") as doc:
                    doc_lines = doc.readlines()
                for line in doc_lines:
                    if line.split(";")[0] == name:
                        doc_lines[doc_lines.index(line)] = save_str
                save_str = "".join(doc_lines)
                with open("user_data.txt", "w") as doc:
                    doc.write(save_str)
                tried_letters.clear()
                break
            if life == 6:
                sleep(1)
                print('\n┌───┐')
                print('│')
                print('│')
                print('│')
                print('│')
            if life == 5:
                sleep(1)
                print('\n┌───┐')
                print('│   😐')
                print('│')
                print('│')
                print('│')
            if life == 4:
                sleep(1)
                print('\n┌───┐')
                print('│   😐')
                print('│   ░  ')
                print('│')
                print('│')
            if life == 3:
                sleep(1)
                print('\n┌───┐')
                print('│   😐')
                print('│   ░╲ ')
                print('│')
                print('│')
            if life == 2:
                sleep(1)
                print('\n┌───┐')
                print('│   😐')
                print('│  ╱░╲ ')
                print('│')
                print('│')
            if life == 1:
                sleep(1)
                print('\n┌───┐')
                print('│   😐')
                print('│  ╱░╲ ')
                print('│  ╱   ')
                print('│')
            if life == 0:
                sleep(1)
                print('\n┌───┐')
                print('│   😐')
                print('│  ╱░╲ ')
                print('│  ╱ ╲ ')
                print('│')
                print(f"\nVOCÊ PERDEU! MAIS SORTE NA PRÓXIMA...")
                life = 6
                tried_letters.clear()
                break
        sleep(1)
        print(f"""\nPLACAR:

NOME: {name}
SCORE TOTAL: {score}
PALAVRAS ACERTADAS: {right_words}""")
        option = input("""\nDESEJA JOGAR UMA NOVA RODADA?
        
[1] - SIM
[2] - NÃO

SUA OPÇÃO - """)
        if int(option) == 1:
            continue
        else:
            sleep(1)
            menu()


if __name__ == '__main__':
    main()
