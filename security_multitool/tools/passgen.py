import typer
import secrets
import string

app = typer.Typer(help="Password Generator")

@app.command()
def generate(length: int = 16, symbols: bool = True):
    """Generate a secure password"""
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    typer.echo(password)
