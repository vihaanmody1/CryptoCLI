# -- Bring to you by Vihaan Mody
# -- Enjoy the script!

from pyfiglet import figlet_format
from clint.textui import colored
from modules import *

def Banner():
    print(colored.blue(figlet_format("Crypto CLI", "slant")), end = "")
    print(colored.yellow("="*50))
    print(colored.green("\nWelcome To Crypto CLI") + colored.magenta(" 1.0"))

