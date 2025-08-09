import typer
import importlib
import os

app = typer.Typer(help="Security & Privacy CLI Multitool")

TOOLS_DIR = "tools"

# Dynamically load commands from tools folder
for filename in os.listdir(TOOLS_DIR):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"{TOOLS_DIR}.{filename[:-3]}"
        module = importlib.import_module(module_name)
        if hasattr(module, "app"):
            app.add_typer(module.app, name=filename[:-3])

if __name__ == "__main__":
    app()
