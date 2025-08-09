import typer
import requests

app = typer.Typer(help="Check if VPN is active")

@app.command()
def check():
    """Check if you're using a VPN"""
    try:
        ip_data = requests.get("https://ipinfo.io/json").json()
        typer.echo(f"IP: {ip_data.get('ip')}")
        typer.echo(f"ISP: {ip_data.get('org')}")
        typer.echo(f"Location: {ip_data.get('city')}, {ip_data.get('country')}")

        if "VPN" in ip_data.get("org", "").upper() or "HOSTING" in ip_data.get("org", "").upper():
            typer.secho("Possible VPN detected!", fg=typer.colors.GREEN)
        else:
            typer.secho("Likely no VPN in use.", fg=typer.colors.RED)
    except Exception as e:
        typer.echo(f"Error: {e}")
