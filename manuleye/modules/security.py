import subprocess
from rich.prompt import Prompt
from manuleye.core import console


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

