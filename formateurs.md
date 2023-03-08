# Tags de sauvegarde

Un tag est associé à un état "stable" pour chaque branche xxx-main. A tout moment d'un TP, si l'état de l'historique semble incohérent, il est possible de reset une branche sur ce tag avec les commandes

```
git checkout xxx-save
git branch -D xxx-main
git checkout -b xxx-main
```
