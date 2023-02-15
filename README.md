# TP1 : Premiers pas avec Git

## Objectifs du TP :

- configurer git
- créer une branche de travail
- manipuler la staging area
- faire des commits
- consulter l'historique
- merger sa branche de travail dans la branche principale

## Préambule: configurer Git

Configurez git et indiquez votre nom et e-mail pour vous identifier comme auteur des futurs commits. Utilisez la commande `git config` ou modifier manuellement les fichiers `~/.gitconfig` ou `.git/config`.

```
git config --global user.name  "Firstname Lastname"
git config --global user.email "firstname@lastname.name"
```

## Contexte

La fonction **sing()** de **lyrics.py** est censée retourner le premier vers d'une chanson bien connue (Let It Be)

Entrez la commande 
```
py -m unittest
``` 
pour constater l'échec des tests.

Dans la suite du TP, vous devrez modifier l'implémentation de **sing()** pour faire passer les tests avec l'aide de Git.

## Créer une branche de travail

Pour chaque TP, nous allons créer une ou des branches de travail spécifiques en partant d'une branche de référence, (ici `tp1-main`).

Créez la branche de travail `tp1-feature` et se positionner dessus:

<details>
<summary>Spoiler</summary>

```
git checkout -b tp1-feature
```
</details>

*Vous pouvez lister les branches existantes avec `git branch`. La branche courante est préfixée par le symbole '*'*

## Faire passer les tests

Modifiez le fichier **lyrics.py** pour faire passer les tests
Vérifiez que tout est au vert avec la commande

```
py -m unittest
```

## Visualiser les modifications avec Git

Visualisez l'état git local avec 
```
git status
```

Le fichier lyrics.py devrait apparaître dans les fichier modifiés

```
Changes not staged for commit:
    modified:   lyrics.py
```

Affichez les changements de lyrics.py

<details>
<summary>Spoiler</summary>

```bash
git diff lyrics.py
```
</details>

## Ajouter les changements à l'historique

Ajoutez les changements dans la staging area et comparez le nouvel état git local

<details>
<summary>Spoiler</summary>

```
git add lyrics.py
git status
```
</details>

Le fichier lyrics.py devrait apparaître dans la staging area

```
Changes to be committed:
    modified:   README.md
```

*Pour annuler cette opération vous pouvez utiliser la commande*
```
git restore --staged lyrics.py
```

Une fois satisfait de vos changements, ajoutez les à l'historique de la branche en créant un commit

<details>
<summary>Spoiler</summary>

```
git commit -m "Un message de votre choix"
```

*En omettant le -m "...", git ouvre un éditeur de texte (souvent vim) pour éditer le message. Editez, sauvegardez puis quittez l'éditeur pour valider le commit*

*Pour effectuer les étapes add + commit en une seule commande, vous pouvez utiliser la commande*
```
git commit -a lyrics.py -m "Message"
```
</details>

Visualisez l'historique avec

```
git log
```

Votre commit et les infos associées devraient apparaître en première position

Visualisez spécifiquement les infos de votre commit avec

```
# Remplacer SHA1 par la révision de votre commit
git show <SHA1>
```

<details>
<summary>Rappel sur les identifiants relatifs de révision</summary>

- `HEAD`: le dernier commit, et le commit parent du prochain commit
- `HEAD^`: le parent de HEAD
- `HEAD^2`: le deuxième parent de HEAD (commit de merge avec plusieurs parents)
- `HEAD~1`: l'ancêtre au premier degré de HEAD, le parent (identique à `HEAD^`)
- `HEAD~2`: le grand-parent
- `HEAD~3`: l'arrière-grand-parent
- et ainsi de suite
</details>

## Intégrer les modifications à la branche de référence

Replacez vous sur la branche `tp1-main`, puis mergez la branche `tp1-feature` dans `tp1-main`

<details>
<summary>Spoiler</summary>

```
git checkout tp1-main
git merge tp1-feature
```
</details>

Visualisez le log pour constater que votre commit a bien été intégré à la branche tp1-main.

Vérifiez que les tests passent désormais sur la branche tp1-main.

Supprimez la branche tp1-feature
<details>
<summary>Spoiler</summary>

```
git branch -d tp1-feature
```
</details>

Fin du TP1, BRAVO ! :D
