class Fish:

	def __init__(self,name, weight, color):

		self.name = name
		self.weight = weight
		self.color = color

	def status(self):

		print(f"fish: {self.name}, weight: {self.weight} grams, color: {self.color}")

	def feed(self):
		self.weight = self.weight + 2


class Clownfish(Fish):

	def __init__(self,name, weight, color, stripes = False):

		super().__init__(name, weight, color)

		self.stripes = stripes


	def status(self):

		print(f"fish: {self.name}, weight: {self.weight} grams, color: {self.color}, stripes color: {self.stripes}")

	def feed(self):

		if self.stripes:
			self.weight = self.weight + 1


class Tang(Fish):

	def __init__(self,name, weight, color, short_term_memory_loss = False):

		super().__init__(name, weight, color)
		self.short_term_memory_loss = short_term_memory_loss

	def status(self):

		print(f"fish: {self.name}, weight: {self.weight} grams, color: {self.color}, short term memory loss: {self.short_term_memory_loss}")

	def feed(self):

		if self.short_term_memory_loss:
			self.weight = self.weight + 1



class Kong(Fish):

	def __init__(self,name, weight, color):
		super().__init__(name, weight, color)





#clownfish= Kong("dori",10, "blue")


