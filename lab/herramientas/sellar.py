"""Uso: python sellar.py archivo  -> imprime el SHA-256 del archivo."""
import hashlib, sys
h = hashlib.sha256()
with open(sys.argv[1], "rb") as f:
    for bloque in iter(lambda: f.read(8192), b""):
        h.update(bloque)
print(h.hexdigest())
