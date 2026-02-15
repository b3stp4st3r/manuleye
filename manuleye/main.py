#!/usr/bin/env python3

import sys
from rich.prompt import Prompt
from rich.table import Table

from manuleye.core import console, clear_screen, get_banner

from manuleye.modules.lookup import (
    username_hunt, email_lookup, phone_intel, ip_geolocate, domain_lookup
)
from manuleye.modules.metadata import (
    exif_extractor, pdf_metadata, video_metadata, audio_metadata,
    office_metadata, archive_info, metadata_cleaner
)
from manuleye.modules.network import (
    port_scanner, traceroute, ping_sweep, ssl_cert_info, http_headers
)
from manuleye.modules.security import sqlmap_scan, xss_scan, instagram_osint
from manuleye.modules.utilities import create_paste, password_generator, hash_analyzer

from manuleye.social import telegram_search, tiktok_search, vk_search

from manuleye.version_check import show_version_info


def show_main_menu():
    menu_table = Table(show_header=False, box=None, padding=(0, 2))
    menu_table.add_column(style="white", width=25)
    menu_table.add_column(style="white", width=25)
    menu_table.add_column(style="white", width=25)
    
    menu_table.add_row(
        "[bold orange3][LOOKUP][/bold orange3]",
        "[bold red][SECURITY][/bold red]",
        "[bold yellow][METADATA][/bold yellow]"
    )
    menu_table.add_row(
        "[1] Username Hunt",
        "[6] SQLMap",
        "[11] EXIF Extract"
    )
    menu_table.add_row(
        "[2] Email Lookup",
        "[7] XSStrike",
        "[12] PDF Metadata"
    )
    menu_table.add_row(
        "[3] Phone Intel",
        "[8] Instagram OSINT",
        "[13] Video Metadata"
    )
    menu_table.add_row(
        "[4] IP Geolocate",
        "",
        "[14] Audio Metadata"
    )
    menu_table.add_row(
        "[5] Domain Resolve",
        "",
        "[15] Office Metadata"
    )
    menu_table.add_row(
        "",
        "",
        "[16] Archive Info"
    )
    menu_table.add_row(
        "[bold cyan][NETWORK][/bold cyan]",
        "[bold green][SOCIAL][/bold green]",
        "[bold magenta][UTILITIES][/bold magenta]"
    )
    menu_table.add_row(
        "[17] Port Scanner",
        "[23] Telegram Search",
        "[20] Create Paste"
    )
    menu_table.add_row(
        "[18] Traceroute",
        "[24] TikTok Search",
        "[21] Password Gen"
    )
    menu_table.add_row(
        "[19] Ping Sweep",
        "[25] VK Search",
        "[22] Hash Analyzer"
    )
    menu_table.add_row(
        "[26] SSL Cert Info",
        "",
        "[10] Meta Cleaner"
    )
    menu_table.add_row(
        "[27] HTTP Headers",
        "",
        ""
    )
    
    console.print(menu_table)
    console.print("\n[bold cyan][9] Version Info & Update Check[/bold cyan]")
    console.print("[bold red][0] Exit[/bold red]")


def main():
    try:
        while True:
            clear_screen()
            get_banner()
            show_main_menu()
            
            choice = Prompt.ask("\n[bold orange3]Select option[/bold orange3]")
            
            if choice == "1":
                username_hunt()
            elif choice == "2":
                email_lookup()
            elif choice == "3":
                phone_intel()
            elif choice == "4":
                ip_geolocate()
            elif choice == "5":
                domain_lookup()
            
            elif choice == "6":
                sqlmap_scan()
            elif choice == "7":
                xss_scan()
            elif choice == "8":
                instagram_osint()
            
            elif choice == "10":
                metadata_cleaner()
            elif choice == "11":
                exif_extractor()
            elif choice == "12":
                pdf_metadata()
            elif choice == "13":
                video_metadata()
            elif choice == "14":
                audio_metadata()
            elif choice == "15":
                office_metadata()
            elif choice == "16":
                archive_info()
            
            elif choice == "17":
                port_scanner()
            elif choice == "18":
                traceroute()
            elif choice == "19":
                ping_sweep()
            elif choice == "26":
                ssl_cert_info()
            elif choice == "27":
                http_headers()
            
            elif choice == "20":
                create_paste()
            elif choice == "21":
                password_generator()
            elif choice == "22":
                hash_analyzer()
            
            elif choice == "23":
                username = Prompt.ask("Telegram username")
                telegram_search(username)
            elif choice == "24":
                username = Prompt.ask("TikTok username")
                tiktok_search(username)
            elif choice == "25":
                username = Prompt.ask("VK username or ID")
                vk_search(username)
            
            elif choice == "9":
                show_version_info()
            
            elif choice == "0":
                console.print("[bold cyan]Stay sharp. Stay hidden.[/bold cyan]")
                break
            else:
                console.print("[red][!] Invalid option[/red]")
                import time
                time.sleep(1)
                
    except KeyboardInterrupt:
        console.print("\n[yellow][!] Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red][!] Unexpected error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
