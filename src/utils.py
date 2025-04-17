"""
Provide different methods to have colorful prints.
"""
from termcolor import colored


def print_yellow(text):
    print(colored(text, 'yellow', attrs=['reverse']))


def print_info(text):
    print(colored(text, 'white', attrs=['reverse']))


def print_lose(text):
    print(colored(text, 'red', attrs=['blink', 'reverse']))


def print_win(text):
    print(colored(text, 'green', attrs=['blink', 'reverse']))
