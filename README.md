# TP6: Bisect

## Objectifs

+ Identifier une régression dans un historique Git
+ Manipuler la commande `git bisect`

## Contexte

L'exécution de la commande `py -m unittest` montre que les tests sont actuellement en échec.
Il est par conséquent légitime de se demander : quel commit a introduit la régression.

L'historique de la branche vous montre que 100 commits suspicieux ont précédemment été ajoutés.
Votre mission, si vous l'acceptez, est de déterminer le commit qui a mis les tests en défaut. 

## Lancement d'une bissection

Commencez par vérifier que les tests passent sur le commit "Suspicious commit #1"

<details>
<summary>Spoiler</summary>

```bash
git switch <sha1 du commit 1>
py -m unittest
```
</details>

Revenez sur le dernier commit puis demandez à Git de démarrer une bissection sur les 100 derniers commits et indiquez manuellement si le commit courant passe les tests ou non.

<details>
<summary>Spoiler</summary>

```bash
git switch tp6-main
git bisect start HEAD <sha1 du commit 1>

py -m unittest
git bisect [good|bad]

py -m unittest
git bisect [good|bad]
[...]
```
</details>

Une fois le commit problématique identifié, quittez le mode bissection.

<details>
<summary>Spoiler</summary>

```bash
git bisect reset
```
</details>

## Lancement d'une bissection automatique

Le saviez-vous ? Vous pouvez aussi automatiser le lancement des tests durant l'opération de bissection ! \o/

Pouvez-vous y arriver ?

<details>
<summary>Spoiler</summary>

```bash
git bisect start HEAD HEAD~99
git bisect run py -m unittest
git bisect reset
```
</details>

## Correction du commit problématique

Le commit problématique est le commit #[<?>](## "44").
Annulez les modifications de ce commit pour faire passer les tests de nouveau.

<details>
<summary>Spoiler</summary>

```bash
git revert HEAD~56
py -m unittest
```
</details>

Fin du TP6, BRAVO ! :D
