#! /usr/bin/python3.9

import os

commit_count_start = 1
commit_count_end = 3

for i in range(commit_count_start, commit_count_end):
    commit_message = f"Suspicious commit #{i}"
    
    # ajouter un fichier avec un nom aléatoire et un contenu aléatoire
    filename = 'commit_number'
    with open(filename, 'w') as f:
        f.write(str(i))
    
    # ajouter les modifications au suivi de version
    os.system('git add ' + filename)
    # faire un commit avec le message aléatoire
    os.system('git commit -m "' + commit_message + '"')
