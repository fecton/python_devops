#!/usr/bin/env python

import fire

def greet(greeting='Hiya', name='Tammy'):
	print(f"{greeting} {name}")

def goodbye(goodbye='Hiya', name='Tammy'):
	print(f"{goodbye} {name}")


if __name__ == "__main__":
	fire.Fire(greet)




