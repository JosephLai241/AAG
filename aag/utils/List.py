#===============================================================================
#                           List all available fonts
#===============================================================================
from prettytable import PrettyTable

from .Fonts import FONTS

class List():
    """
    Method for listing all fonts with their corresponding numbers.
    """

    @staticmethod
    def print_fonts():
        pretty_fonts = PrettyTable()
        pretty_fonts.field_names = ["Number", "Font"]

        for number, font in FONTS.items():
            pretty_fonts.add_row([number, font])

        pretty_fonts.align = "l"
        print(pretty_fonts)
