import sys

def giveLinks() -> None:
    print("[+] Very useful links!")
    print("Google\thttps://google.com")
    print("Xakep\thttps://xakep.ru", end='\n'*2)

def giveAdvices() -> None:
    print("[+] Very useful advices!")
    print("* Do not try to learn everything in a day split it out and chill")
    print("* Do not compare yourself with others it is bad only for you")
    print("* Do not do what is not joyful for you")

argv = sys.argv

if(len(sys.argv) == 1):
    argv = ['-h']
else:
    argv = argv[1:]

if(argv[0] in ['-h','--help']):
    print("[?] It's a help message!")
    print('\t- First argument: a neccessary theme',end='\n'*2)
    print('[?] Examples:')
    print('\t-l\tlinks only')
    print('\t-a\tadvices only')
    print('\t-E\teverything', end='\n'*2)
    exit(0)

if(argv[0] == '-l'):
    giveLinks()
elif(argv[0] == '-a'):
    giveAdvices()
elif(argv[0] == '-E'):
    giveLinks()
    giveAdvices()
else:
    print('[!] Invalid argument!', end='\n'*2)


