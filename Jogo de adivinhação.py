from random import randrange

n = randrange(1000)
print('Digite um numero entre 0 e 1000: ', end='')

while True:
	v = int(input())
	if n == v:
		print('Voce ACERTOU!')
		break
	print('MENOR, digite outro numero: ' if (n < v) else ('MAIOR, digite outro numero: '))

input('\nAperte ENTER para sair...')