#!/usr/bin/env python

import sys

def say_it(greeting: str, target: str):
	message = f'{greeting} {target}'
	print(message)

if __name__ == '__main__':
	greeting = 'Hello'
	target = 'Joe'

	if '--help' in sys.argv:
		help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
		print(help_message)
		sys.exit()

	if '--greeting' in sys.argv:
		greeting_index = sys.argv.index('--greeting') + 1

