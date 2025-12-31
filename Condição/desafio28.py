import random
import pygame
print('Jogo da advinhação')
num = int(input('Adivinhe o número que eu estou pensando entre 0 e 5 : '))
numero = random.randint(0,5)
if num == numero:
    print('O número foi {}, parabéns você acertou !!!'.format(num))
    pygame.mixer.init()
    pygame.mixer.music.load('faustaoacertou.mp3')
    pygame.mixer.music.play()
    input()

else:
    print(f'Você errou o número que pensei foi o {numero}, tente de novo !')
    pygame.mixer.init()
    pygame.mixer.music.load('faustao.mp3')
    pygame.mixer.music.play()
    input()

