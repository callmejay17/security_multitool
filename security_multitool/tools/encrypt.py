import typer
from cryptography.fernet import Fernet

app = typer.Typer(help="Encrypt & Decrypt Files")

@app.command()
def genkey():
    """Generate and save a new key"""
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
    typer.echo("Key saved to key.key")

@app.command()
def file_encrypt(file_path: str, key_path: str = "key.key"):
    """Encrypt a file"""
    key = open(key_path, "rb").read()
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted)
    typer.echo(f"Encrypted file saved as {file_path}.enc")

@app.command()
def file_decrypt(file_path: str, key_path: str = "key.key"):
    """Decrypt a file"""
    key = open(key_path, "rb").read()
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    out_path = file_path.replace(".enc", ".dec")
    with open(out_path, "wb") as f:
        f.write(decrypted)
    typer.echo(f"Decrypted file saved as {out_path}")
