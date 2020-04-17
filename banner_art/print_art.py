from pyfiglet import figlet_format
from termcolor import colored

def printArt(msg, color):
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


if __name__ == "__main__":
    printArt()
