"""VK (VKontakte) OSINT module."""

import requests
from rich.table import Table
from manuleye.core import console


def vk_search(username_or_id):
    """
    Search for VK user information.
    
    Args:
        username_or_id: VK username (screen_name) or user ID
    """
    console.print(f"[cyan][*] Searching VK for: {username_or_id}...[/cyan]")
    
    table = Table(title=f"VK: {username_or_id}", border_style="orange3")
    table.add_column("Parameter", style="bold white")
    table.add_column("Value", style="green")
    
    try:
        # Method 1: Check profile via web (no API key needed)
        url = f"https://vk.com/{username_or_id}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            content = response.text
            
            # Check if profile exists
            if 'profile_deleted' in content or 'page_block_header' in content:
                console.print(f"[yellow][!] Profile deleted or does not exist[/yellow]")
                input("\n[Press Enter]")
                return
            
            table.add_row("Profile URL", url)
            table.add_row("Status", "✓ Profile exists")
            
            # Extract user ID from page
            if 'profile?id=' in response.url:
                user_id = response.url.split('id=')[1].split('&')[0]
                table.add_row("User ID", user_id)
            elif '/id' in response.url:
                user_id = response.url.split('/id')[1].split('?')[0]
                table.add_row("User ID", user_id)
            
            # Try to extract name from title
            if '<title>' in content:
                title_start = content.find('<title>') + 7
                title_end = content.find('</title>')
                title = content[title_start:title_end].strip()
                if title and '|' in title:
                    name = title.split('|')[0].strip()
                    table.add_row("Name", name)
            
            # Extract profile photo if available
            if 'profile_photo' in content or 'page_avatar' in content:
                table.add_row("Has Photo", "✓ Yes")
            
            console.print(table)
            console.print(f"\n[cyan]Profile: https://vk.com/{username_or_id}[/cyan]")
            
            # Suggest using VK API for more details
            console.print("\n[yellow][!] For detailed information, use VK API:[/yellow]")
            console.print("[cyan]1. Get API token from https://vk.com/dev[/cyan]")
            console.print("[cyan]2. Use users.get method[/cyan]")
            
        elif response.status_code == 404:
            console.print(f"[yellow][!] Profile not found[/yellow]")
        else:
            console.print(f"[yellow][!] Could not access profile (Status: {response.status_code})[/yellow]")
            
    except requests.exceptions.RequestException as e:
        console.print(f"[red][!] Error: {e}[/red]")
    except Exception as e:
        console.print(f"[red][!] Unexpected error: {e}[/red]")
    
    input("\n[Press Enter]")


def vk_api_search(user_id, access_token=None):
    """
    Search VK using official API (requires access token).
    
    Args:
        user_id: VK user ID
        access_token: VK API access token (optional)
    """
    if not access_token:
        console.print("[yellow][!] VK API search requires access token[/yellow]")
        console.print("[cyan]To get access token:[/cyan]")
        console.print("1. Go to https://vk.com/dev")
        console.print("2. Create standalone application")
        console.print("3. Get access token with required permissions")
        console.print("4. Use users.get, friends.get, photos.get methods")
        input("\n[Press Enter]")
        return
    
    try:
        # VK API request
        api_url = "https://api.vk.com/method/users.get"
        params = {
            'user_ids': user_id,
            'fields': 'photo_max,city,country,bdate,contacts,education,career',
            'access_token': access_token,
            'v': '5.131'
        }
        
        response = requests.get(api_url, params=params, timeout=10)
        data = response.json()
        
        if 'response' in data and data['response']:
            user = data['response'][0]
            
            table = Table(title=f"VK API: {user_id}", border_style="orange3")
            table.add_column("Parameter", style="bold white")
            table.add_column("Value", style="green")
            
            table.add_row("First Name", user.get('first_name', 'N/A'))
            table.add_row("Last Name", user.get('last_name', 'N/A'))
            table.add_row("User ID", str(user.get('id', 'N/A')))
            
            if 'bdate' in user:
                table.add_row("Birth Date", user['bdate'])
            
            if 'city' in user:
                table.add_row("City", user['city'].get('title', 'N/A'))
            
            if 'country' in user:
                table.add_row("Country", user['country'].get('title', 'N/A'))
            
            console.print(table)
        else:
            console.print(f"[red][!] API Error: {data.get('error', {}).get('error_msg', 'Unknown')}[/red]")
            
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")
