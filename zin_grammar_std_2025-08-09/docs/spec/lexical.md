# Zin — Spécification lexicale (v0.1 draft)

## Espaces & commentaires
- Espaces et tabulations: ignorés sauf dans les chaînes.
- Nouvelle ligne: peut séparer des instructions (terminateur implicite) — pour simplifier les implémentations, **un `;` optionnel** est accepté en fin d’instruction.
- Commentaires: `//` jusqu'à la fin de ligne, ou `/* ... */` multilignes (non emboîtables).

## Littéraux
- `nombre/num` : décimaux (`0|[1-9][0-9]*`), flottants (`[0-9]+\.[0-9]+`), hex (`0x[0-9a-fA-F]+`).
- `texte/str` : `"..."` avec échappements `\" \\ \n \t \r`.
- `booléen/bool` : `vrai|true`, `faux|false`.

## Identifiants
- Regex: `[A-Za-z_][A-Za-z0-9_]*`
- Sensibles à la casse.

## Mots-clés (bilingues)
| FR          | EN      | Canon |
|-------------|---------|-------|
| si          | if      | IF    |
| sinon       | else    | ELSE  |
| fonction    | fn      | FN    |
| retourne    | return  | RETURN|
| pour        | for     | FOR   |
| de          | from    | FROM  |
| à / a       | to      | TO    |
| tantque     | while   | WHILE |
| affiche     | print   | PRINT |
| pause       | sleep   | SLEEP |
| importe(r)  | import  | IMPORT|
| module      | module  | MODULE|
| structure   | struct  | STRUCT|
| vrai        | true    | TRUE  |
| faux        | false   | FALSE |
| nombre      | num     | NUM_T |
| texte       | str     | STR_T |
| booléen/booleen | bool| BOOL_T |

> Notes:
> - `à` et `a` sont reconnus comme le même mot-clé quand ils signifient `to` dans `pour i de 0 à 10`.
> - `booléen` et `booleen` sont tous deux valides.
> - Les alias FR/EN sont strictement équivalents.
