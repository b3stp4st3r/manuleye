import requests
from packaging import version
from manuleye import __version__
from manuleye.core import console


def check_version():
    try:
        console.print("[cyan][*] Checking for updates...[/cyan]")
        
        response = requests.get("https://pypi.org/pypi/manuleye/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            latest_version = data['info']['version']
            current_version = __version__
            
            console.print(f"[cyan]Current version: {current_version}[/cyan]")
            console.print(f"[cyan]Latest version: {latest_version}[/cyan]")
            
            if version.parse(latest_version) > version.parse(current_version):
                console.print(f"\n[yellow]⚠️  New version available: {latest_version}[/yellow]")
                console.print("[green]Update with: pip install --upgrade manuleye[/green]")
                return False
            else:
                console.print("\n[green]✓ You are using the latest version![/green]")
                return True
        else:
            console.print("[yellow][!] Could not check for updates[/yellow]")
            return None
    except Exception as e:
        console.print(f"[yellow][!] Update check failed: {e}[/yellow]")
        return None


def show_version_info():
    from rich.panel import Panel
    from rich.table import Table
    
    table = Table(show_header=False, box=None)
    table.add_column(style="cyan", width=20)
    table.add_column(style="white")
    
    table.add_row("Version:", __version__)
    table.add_row("Package:", "manuleye")
    table.add_row("PyPI:", "https://pypi.org/project/manuleye/")
    table.add_row("GitHub:", "https://github.com/b3stp4st3r/manuleye")
    table.add_row("Author:", "Daniil Pentium")
    
    console.print(Panel(table, title="[bold cyan]MANUL-EYE Version Info[/bold cyan]", border_style="cyan"))
    
    check_version()
    
    input("\n[Press Enter]")
