"""Banner and UI elements for MANUL-EYE."""

import random
import pyfiglet
from .config import console


def get_banner():
    """Display random ASCII art banner."""
    fonts = ["slant", "bloody", "banner3", "doom", "graffiti", "standard"]
    selected_font = random.choice(fonts)
    banner_text = pyfiglet.figlet_format("MANUL - EYE", font=selected_font)
    console.print(f"[bold orange3]{banner_text}[/bold orange3]")
    console.print(f"[dim]Font: {selected_font}[/dim]\n")
