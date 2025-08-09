# Feuille de route (préliminaire)

## Phase 0 — Démarrage communautaire
- [ ] Publier ZEP-0001 : objectifs, principes, terminologie
- [ ] Choisir la **stratégie d’implémentation** (compiler natif, VM, transpileur)
- [ ] Définir le **format binaire** ciblé (PE/ELF/Mach-O) et/ou une VM intermédiaire
- [ ] Ébauche de **syntaxe** et **types**

## Phase 1 — Prototype (MVP)
- [ ] Parser + AST
- [ ] Type checker simplifié
- [ ] Backend minimal (ex : LLVM / Cranelift / codegen x64)
- [ ] CLI `zinc` rudimentaire (compile `hello.zin` -> exécutable)

## Phase 2 — Sécurité et outils
- [ ] `zinsecure` : analyse statique pré-compilation (liste noire, sandboxing)
- [ ] `zinmind` : assistant (règles, auto-complétion, prompts)
- [ ] `ZinWatch` : hooks anti-triche (lib réseau, signature, heuristiques)

## Phase 3 — Écosystème
- [ ] Stdlib minimale (IO, string, containers)
- [ ] Paquetage (`zinpkg`)
- [ ] Éditeur/extension VS Code
