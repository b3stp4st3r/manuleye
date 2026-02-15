import random
import pyfiglet
from .config import console


def get_banner():
    fonts = ["slant", "bloody", "doom", "graffiti", "standard"]
    selected_font = random.choice(fonts)
    banner_text = pyfiglet.figlet_format("MANUL - EYE", font=selected_font)
    console.print(f"[bold orange3]{banner_text}[/bold orange3]")
