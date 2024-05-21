# TP2: Divergences, merge et conflits

## Objectifs

+ Travailler en parallèle sur deux branches divergentes
+ Résoudre des conflits de merge

## Contexte

Les fonctions **first_verse** et **second_verse** de lyrics.py doivent chacune retourner les vers correspondants de Let It Be.

Vérifiez que les trois tests **sing**, **first_verse** et **second_verse** échouent avec `py -m unittest`.

Vous allez implémenter chaque fonction dans des branches parallèles.

## Création des branches de travail

C'est parti, votre équipe s'est réparti le travail entre les fonctions **first_verse** et **second_verse** créez les branches correspondantes.

```
git branch tp2-first
git branch tp2-second
```

## Modification sur tp2-main

Toujours sur la branche tp2-main, modifiez l'implémentation de **sing** pour retourner la concaténation de **first_verse** et **second_verse**.
<details>
<summary>Spoiler</summary>

```py
return first_verse() + second_verse()
```
</details>

Ajoutez vos changements et commitez.

<details>
<summary>Spoiler</summary>

```
git add lyric.py
git commit -m "Implemented sing"
```
</details>

## Implémentation de first_verse

Basculez maintenant sur la branche tp2-first. 
Implémentez **first_verse**.

Vérifiez que test_first_verse passe avec la commande 
```
py -m unittest -k first
```
Commitez.

Modifiez maintenant le message d'erreur de **second_verse** pour inciter votre collègue de la branche tp2-second à accélérer:
```py
raise Exception("Hurry up!")
```

Commitez

## Merge de la première branche de travail

Basculez sur tp2-main et mergez les changements de tp2-first.
<details>
<summary>Spoiler</summary>

```
git checkout tp2-main
git merge tp2-first
```
</details>

Visualisez l'historique avec
```
git log
```

**NB:** Contrairement au merge du TP précédent, un commit de merge a été ajouté à l'historique.

```
commit ................ (HEAD -> tp2-main)
Merge: ... ...
Author: ...
Date:   ...

    Merge branch 'tp2-first' into tp2-main
```

## Implémentation de second_verse

Basculez maintenant sur la branche tp2-second.
Implémentez **second_verse**. 

Vérifiez que test_second_verse passe avec la commande 
```
py -m unittest -k second
```
Commitez.

## Résolution des conflits et merge de la deuxième branche de travail

Basculez sur tp2-main puis tentez de merger tp2-second.
Un message d'erreur apparaît, pas de panique tout est sous contrôle ;)

```
CONFLICT (content): Merge conflict in lyrics.py
Automatic merge failed; fix conflicts and then commit the result.
```

Visualiser l'état courant avec `git status`

Pouvez vous expliquer le problème ?

<details>
<summary>Explications</summary>

```
Contrairement au merge précédent, des conflits entre main et second n'ont pas pu être résolus automatiquement par Git, car des lignes de lyrics.py ont été modifiées des deux côtés. Dans ces cas, il faut résoudre manuellement les conflits.
```
</details>

Git indique les zones en conflits directement dans les fichiers concernés.

Les modifications de la branche courante (ici tp2-main) sont indiquées en premier entre des lignes `<<<<<<< HEAD` et `=======`.

Les modifications de la branche mergée dans la branche courante (ici tp2-second) sont indiquées entre des lignes `=======` et `>>>>>>> tp2-second`

```py
<<<<<<< HEAD
raise Exception("Hurry up")
=========
return [...]
>>>>>>> tp2-second
```

Résolvez les conflits en modifiant directement le fichier concerné (ne pas oublier de supprimer les lignes générées par git). 

Vérifiez que tous les tests passent avec `py -m unittest`.

Une fois satisfait, ajoutez les fichiers puis commitez (pas besoin de spécifier de message, git en génère un automatiquement).

Prenez le temps de visualiser l'état courant à chaque étape avec `git status`.

C'est la fin du TP2, BRAVO !
