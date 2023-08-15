import random
from guess import Tangka

tebak = Tangka()
tebak.jawaban = random.randint(1, 3)
while True:
	tebak.tebakan = int(input('tebak angka 1 s.d 3:  '))
	if tebak.cek():
		print("TEBAKAN KAMU BENAR SEKALI")
		break
	else:
		print("TEBAKAN KAMU SALAH")