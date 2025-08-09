import typer
import nmap

app = typer.Typer(help="Port Scanner")

@app.command()
def scan(target: str, ports: str = "1-1024"):
    """Scan ports on a target"""
    nm = nmap.PortScanner()
    typer.echo(f"Scanning {target} on ports {ports}...")
    nm.scan(target, ports)
    for host in nm.all_hosts():
        typer.echo(f"Host: {host} ({nm[host].hostname()})")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                typer.echo(f"Port {port}/{proto}: {nm[host][proto][port]['state']}")
