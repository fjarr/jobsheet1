import random

class Tangka:
	def __init__(self):
		self.tebakan = 0
		self.jawaban = random.randint(1,3)

	def cek(self):
		if self.jawaban == self.tebakan:
			return True
		return False