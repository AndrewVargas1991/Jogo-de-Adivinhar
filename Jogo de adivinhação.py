from random import randrange

n = randrange(1000)
t = 0
print('Digite um numero entre 0 e 1000: ', end='')

while True:
	v = int(input())
	if n == v:
		t += 1
		print(f'Voce ACERTOU na {t}ª tentativa!')
		break
	print('MENOR, digite outro numero: ' if (n < v) else ('MAIOR, digite outro numero: '), end='')
	t += 1

input('\nAperte ENTER para sair...')
