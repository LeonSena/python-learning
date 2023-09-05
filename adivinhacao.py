print("************************************")
print("BEM-VINDO(A) AO JOGO DE ADIVINHAÇÃO!")
print("************************************")

numero_secreto = 29
total_tentativas = 3
rodada = 1

for rodada in range (1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite o seu palpite entre 1 e 100: ")
    print("você chutou o numero..." , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue


    
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto


    if(acertou):
        print("Você acertou!!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


print("Fim do jogo")