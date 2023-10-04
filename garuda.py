import scan
import Honeypot
from cli import Output

msg = (
    "                                                                                         __..-' \n"
    "     ________                         ___                                          _.--''       \n"
    "    /  _____/_____  _______ __ __  __| _/____                            _...__..-'             \n"
    "   /   \  ___\__  \ \_  __ \  |  \/ __ |\__  \                         .'                       \n"
    "   \    \_\  \/ __ \_|  | \/  |  / /_/ | / __ \_                   .'                           \n"
    "    \______  /____  /|__|  |____/\____ |(____  /                 .'                             \n"
    "           \/     \/                  \/     \/                .'                               \n"
    "                                                              |                                 \n"
    "                                    .------._                 ;                                 \n"
    '------MENU-------              .-"""`-.<'
    ")    `-._           .                                 \n"
    "                             (.--. _   `._       `'---.__.-'                                    \n"
    "   1) PORT Scannner           `   `;'-.-'         '-    ._                                      \n"
    "                                .--'``  '._      - '   .                                        \n"
    "   2) HoneyPot                   `"
    "'-.    `---'    ,                                           \n"
    "                         ''--..__      `\"                                                      \n"
    "                                 ``''---'`\      .'                                             \n"
    "                                           `'. '                                                \n"
    "                                             `'.                                                \n"
)

output = Output()


class bold_color:  # Change colours according to your need
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


# I could have replaced the print function with the c_print function
# But it would be a lot of work to replace all the print functions
print("\033[92m")
print(msg)
# Reset the color to default
print("\033[0m")

if __name__ == "__main__":
    menu_option = int(output.ask("Select an option", choices=["1", "2"]))
    if menu_option == 1:
        scan.scanner()
    elif menu_option == 2:
        Honeypot.honey()
else:
    output.c_print("This file is not meant to be imported", code="danger")
