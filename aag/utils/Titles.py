#===============================================================================
#                               Titles for AAG
#===============================================================================
from colorama import Fore, init, Style

### Automate sending reset sequences to turn off color changes at the end of 
### every print.
init(autoreset = True)

class Titles():
    """
    Methods for printing titles.
    """

    ### Print the main title.
    @staticmethod
    def title():
        print(Fore.BLUE + Style.BRIGHT + r"""
____________________________
________    |__    |_  ____/
_______  /| |_  /| |  / __  
______  ___ |  ___ / /_/ /  
     /_/  |_/_/  |_\____/   
____________________________
""")

    ### Print the randomize title.
    @staticmethod
    def random_title():
        print(Fore.YELLOW + Style.BRIGHT + r"""
_____________
_______  ___/
______  /    
     /_/     
_____________     
""")

    ### Print the error title.
    @staticmethod
    def error_title():
        print(Fore.RED + Style.BRIGHT + r"""
__________ 
______  _ \
     /  __/
     \___/... Please recheck font selection (1-425).   
""")
