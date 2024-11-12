import pyfiglet
from colorama import Fore, Back, Style, init
init()
print(Fore.RED + "Vermelho")
print(Fore.GREEN+ "GREEN")
print(Fore.BLUE+ "BLUE")

print(Style.RESET_ALL + "Texto na cor padrão")

ascii_art = pyfiglet.figlet_format("PYTHON", font="block")
print(Fore.RED + ascii_art)
