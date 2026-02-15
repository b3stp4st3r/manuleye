import os
import socket
import ssl
import subprocess
import requests
from rich.prompt import Prompt
from rich.table import Table
from manuleye.core import console


def port_scanner():
    target = Prompt.ask("Target IP/Domain")
    ports_input = Prompt.ask("Ports (e.g. 80,443 or 1-1000)", default="21,22,23,25,80,443,3306,3389,8080")
    console.print(f"[cyan][*] Scanning {target}...[/cyan]\n")
    
    try:
        if '-' in ports_input:
            start, end = map(int, ports_input.split('-'))
            ports = range(start, end + 1)
        else:
            ports = [int(p.strip()) for p in ports_input.split(',')]
        
        open_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                console.print(f"[green][+] Port {port} is OPEN[/green]")
            sock.close()
        
        if not open_ports:
            console.print("[yellow][!] No open ports found[/yellow]")
        else:
            console.print(f"\n[green][+] Found {len(open_ports)} open ports[/green]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")


def traceroute():
    target = Prompt.ask("Target IP/Domain")
    console.print(f"[cyan][*] Tracing route to {target}...[/cyan]\n")
    try:
        if os.name == 'nt':
            subprocess.run(f"tracert {target}", shell=True)
        else:
            subprocess.run(f"traceroute {target}", shell=True)
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")


def ping_sweep():
    network = Prompt.ask("Network (e.g. 192.168.1)", default="192.168.1")
    start = int(Prompt.ask("Start IP", default="1"))
    end = int(Prompt.ask("End IP", default="254"))
    console.print(f"[cyan][*] Scanning {network}.{start}-{end}...[/cyan]\n")
    
    alive_hosts = []
    for i in range(start, end + 1):
        ip = f"{network}.{i}"
        if os.name == 'nt':
            response = os.system(f"ping -n 1 -w 500 {ip} > nul 2>&1")
        else:
            response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        
        if response == 0:
            alive_hosts.append(ip)
            console.print(f"[green][+] {ip} is UP[/green]")
    
    console.print(f"\n[green][+] Found {len(alive_hosts)} alive hosts[/green]")
    input("\n[Press Enter]")


def ssl_cert_info():
    target = Prompt.ask("Domain (e.g. google.com)")
    port = int(Prompt.ask("Port", default="443"))
    console.print(f"[cyan][*] Fetching SSL certificate from {target}:{port}...[/cyan]\n")
    
    try:
        context = ssl.create_default_context()
        with socket.create_connection((target, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()
        
        table = Table(title=f"SSL Certificate: {target}", border_style="orange3")
        table.add_column("Field", style="bold white")
        table.add_column("Value", style="green")
        
        table.add_row("Subject", str(dict(x[0] for x in cert['subject'])))
        table.add_row("Issuer", str(dict(x[0] for x in cert['issuer'])))
        table.add_row("Version", str(cert['version']))
        table.add_row("Serial Number", str(cert['serialNumber']))
        table.add_row("Not Before", str(cert['notBefore']))
        table.add_row("Not After", str(cert['notAfter']))
        
        if 'subjectAltName' in cert:
            alt_names = ', '.join([x[1] for x in cert['subjectAltName']])
            table.add_row("Alt Names", alt_names)
        
        console.print(table)
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")


def http_headers():
    target = Prompt.ask("URL (e.g. https://example.com)")
    if not target.startswith('http'):
        target = 'https://' + target
    
    console.print(f"[cyan][*] Fetching headers from {target}...[/cyan]\n")
    
    try:
        response = requests.get(target, timeout=10, allow_redirects=True)
        
        table = Table(title=f"HTTP Headers: {target}", border_style="orange3")
        table.add_column("Header", style="bold white")
        table.add_column("Value", style="green")
        
        table.add_row("Status Code", str(response.status_code))
        
        for header, value in response.headers.items():
            table.add_row(header, str(value)[:100])
        
        console.print(table)
        
        security_headers = [
            'Strict-Transport-Security',
            'Content-Security-Policy',
            'X-Frame-Options',
            'X-Content-Type-Options'
        ]
        missing = [h for h in security_headers if h not in response.headers]
        
        if missing:
            console.print(f"\n[yellow][!] Missing security headers: {', '.join(missing)}[/yellow]")
        else:
            console.print("\n[green][+] All security headers present[/green]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")
    
    input("\n[Press Enter]")
