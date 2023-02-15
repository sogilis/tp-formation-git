# TP4: Cherry-pick

## Objectif
+ Intégrer des modifs précises d'une autre branche par cherry-pick

## Contexte

Comme au TP1, vous allez implémenter la fonction sing dans lyrics.py dans une branche de feature.
Vérifiez que les tests échouent en lançant `py -m unittest`.

## Créer une branche de feature

Créez la branche de feature tp4-feature.
<details>
<summary>Spoiler</summary>

```
git branch tp4-feature
```
</details>

## Ajouter des commits dans la branche de référence
Pendant que vous travaillez sur la feature, des collègues ajoutent des scripts de test utilitaire dans la branche main.

Créez un fichier test.sh contenant les lignes

```bash
#!/bin/bash

py -m unittest
```

*Si vous êtes sous linux, modifiez les droits d'exécution de ce fichier avec `chmod +x test.sh`. NB: Ces droits sont aussi versionnés par git !*

Commitez vos changements sur tp4-main.

<details>
<summary>Spoiler</summary>

```
git add test.sh
git commit -m "Add test.sh script"
```
</details>

Mais certains collègues sont sous Windows ! 

Créez un fichier test.bat contenant la ligne

```
py -m unittest
```

Commitez vos changements, toujours sur tp4-main.

<details>
<summary>Spoiler</summary>

```
git add test.bat
git commit -m "Add test.bat script"
```
</details>

Visualisez l'historique avec `git log`. 

## Implémenter sing dans la branche de feature

Placez vous sur la branche tp4-feature.

Implémentez la fonction sing et vérifiez que les tests passent avec la commande `py -m unittest`.

Commitez vos changements.

<details>
<summary>Spoiler</summary>

```
git add lyrics.py
git commit -m "Implemented sing"
```
</details>

Un peu longuette cette commande `py -m unittest` non ?

Récupérez le commit ajoutant le script de test de la branche tp4-main, en choisissant le commit correspondant à votre OS.

<details>
<summary>Spoiler</summary>

```
git cherry-pick <sha1-linux-or-windows>
```
</details>

Vérifiez que vous pouvez maintenant exécuter les tests avec 
```
# Linux
./test.sh

# Windows
test
```
## Merger la branche de feature

Placez vous sur la branche tp4-main et mergez la branche tp4-feature.

<details>
<summary>Spoiler</summary>

```
git checkout tp4-main
git merge tp4-feature
```
</details>

Visualisez le contenu du commit de merge avec `git show HEAD`
