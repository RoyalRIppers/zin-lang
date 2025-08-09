# Zin — Pro Parser Suite (draft)

Ce module fournit :
- **CLI `zinc`** : génération du parseur ANTLR (`zinc gen`), parse d’un fichier (`zinc parse`), AST JSON (`zinc ast`).
- **AST builder (skeleton)** : visiteur ANTLR → AST JSON minimal.
- **CI** : génération parseur, lint (ruff), tests (pytest).

## Utilisation rapide
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .

# Générer le parseur depuis docs/spec/grammar/Zin.g4
zinc gen

# Parser un fichier
zinc parse tests/grammar/hello.zin

# AST JSON (expérimental)
zinc ast tests/grammar/functions.zin
```
