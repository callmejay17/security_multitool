import typer
import hashlib

app = typer.Typer(help="File Hashing Tool")

@app.command()
def file(file_path: str, algo: str = "sha256"):
    """Generate hash for a file"""
    try:
        h = hashlib.new(algo)
    except ValueError:
        typer.echo("Invalid algorithm. Try: md5, sha1, sha256, sha512")
        raise typer.Exit()
    
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    typer.echo(f"{algo.upper()} hash: {h.hexdigest()}")
