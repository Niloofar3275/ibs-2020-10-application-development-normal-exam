from Fish import *

class Aquarium:

	def __init__(self):

		self.fishes = []


	def add_fish(self, fish):

		self.fishes.append(fish)
		print(f"{fish.name} was added to aquarium.")

	def remove_fish(self):

		for fish in self.fishes:

			if fish.weight > 10:
				del self.fishes[self.fishes.index(fish)]
				print(f"{fish.name} was a big fish and it was removed.")


	def feed(self):
		for fish in self.fishes:
			fish.feed()

		print("All fishes were fed.")

	def getStatus(self):
		
		print("\n")

		for fish in self.fishes:
			fish.status()

		




aquarium = Aquarium()
kong= Kong("Dori",10, "blue")
tang = Tang("Bubbles", 7, "green", True)
clownfish = Clownfish("Nemo", 5, "red","white")

aquarium.add_fish(kong)
aquarium.add_fish(tang)
aquarium.add_fish(clownfish)


aquarium.getStatus()
aquarium.feed()
aquarium.remove_fish()
aquarium.getStatus()









