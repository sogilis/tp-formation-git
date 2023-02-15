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

## Annuler un commit local

Annulez le commit de revert en conservant les changements associés.

<details>
<summary>Spoiler</summary>

```
git reset HEAD~1
```
</details>

Visualiser l'historique, le commit de revert doit avoir disparu.

Visualiser l'état local, les changements du commit annulés doivent apparaître dans les modifications locales.

## Amender un commit local

Visualiser l'historique. Le dernier commit doit avoir le message "Add instructions".

Intégrez directement les changements locaux dans ce dernier commit.

<details>
<summary>Spoiler</summary>

```
git add .
git commit --amend -m "Correct instructions"
```
</details>

Visualiser le dernier commit avec `git show HEAD`. Le message et les modifications de ce commit doivent avoir été mis à jour avec nos changements.

## Bonus : Répéter l'opération pour effacer le commit problématique

Bien qu'amusant, le commit "Delete instructions" n'a finalement pas grand intérêt. En répétant un cycle de reset/amend, remplacez ce commit par le contenu intéressant de "Add more instructions".

<details>
<summary>Spoiler</summary>

```
git reset HEAD~
git add .
git commit --amend -m "Correct instructions"
```
</details>


*Ces opérations peuvent être effectuées de manières plus synthétiques avec d'autres commandes, notamment la commande rebase, que nous verrons dans les TP suivants.*
