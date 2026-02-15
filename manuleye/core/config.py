from rich.console import Console

console = Console()

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

EXTERNAL_TOOLS = ["maigret", "holehe"]

API_ENDPOINTS = {
    'ip_lookup': 'http://ip-api.com/json/',
}
