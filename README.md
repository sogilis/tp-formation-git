# TP3 : Corriger une erreur

## Créer un commit de revert

Oups, les instructions de ce TP ont été écrasées par un collègue malicieux.

Visualisez l'historique et repérez le commit "Delete instructions".

Générez un commit annulant ces modifications.

<details>
<summary>Spoiler</summary>

```
# Either
git revert <sha1>
# Or
git revert HEAD~1
```
</details>

Visualisez à nouveau l'historique.
