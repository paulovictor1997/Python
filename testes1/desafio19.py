from random import choice
print('Sorteio para apagar o quadro')

nome1 = input("O nome do primeiro aluno : ")
nome2 = input("O nome do segundo aluno : ")
nome3 = input("O nome do terceiro aluno : ")
nome4 = input("O nome do quarto aluno : ")
alunos = [nome1,nome2,nome3,nome4]
sorteio =choice(alunos)

print('O sorteado foi : {}'.format(sorteio))