"""Telegram OSINT module."""

import requests
from rich.table import Table
from manuleye.core import console


def telegram_search(username):
    """
    Search for Telegram user/channel information.
    
    Args:
        username: Telegram username (without @)
    """
    console.print(f"[cyan][*] Searching Telegram for: @{username}...[/cyan]")
    
    # Remove @ if present
    username = username.lstrip('@')
    
    table = Table(title=f"Telegram: @{username}", border_style="orange3")
    table.add_column("Parameter", style="bold white")
    table.add_column("Value", style="green")
    
    try:
        # Method 1: Check if username exists via t.me redirect
        url = f"https://t.me/{username}"
        response = requests.get(url, timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            table.add_row("Profile URL", url)
            table.add_row("Status", "✓ Username exists")
            
            # Try to extract info from page
            content = response.text
            
            # Extract title (name)
            if '<title>' in content:
                title_start = content.find('<title>') + 7
                title_end = content.find('</title>')
                title = content[title_start:title_end].strip()
                if title and title != 'Telegram':
                    table.add_row("Name", title)
            
            # Extract description
            if 'tgme_page_description' in content:
                desc_start = content.find('tgme_page_description') + 30
                desc_end = content.find('</div>', desc_start)
                if desc_start > 30 and desc_end > desc_start:
                    desc = content[desc_start:desc_end].strip()
                    if desc and len(desc) < 200:
                        table.add_row("Description", desc[:100])
            
            # Check if it's a channel or user
            if 'tgme_page_photo' in content:
                table.add_row("Type", "User/Channel (has photo)")
            
            console.print(table)
            console.print(f"\n[cyan]Open in Telegram: tg://resolve?domain={username}[/cyan]")
            console.print(f"[cyan]Web version: https://t.me/{username}[/cyan]")
            
        else:
            console.print(f"[yellow][!] Username @{username} not found or private[/yellow]")
            
    except requests.exceptions.RequestException as e:
        console.print(f"[red][!] Error: {e}[/red]")
    except Exception as e:
        console.print(f"[red][!] Unexpected error: {e}[/red]")
    
    input("\n[Press Enter]")


def telegram_phone_search(phone):
    """
    Search Telegram by phone number (requires Telegram API).
    Note: This is a placeholder - real implementation requires Telegram API credentials.
    
    Args:
        phone: Phone number in international format
    """
    console.print(f"[yellow][!] Phone search requires Telegram API credentials[/yellow]")
    console.print("[cyan]To use this feature:[/cyan]")
    console.print("1. Get API credentials from https://my.telegram.org")
    console.print("2. Use libraries like 'telethon' or 'pyrogram'")
    console.print("3. Implement authentication flow")
    input("\n[Press Enter]")
