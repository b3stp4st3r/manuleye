import requests
from rich.table import Table
from manuleye.core import console

try:
    import instaloader
except ImportError:
    instaloader = None


def instagram_search(username):
    if instaloader is None:
        console.print("[red][!] instaloader not installed. Run: pip install instaloader[/red]")
        input("\n[Press Enter]")
        return
    
    console.print(f"[cyan][*] Fetching data for @{username}...[/cyan]\n")
    
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)
        
        table = Table(title=f"Instagram: @{username}", border_style="orange3")
        table.add_column("Field", style="bold white")
        table.add_column("Value", style="green")
        
        table.add_row("User ID", str(profile.userid))
        table.add_row("Full Name", profile.full_name)
        table.add_row("Biography", profile.biography[:100] if profile.biography else "N/A")
        table.add_row("Followers", str(profile.followers))
        table.add_row("Following", str(profile.followees))
        table.add_row("Posts", str(profile.mediacount))
        table.add_row("Is Private", str(profile.is_private))
        table.add_row("Is Verified", str(profile.is_verified))
        table.add_row("Is Business", str(profile.is_business_account))
        
        if profile.external_url:
            table.add_row("External URL", profile.external_url)
        
        console.print(table)
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")
