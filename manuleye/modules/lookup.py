"""Lookup and intelligence gathering modules."""

import subprocess
import requests
import socket
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from rich.table import Table
from rich.prompt import Prompt
from manuleye.core import console, validate_ip, API_ENDPOINTS


def username_hunt():
    """Search for username across 500+ platforms using Maigret."""
    target = Prompt.ask("Username")
    console.print(f"[cyan][*] Searching for: {target}...[/cyan]")
    try:
        subprocess.run(f"maigret {target} -a", shell=True, timeout=300)
    except subprocess.TimeoutExpired:
        console.print("[red][!] Timeout (5 min limit)[/red]")
    except FileNotFoundError:
        console.print("[red][!] Maigret not found. Install: pip install maigret[/red]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    input("\n[Press Enter]")


def email_lookup():
    """Check email presence on various services using Holehe."""
    target = Prompt.ask("Email")
    console.print(f"[cyan][*] Checking: {target}...[/cyan]")
    try:
        subprocess.run(f"holehe {target} --only-used", shell=True, timeout=60)
    except subprocess.TimeoutExpired:
        console.print("[red][!] Timeout[/red]")
    except FileNotFoundError:
        console.print("[red][!] Holehe not found. Install: pip install holehe[/red]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    input("\n[Press Enter]")


def phone_intel():
    """Analyze phone number and extract carrier, location, timezone info."""
    number = Prompt.ask("Phone (e.g. +79991234567)")
    console.print(f"[*] Analyzing phone number: {number}...", style="cyan")
    
    try:
        parsed_num = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(parsed_num):
            console.print("[red][!] Invalid phone number format![/red]")
            input("\n[Press Enter]")
            return
        
        table = Table(title=f"Phone Intelligence: {number}", border_style="orange3")
        table.add_column("Parameter", style="bold white")
        table.add_column("Value", style="green")
        
        region = geocoder.description_for_number(parsed_num, "en")
        operator = carrier.name_for_number(parsed_num, "en")
        zones = timezone.time_zones_for_number(parsed_num)
        
        table.add_row("Country/Region", region if region else "Unknown")
        table.add_row("Carrier/Provider", operator if operator else "Unknown")
        table.add_row("Time Zones", str(zones))
        table.add_row("International Format", 
                     phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
        table.add_row("Local Format", 
                     phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.NATIONAL))
        table.add_row("E.164 Format", 
                     phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.E164))
        
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error parsing number: {e}[/red]")
    
    input("\n[Press Enter]")


def ip_geolocate():
    """Get detailed information about IP address."""
    ip = Prompt.ask("IP Address")
    
    if not validate_ip(ip):
        console.print("[red][!] Invalid IP address format![/red]")
        input("\n[Press Enter]")
        return
    
    try:
        console.print(f"[cyan][*] Querying IP: {ip}...[/cyan]")
        response = requests.get(f"{API_ENDPOINTS['ip_lookup']}{ip}", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "success":
            table = Table(title=f"IP Intel: {ip}", border_style="orange3")
            table.add_column("Parameter", style="bold white")
            table.add_column("Value", style="green")
            
            key_order = ["country", "regionName", "city", "zip", "lat", "lon", 
                        "timezone", "isp", "org", "as"]
            for key in key_order:
                if key in data:
                    table.add_row(key.upper(), str(data[key]))
            
            console.print(table)
            
            if "lat" in data and "lon" in data:
                maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
                console.print(f"\n[cyan]Google Maps: {maps_url}[/cyan]")
        else:
            console.print(f"[red][!] IP lookup failed: {data.get('message', 'Unknown error')}[/red]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")


def domain_lookup():
    """Resolve domain to IP and gather information."""
    domain = Prompt.ask("Domain (e.g. example.com)")
    console.print(f"[cyan][*] Analyzing domain: {domain}...[/cyan]")
    
    try:
        ip = socket.gethostbyname(domain)
        console.print(f"[green][+] Resolved IP: {ip}[/green]\n")
        
        # Reuse IP geolocation
        response = requests.get(f"{API_ENDPOINTS['ip_lookup']}{ip}", timeout=10)
        data = response.json()
        
        if data.get("status") == "success":
            table = Table(title=f"Domain: {domain}", border_style="orange3")
            table.add_column("Parameter", style="bold white")
            table.add_column("Value", style="green")
            
            table.add_row("Domain", domain)
            table.add_row("IP Address", ip)
            table.add_row("Country", data.get("country", "N/A"))
            table.add_row("Region", data.get("regionName", "N/A"))
            table.add_row("City", data.get("city", "N/A"))
            table.add_row("ISP", data.get("isp", "N/A"))
            table.add_row("Organization", data.get("org", "N/A"))
            
            console.print(table)
    except socket.gaierror:
        console.print("[red][!] Domain not found or DNS error.[/red]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")
