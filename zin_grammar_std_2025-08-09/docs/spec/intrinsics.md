# Intrinsics du langage (v0.1)

Ces opérations sont **mots-clés** (pas des fonctions de bibliothèque) et peuvent être mappées sur des appels natifs par le backend.

- `affiche` / `print <expr>` : écrit sur la sortie standard avec saut de ligne implicite.
- `pause` / `sleep <nombre>` : dort `<nombre>` millisecondes (draft; précision à définir).
- `retourne` / `return [expr]` : renvoie depuis la fonction courante.
- Contrôle: `si/sinon`, `pour de ... à ...`, `tantque`.

> I/O fichiers, réseau brut, etc. ne sont **pas** intrinsèques et passent par la std + `zinsecure`.
