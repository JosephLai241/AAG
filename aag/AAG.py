#!/usr/bin/python
"""
Created on Sun Jul 19 17:17:24 2020

ASCII art generator.

@author: Joseph Lai
"""
import random

from pyfiglet import Figlet

from utils.Cli import CheckArgs, Parser
from utils.Examples import Examples
from utils.Fonts import FONTS
from utils.List import List
from utils.Make import Make
from utils.Titles import Titles

class Main():
    """
    Putting it all together
    """

    @staticmethod
    def main():
        args, parser = Parser().parse_args()

        ### List all fonts with their corresponding number.
        if args.list:
            Titles.title()
            List.print_fonts()

        ### Generate examples for all fonts.
        elif args.examples:
            Titles.title()
            Examples.generate_examples()

        ### Generate ASCII art based on the selected font and entered string.
        elif args.make:
            CheckArgs.check_make(args, parser)

            for args in args.make:
                Make.make(FONTS[int(args[0])], args[1])

        ### Generate ASCII art from a random font and entered string.
        elif args.randomize:
            Titles.random_title()
            Make.make(FONTS[random.randint(1,426)], args.randomize)

if __name__ == "__main__":
    Main.main()
