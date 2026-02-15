"""Configuration and constants for MANUL-EYE."""

from rich.console import Console

# Console instance
console = Console()

# Required Python libraries
REQUIRED_LIBS = [
    "requests",
    "rich",
    "pyfiglet",
    "Pillow",
    "phonenumbers",
    "pypdf",
    "mutagen",
    "python-docx",
    "openpyxl",
    "instaloader"
]

# External command-line tools
EXTERNAL_TOOLS = ["maigret", "holehe"]

# API endpoints
API_ENDPOINTS = {
    'ip_lookup': 'http://ip-api.com/json/',
}
