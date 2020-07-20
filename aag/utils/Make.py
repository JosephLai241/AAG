#===============================================================================
#                               Make ASCII art
#===============================================================================
from pyfiglet import Figlet

class Make():
    """
    Method for making ASCII art.
    """

    ### Generate ASCII art.
    @staticmethod
    def make(font, text):
        banner = Figlet(font = font)
        print("\n%s" % banner.renderText(text))
