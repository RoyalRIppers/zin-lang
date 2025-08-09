# Module fs (std.fs) — v0.1 (restreint par zinsecure)

> **Sécurité** : I/O fichier est **privileged**. `zinsecure` doit autoriser explicitement ces appels.

- `fn read_text(str path) -> str`
- `fn write_text(str path, str data)`
- `fn exists(str path) -> bool`
