import os
from pathlib import Path

for pyfile in Path('app').rglob("*.py"):
    os.system(f"pycodestyle {pyfile}")
