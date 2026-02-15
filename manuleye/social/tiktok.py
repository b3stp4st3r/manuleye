"""TikTok OSINT module."""

import requests
from rich.table import Table
from manuleye.core import console


def tiktok_search(username):
    """
    Search for TikTok user information.
    
    Args:
        username: TikTok username (without @)
    """
    console.print(f"[cyan][*] Searching TikTok for: @{username}...[/cyan]")
    
    # Remove @ if present
    username = username.lstrip('@')
    
    table = Table(title=f"TikTok: @{username}", border_style="orange3")
    table.add_column("Parameter", style="bold white")
    table.add_column("Value", style="green")
    
    try:
        # Check if profile exists
        url = f"https://www.tiktok.com/@{username}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            table.add_row("Profile URL", url)
            table.add_row("Status", "✓ Profile exists")
            
            content = response.text
            
            # Try to extract basic info from HTML
            # Note: TikTok uses heavy JavaScript, so full scraping requires selenium
            
            if '"uniqueId":"' in content:
                table.add_row("Username", f"@{username}")
            
            # Extract nickname if available
            if '"nickname":"' in content:
                nick_start = content.find('"nickname":"') + 12
                nick_end = content.find('"', nick_start)
                if nick_start > 12 and nick_end > nick_start:
                    nickname = content[nick_start:nick_end]
                    table.add_row("Nickname", nickname)
            
            # Extract follower count if available
            if '"followerCount":' in content:
                fol_start = content.find('"followerCount":') + 16
                fol_end = content.find(',', fol_start)
                if fol_start > 16 and fol_end > fol_start:
                    followers = content[fol_start:fol_end]
                    table.add_row("Followers", followers)
            
            console.print(table)
            console.print(f"\n[yellow][!] Note: Full TikTok data requires API or browser automation[/yellow]")
            console.print(f"[cyan]Profile: https://www.tiktok.com/@{username}[/cyan]")
            
        elif response.status_code == 404:
            console.print(f"[yellow][!] Username @{username} not found[/yellow]")
        else:
            console.print(f"[yellow][!] Could not access profile (Status: {response.status_code})[/yellow]")
            
    except requests.exceptions.RequestException as e:
        console.print(f"[red][!] Error: {e}[/red]")
    except Exception as e:
        console.print(f"[red][!] Unexpected error: {e}[/red]")
    
    input("\n[Press Enter]")


def tiktok_advanced_search(username):
    """
    Advanced TikTok search using third-party APIs.
    Note: This is a placeholder for API-based search.
    
    Args:
        username: TikTok username
    """
    console.print("[yellow][!] Advanced TikTok search requires API access[/yellow]")
    console.print("[cyan]Options:[/cyan]")
    console.print("1. Use TikTok API (requires approval)")
    console.print("2. Use third-party services like RapidAPI")
    console.print("3. Use browser automation (Selenium/Playwright)")
    input("\n[Press Enter]")
