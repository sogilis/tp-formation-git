# TP5: Rebase

## Objectifs

+ Commitez des changements partiels
+ Travailler son historique local avec rebase interactif
+ Rebaser une branche sur une autre

## Contexte

Les fonctions **first_verse** et **second_verse** de lyrics.py doivent chacune retourner les vers correspondants de Let It Be.

Vérifiez que les tests **test_first_verse** et **test_second_verse** échouent avec `py -m unittest`.

La fonction first_verse sera implémentée dans une branche feature.

## Création de la branche de travail

Créez la branche tp5-feature

<details>
<summary>Spoiler</summary>

```
git branch tp5-feature
```
</details>

## Implémentation de second_verse sur tp5-main
Pendant que vous travaillez sur la branche feature, un collègue a déjà implémenté second_verse dans tp5-main.

Pour le simuler, toujours sur la branche tp5-main, implémentez second_verse.

Vérifiez que le test de second_verse passe avec 
```
py -m unittest -k second
```

Commitez vos changements.


## Implémentation de first_verse sur tp5-feature

Basculez maintenant sur la branche tp5-feature. 

### Ajout d'un fichier paroles

Pour être sûr de ne pas les oublier, commencez par créer un fichier **letitbe.txt** contenant les paroles de la chanson

<details>
<summary>Paroles</summary>

```
When I find myself in times of trouble, Mother Mary comes to me
Speaking words of wisdom, let it be
And in my hour of darkness she is standing right in front of me
Speaking words of wisdom, let it be
Let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
And when the broken hearted people living in the world agree
There will be an answer, let it be
For though they may be parted, there is still a chance that they will see
There will be an answer, let it be
Let it be, let it be, let it be, let it be
There will be an answer, let it be
Let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
Let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be, be
And when the night is cloudy there is still a light that shines on me
Shinin' until tomorrow, let it be
I wake up to the sound of music, Mother Mary comes to me
Speaking words of wisdom, let it be
And let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
And let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
```
</details>

Commitez ce fichier.

### Implémentation de first_verse

Implémentez **first_verse**.

Vérifiez que test_first_verse passe avec la commande 
```
py -m unittest -k first
```

### Commit partiel

Au lieu de commit toutes les modifications de lyrics.py, commitez d'abord seulement la première ligne modifiée.
Pour celà, lancez un add partiel avec `git add -p lyrics.py`
Une interface de ce type s'affiche dans le terminal:

```
+ line 1
+ line 2
+ ...

(1/1) Stage this hunk [y,n,q,a,d,s,e,?]? 
```
Les 'hunks' représentent des blocs de modifications groupées par git.

Entrez 'e' pour splitter manuellement le hunk courant. Une interface de ce type s'affiche:

```
# Manual hunk edit mode -- see bottom for a quick guide.
@@ -1,66 +1,112 @@
+ line 1
+ line 2
...
# ---
# To remove '-' lines, make them ' ' lines (context).
# To remove '+' lines, delete them.
# Lines starting with # will be removed.
# 
# If the patch applies cleanly, the edited hunk will immediately be
# marked for staging.
# If it does not apply cleanly, you will be given an opportunity to
# edit again.  If all lines of the hunk are removed, then the edit is
# aborted and the hunk is left unchanged.
```

Supprimez toutes les lignes sauf la première modifiée puis validez.

Visualisez l'état local avec git status. lyrics.py doit apparaître à la fois dans la staging area et les modifications locales.

Commitez le contenu de la staging area.
<details>
<summary>Spoiler</summary>

```
git commit -m "First line"
```
</details>
Commitez le reste des modifications à lyrics.py. 
<details>
<summary>Spoiler</summary>

```
git add lyrics.py
git commit -m "Rest of the lines"
```
</details>

Visualisez l'historique avec git log. Vous devriez voir trois commits après le commit 'TP5 Main', correspondant à l'ajout de letitbe.txt, la première ligne de votre implémentation de first_verse, puis le reste de l'implémentation.

### Réécriture de l'historique avec rebase interactif

Finalement, vous connaissez la chanson par coeur, et pas besoin d'intégrer votre memo letitbe.txt à la branch main.

Egalement, finalement, pas besoin de séparer votre implémentation en deux commits, qui peuvent être groupés en un seul.

Ces modifications de votre historique peuvent être effectuées en une commande avec un rebase interactif. Supprimez le commit de letitbe.txt et fusionnez les deux commits de l'implémentation de first_verse.

<details>
<summary>Spoiler</summary>

```
git rebase -i HEAD~3
```

Une interface de ce type s'affiche dans le terminal:

```
pick .... letitbe.txt
pick .... first line
pick .... rest of implem

# Rebase ...... onto ... (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
```

Remplacez pick par drop devant la ligne de letitbe.txt
Remplacez pick par reword devant la ligne de la première ligne de l'implémentation
Remplacez pick par fixup devant la ligne du reste de l'implémentation

Sauvez et quittez l'éditeur
</details>

## Rebase de la branche de travail sur tp5-main

Heureux de votre implémentation et de votre historique, vous pouvez maintenant rebaser votre branche de feature sur la branche tp5-main pour rester à jour des dernières modifications.

Listez les différences entre tp5-main et tp5-feature

<details>
<summary>Spoiler</summary>

```
git diff tp5-main tp5-feature
```
</details>

<details>
<summary>Spoiler</summary>

```
git rebase tp5-main
```
</details>

Vérifiez que le commit d'implémentation de second_verse fait désormais partie de l'historique de la branche tp5-feature.

Vérifiez que tous les tests passent avec py -m unittest.

## Merge de la branche feature dans master

Vous pouvez maintenant merger la branche tp5-feature dans tp5-main. Comme la branche feature est désormais basée sur la branche main, le merge est un simple fast-forward sans commit de merge.

<details>
<summary>Spoiler</summary>

```
git checkout tp5-main
git merge tp5-feature
```
</details>

Fin du TP5, BRAVO ! :D
