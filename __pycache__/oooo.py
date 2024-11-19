from colorama import Fore, init, Back


init()

cores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE, Fore.BLACK +Back.WHITE]

for cor in cores:
    print(cor + "Texto colorido com Colorama!")
