import random 
import time

num_maquina = random.randint(1, 100)
tentativa = 0

while True:
    while True:
        try:
            num_user = int(input('insira o número que você acha que é: '))
            break
        except ValueError:
            print('Você não digitou um valor válido, tente denovo!')
    tentativa= tentativa + 1
    if num_maquina > num_user:
        print('Eeeeeeerrou, é maior.')
    elif num_maquina < num_user:
        print('Foiiii longe, é menor.')
    elif num_maquina == num_user: 
        print('Acertou!!!')

        if tentativa > 1:
            print('Parabéns, você acertou em',tentativa,'tentativas')
            time.sleep(1.5)
            break
        else:
             print('Parabéns, você acertou em',tentativa,'tentativa')
             time.sleep(1.5)
             break