#!/usr/bin/env python3
import click




@click.group()
def cli() -> None:
    pass


@cli.command(help='Very useful links!')
def giveLinks() -> None:
    print("[+] Very useful links!")
    print("Google\thttps://google.com")
    print("Xakep\thttps://xakep.ru", end='\n'*2)


@cli.command(help='Very useful advices!')
def giveAdvices() -> None:
    print("[+] Very useful advices!")
    print("* Do not try to learn everything in a day split it out and chill")
    print("* Do not compare yourself with others it is bad only for you")
    print("* Do not do what is not joyful for you")


@cli.command(help='Very useful advices and links!')
def all() -> None:
    print("[+] Very useful links!")
    print("Google\thttps://google.com")
    print("Xakep\thttps://xakep.ru", end='\n'*2)

    print("[+] Very useful advices!")
    print("* Do not try to learn everything in a day split it out and chill")
    print("* Do not compare yourself with others it is bad only for you")
    print("* Do not do what is not joyful for you")


if __name__ == '__main__':
    cli()
 

