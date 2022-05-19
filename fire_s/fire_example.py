#!/usr/bin/env python

import fire

class Ships():
	def sail(self):
		ship_name = 'Your ship'
		print(f"{ship_name} is setting sail")

	def list(self):
		ships = ['Johb B', 'Yankee Clipper', 'Pequod']
		print(f"Ships: {','.join(ships)}")

def sailors(greeting, name):
	message = f'{greeting} {name}'
	print(message)

class Cli():
	def __init__(self):
		self.sailors = sailors
		self.ships = Ships()

if __name__ == '__main__':
	fire.Fire(Cli)

# python fire_example.py -- --interactive

