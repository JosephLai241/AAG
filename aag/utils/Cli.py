#===============================================================================
#                           Command-line interface
#===============================================================================
import argparse

from .Titles import Titles

class Parser():
    """
    Methods for parsing CLI arguments.
    """

    ### Initialize objects that will be used on class methods.
    def __init__(self):
        self._usage = "$ AAG.py [-h] [-l] [-e] [-m FONT_NUM TEXT] [-r TEXT]"
        self._description = r"""
Ascii Art Generator - Generate art from 425 fonts

Author: Joseph Lai
"""
        self._epilog = r"""
EXAMPLES

List all available fonts:

    $ ./AAG.py -l

Generate examples for all fonts:

    $ ./AAG.py -e

Create ASCII art using the "larry3d" font:

    $ ./AAG.py -m 211 something

Wrap your text in quotes if it is more than one word or contains special characters:

    $ ./AAG.py -m 211 "ASCII Art Generator"

    $ ./AAG.py -m 330 "H&M"

Generate ASCII art from a random font:

    $ ./AAG.py -r "A random font"
"""

    ### Add parser flags.
    def _add_flags(self, parser):
        aag = parser.add_argument_group("generator options")
        aag.add_argument(
            "-l", "--list",
            action = "store_true",
            help = "list all available fonts and their corresponding number")
        aag.add_argument(
            "-e", "--examples",
            action = "store_true",
            help = "generate examples for each font")
        aag.add_argument(
            "-m", "--make",
            action = "append",
            metavar = "",
            nargs = 2,
            help = "generate ASCII art")
        aag.add_argument(
            "-r", "--randomize",
            action = "append",
            metavar = "",
            help = "generate ASCII art from a random font")

    ### Get args.
    def parse_args(self):
        parser = argparse.ArgumentParser(
            description = self._description,
            epilog = self._epilog,
            formatter_class = argparse.RawDescriptionHelpFormatter,
            usage = self._usage)

        self._add_flags(parser)

        args = parser.parse_args()
        return args, parser

class CheckArgs():
    """
    Method for checking the `-m`/`--make` flag.
    """

    @staticmethod
    def check_make(args, parser):
        for args in args.make:
            try:
                if not args[0].isdigit():
                    raise ValueError
            except ValueError:
                Titles.error_title()
                parser.exit()
