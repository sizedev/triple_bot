from importlib import import_module
from pkgutil import iter_modules
from pathlib import Path
from interactions import Client


# Added a util to load all extensions in a particular directory
def load_extensions(client: Client, pkg: str):
    pkg_module = import_module(pkg)
    for ext_module in iter_modules(pkg_module.__path__):
        extname = f"{pkg_module.__name__}.{ext_module.name}"
        client.load(extname)
        print(f"Loaded {extname} Extension")