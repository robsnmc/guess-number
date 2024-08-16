import random
import os

numero = random.randint(1, 100)

tentativas = 0

dificuldade = int(input("1 - Fácil\n2 - Médio\n3 - Difícil\n\n"))

max_tentativas = 0

def clear():
    if os.name == 'nt':
        os.system('cls')

clear()

while True: 
    tentativas += 1

    if dificuldade == 1:
        max_tentativas = 15
    elif dificuldade == 2:
        max_tentativas = 10
    else:
        dificuldade == 3
        max_tentativas = 5

    if tentativas > max_tentativas:
        print("Suas chances acabaram")
        break

    pergunta = int(input("Escolha um número entre 1 e 100: "))

    if pergunta < numero:
        print("+")

    elif pergunta > numero:
        print("-")

    else:
        pergunta == numero
        print("🎉")
        break