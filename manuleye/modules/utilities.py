"""Utility modules."""

import os
import hashlib
import random
import string
import json
from datetime import datetime
from rich.table import Table
from rich.prompt import Prompt
from manuleye.core import console, select_file


def hash_analyzer():
    """Calculate file hashes."""
    path = select_file()
    if not path:
        return
    
    try:
        console.print(f"[cyan][*] Calculating hashes for: {os.path.basename(path)}...[/cyan]")
        
        with open(path, 'rb') as f:
            data = f.read()
        
        table = Table(title=f"File Hashes: {os.path.basename(path)}", border_style="orange3")
        table.add_column("Algorithm", style="bold white")
        table.add_column("Hash", style="green")
        
        table.add_row("MD5", hashlib.md5(data).hexdigest())
        table.add_row("SHA1", hashlib.sha1(data).hexdigest())
        table.add_row("SHA256", hashlib.sha256(data).hexdigest())
        table.add_row("File Size", f"{len(data)} bytes")
        
        console.print(table)
        console.print("\n[cyan]Check hash on VirusTotal: https://www.virustotal.com/[/cyan]")
    except FileNotFoundError:
        console.print("[red][!] File not found![/red]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")


def calculate_password_strength(password):
    """Calculate password strength score."""
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    
    unique_chars = len(set(password))
    if unique_chars >= len(password) * 0.7:
        score += 1
    
    if score <= 3:
        return "Weak"
    elif score <= 5:
        return "Medium"
    elif score <= 7:
        return "Strong"
    else:
        return "Very Strong"


def password_generator():
    """Generate strong passwords."""
    console.print("[bold cyan]═══ PASSWORD GENERATOR ═══[/bold cyan]\n")
    
    length = int(Prompt.ask("Password length", default="16"))
    count = int(Prompt.ask("Number of passwords", default="5"))
    
    console.print("\n[yellow]Character types to include:[/yellow]")
    use_uppercase = Prompt.ask("Uppercase letters (A-Z)?", choices=["y", "n"], default="y") == "y"
    use_lowercase = Prompt.ask("Lowercase letters (a-z)?", choices=["y", "n"], default="y") == "y"
    use_digits = Prompt.ask("Digits (0-9)?", choices=["y", "n"], default="y") == "y"
    use_special = Prompt.ask("Special characters (!@#$%^&*)?", choices=["y", "n"], default="y") == "y"
    
    console.print("\n[yellow]Additional options:[/yellow]")
    exclude_ambiguous = Prompt.ask("Exclude ambiguous chars (0,O,l,1,I)?", choices=["y", "n"], default="n") == "y"
    readable = Prompt.ask("Make more readable (no consecutive special)?", choices=["y", "n"], default="n") == "y"
    
    # Build character set
    charset = ""
    if use_uppercase:
        charset += string.ascii_uppercase
    if use_lowercase:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_special:
        charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if exclude_ambiguous:
        ambiguous = "0Ol1I"
        charset = ''.join(c for c in charset if c not in ambiguous)
    
    if not charset:
        console.print("[red][!] No character types selected![/red]")
        input("\n[Press Enter]")
        return
    
    # Generate passwords
    passwords = []
    for _ in range(count):
        if readable:
            password = []
            special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            last_was_special = False
            
            for i in range(length):
                if last_was_special:
                    char = random.choice([c for c in charset if c not in special_chars])
                    last_was_special = False
                else:
                    char = random.choice(charset)
                    if char in special_chars:
                        last_was_special = True
                password.append(char)
            passwords.append(''.join(password))
        else:
            password = ''.join(random.choice(charset) for _ in range(length))
            passwords.append(password)
    
    # Display passwords
    table = Table(title="Generated Passwords", border_style="cyan")
    table.add_column("#", style="dim", width=4)
    table.add_column("Password", style="bold green")
    table.add_column("Strength", style="yellow")
    
    for i, pwd in enumerate(passwords, 1):
        strength = calculate_password_strength(pwd)
        table.add_row(str(i), pwd, strength)
    
    console.print("\n")
    console.print(table)
    
    # Save option
    save = Prompt.ask("\nSave to file?", choices=["y", "n"], default="n")
    if save == "y":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"passwords_{timestamp}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("═" * 60 + "\n")
                f.write("GENERATED PASSWORDS\n")
                f.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Length: {length} | Count: {count}\n")
                f.write("═" * 60 + "\n\n")
                for i, pwd in enumerate(passwords, 1):
                    strength = calculate_password_strength(pwd)
                    f.write(f"{i}. {pwd} [{strength}]\n")
                f.write("\n" + "═" * 60 + "\n")
                f.write("Generated by MANUL-EYE OSINT Framework\n")
                f.write("═" * 60 + "\n")
            console.print(f"[green][+] Passwords saved to: {filename}[/green]")
        except Exception as e:
            console.print(f"[red][!] Error saving: {e}[/red]")
    
    input("\n[Press Enter]")


def create_paste():
    """Create OSINT report."""
    console.print("[bold cyan]═══ PASTE CREATOR ═══[/bold cyan]\n")
    
    target_name = Prompt.ask("Target Name/Nickname")
    
    paste_data = {
        "target": target_name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "personal_info": {},
        "social_media": {},
        "contacts": {},
        "notes": []
    }
    
    console.print("\n[yellow]Fill in available information (press Enter to skip):[/yellow]\n")
    
    # Personal Information
    console.print("[bold orange3]Personal Information:[/bold orange3]")
    paste_data["personal_info"]["full_name"] = Prompt.ask("Full Name", default="")
    paste_data["personal_info"]["date_of_birth"] = Prompt.ask("Date of Birth", default="")
    paste_data["personal_info"]["age"] = Prompt.ask("Age", default="")
    
    # Social Media
    console.print("\n[bold orange3]Social Media:[/bold orange3]")
    paste_data["social_media"]["vk"] = Prompt.ask("VK", default="")
    paste_data["social_media"]["telegram"] = Prompt.ask("Telegram", default="")
    paste_data["social_media"]["instagram"] = Prompt.ask("Instagram", default="")
    paste_data["social_media"]["tiktok"] = Prompt.ask("TikTok", default="")
    paste_data["social_media"]["twitter"] = Prompt.ask("Twitter/X", default="")
    
    # Contacts
    console.print("\n[bold orange3]Contacts:[/bold orange3]")
    paste_data["contacts"]["phone"] = Prompt.ask("Phone", default="")
    paste_data["contacts"]["email"] = Prompt.ask("Email", default="")
    
    # Notes
    console.print("\n[bold orange3]Notes:[/bold orange3]")
    while True:
        note = Prompt.ask("Add note (or press Enter to finish)", default="")
        if not note:
            break
        paste_data["notes"].append(note)
    
    # Save paste
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"paste_{target_name.replace(' ', '_')}_{timestamp}.txt"
    json_filename = filename.replace('.txt', '.json')
    
    try:
        # Save as text
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("═" * 80 + "\n")
            f.write(f"PASTE: {target_name}\n")
            f.write(f"Created: {paste_data['timestamp']}\n")
            f.write("═" * 80 + "\n\n")
            
            if any(paste_data["personal_info"].values()):
                f.write("【 PERSONAL INFORMATION 】\n")
                f.write("-" * 80 + "\n")
                for key, value in paste_data["personal_info"].items():
                    if value:
                        f.write(f"{key.replace('_', ' ').title()}: {value}\n")
                f.write("\n")
            
            if any(paste_data["social_media"].values()):
                f.write("【 SOCIAL MEDIA 】\n")
                f.write("-" * 80 + "\n")
                for key, value in paste_data["social_media"].items():
                    if value:
                        f.write(f"{key.upper()}: {value}\n")
                f.write("\n")
            
            if any(paste_data["contacts"].values()):
                f.write("【 CONTACTS 】\n")
                f.write("-" * 80 + "\n")
                for key, value in paste_data["contacts"].items():
                    if value:
                        f.write(f"{key.title()}: {value}\n")
                f.write("\n")
            
            if paste_data["notes"]:
                f.write("【 NOTES 】\n")
                f.write("-" * 80 + "\n")
                for i, note in enumerate(paste_data["notes"], 1):
                    f.write(f"{i}. {note}\n")
                f.write("\n")
            
            f.write("═" * 80 + "\n")
            f.write("Generated by MANUL-EYE OSINT Framework\n")
            f.write("═" * 80 + "\n")
        
        # Save as JSON
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(paste_data, f, indent=4, ensure_ascii=False)
        
        console.print(f"\n[green][+] Paste created successfully![/green]")
        console.print(f"[cyan]Text version: {filename}[/cyan]")
        console.print(f"[cyan]JSON version: {json_filename}[/cyan]")
    except Exception as e:
        console.print(f"[red][!] Error creating paste: {e}[/red]")
    
    input("\n[Press Enter]")
