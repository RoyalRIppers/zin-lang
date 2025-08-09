# Zin — Grammaire + Std (starter v0.1)

Ce pack fournit :
- **Grammaire** EBNF + **ANTLR4** (`docs/spec/grammar/`)
- **Lexical** (`docs/spec/lexical.md`)
- **Types & Intrinsics**
- **Std** modules (`std/*`) — prototypes
- **Tests** `.zin` pour valider le parseur

## Intégration rapide dans ton repo
1. Copie les dossiers `docs/spec`, `std`, `tests/grammar`, `compiler/keywords.json` dans ton dépôt.
2. Si tu utilises ANTLR: `docs/spec/grammar/Zin.g4` est prêt.
3. Ajoute une CI qui liste et parse `tests/grammar/*.zin` (quand le parser sera prêt).

— Généré le 2025-08-09
