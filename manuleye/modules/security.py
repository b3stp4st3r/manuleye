import subprocess
from rich.prompt import Prompt
from manuleye.core import console

try:
    import instaloader
except ImportError:
    instaloader = None


def sqlmap_scan():
    target = Prompt.ask("Target URL (e.g. http://site.com/page.php?id=1)")
    console.print(f"[cyan][*] Starting SQLMap scan on: {target}...[/cyan]")
    console.print("[yellow][!] This may take a while...[/yellow]\n")
    try:
        subprocess.run(f"sqlmap -u {target} --batch --banner", shell=True, timeout=600)
    except subprocess.TimeoutExpired:
        console.print("[red][!] SQLMap timeout (10 min limit)[/red]")
    except FileNotFoundError:
        console.print("[red][!] SQLMap not found. Install: pip install sqlmap-python[/red]")
        console.print("[yellow]Or download from: https://sqlmap.org/[/yellow]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")


def xss_scan():
    target = Prompt.ask("Target URL")
    console.print(f"[cyan][*] Starting XSStrike scan on: {target}...[/cyan]\n")
    try:
        subprocess.run(f"xsstrike -u {target}", shell=True, timeout=300)
    except subprocess.TimeoutExpired:
        console.print("[red][!] XSStrike timeout (5 min limit)[/red]")
    except FileNotFoundError:
        console.print("[red][!] XSStrike not found. Install: pip install xsstrike[/red]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")


def instagram_osint():
    username = Prompt.ask("Instagram Username")
    if instaloader is None:
        console.print("[red][!] instaloader not installed. Run: pip install instaloader[/red]")
        input("\n[Press Enter]")
        return
    
    console.print(f"[cyan][*] Fetching data for @{username}...[/cyan]\n")
    
    try:
        from rich.table import Table
        
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
