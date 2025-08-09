import typer
import os
import secrets

app = typer.Typer(help="Securely Delete Files")

@app.command()
def file(file_path: str, passes: int = 3):
    """Overwrite and delete a file securely"""
    if not os.path.isfile(file_path):
        typer.echo("File not found.")
        raise typer.Exit()

    length = os.path.getsize(file_path)
    for _ in range(passes):
        with open(file_path, "wb") as f:
            f.write(secrets.token_bytes(length))
    os.remove(file_path)
    typer.echo(f"File {file_path} securely deleted.")
