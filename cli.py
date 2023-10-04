"""

"""

from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.prompt import Prompt, Confirm
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table

# These are the colors that will be used for the output
# If you want to tweak the style of the output, you can change these
theme = Theme(
    {
        "info": "cyan",
        "warning": "yellow",
        "danger": "red",
        "success": "green",
        "normal": "",
    }
)


# The main output class
# This is class that controls the rich output of the program
class Output:
    def __init__(self) -> None:
        self.console = Console(theme=theme)
        self.prompt = Prompt(console=self.console)
        self.table = Table()

    def colored_text(self, text: str, color: str) -> Text:
        return Text(text, style=color)
    
    def log(self, text: str) -> None:
        self.console.log(text)

    # The updated print function
    # The Code can be one of the following: info, warning, danger, success, normal
    # Default is normal if no code is specified
    def c_print(self, text="", code="normal", color=None):
        if color is not None:
            self.console.print(text, style=color)
        else:
            self.console.print(text, style=code)

    # The updated input function
    # This is used to give a nice list of options to the user
    def ask(self, msg: str, color=None, choices=None, default=""):
        # Only ask for a default if one is specified
        if default != "":
            return self.prompt.ask(
                self.colored_text(msg, color), choices=choices, default=default
            )
        else:
            return self.prompt.ask(msg, choices=choices)

    # The default is False if no default is specified
    def confirm(self, msg: str, default=False):
        return Confirm.ask(msg, default=default)

    # Print a options in a nice column
    # This helps it stand out from the rest of the output
    def show_options(self, options) -> str:
        columns = Columns(options, equal=True, expand=True)
        self.c_print(str(columns))
        return self.ask("Select an option", options)

    def show_panel(self, title: str, content=None, color=None):
        panel = Panel.fit(content, title=title, border_style=color)
        self.console.print(panel)