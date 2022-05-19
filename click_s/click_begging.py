#!/usr/bin/env python

import click

@click.command()
@click.option('--greeting', default='Hiya', help='How do you want to grret?')
@click.option('--name', default='Tammy', help='Who do you want to greet!')
def greet(greeting, name):
	print(f"{greeting} {name}")


if __name__ == "__main__":
	greet()

