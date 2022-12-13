from pathlib import Path
from interactions import Client


# Added a util to load all extensions in a particular directory
def load_extensions(client: Client, pkg: str):
    path = Path(pkg.replace(".", "/"))
    for extpath in path.glob("*.py"):
        extname = f"{pkg}.{extpath.stem}"
        client.load(extname)
        print(f"Loaded {extname} Extension")