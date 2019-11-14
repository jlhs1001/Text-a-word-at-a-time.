import sys
import time
from colorama import Fore, Style


def print1b1(printed, pause_length=0.2, color=Fore.RED):
    if printed.endswith("."):
        pause_length += 0.5
    elif printed.endswith(","):
        pause_length += 0.25
    sys.stdout.write(f'{color} {printed}')
    sys.stdout.flush()
    time.sleep(pause_length)


def print_sentence(sentence, color=Fore.WHITE):
    words = sentence.split()
    for word in words:
        print1b1(word, 0.3, color)
    print('')


'''Print each word, one at a time, with custom colors and custom time'''

print_sentence("let me do my work", Fore.RED)
