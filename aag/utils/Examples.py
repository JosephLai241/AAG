#===============================================================================
#                       Generate examples for each font
#===============================================================================
from .Fonts import FONTS
from .Make import Make

class Examples():
    """
    Method for generating examples for each font.
    """

    ### Generate examples.
    @staticmethod
    def generate_examples():
        for number, font in FONTS.items():
            print("%s: %s" % (number, font))
            Make.make(font, "Example")
