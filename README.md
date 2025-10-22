# Gestionnaire de tâches

Ce projet consiste en la création d'un gestionnaire de tâches sous la forme d'une application desktop avec Python et PySide6

## Contraintes techniques
- Utilisation de Python et PySide6
- Archietcture MVC

## Contraintes fonctionnelles
- Chaque tâche possède les attributs suivants : 
    - ID (int, obligatoire)
    - Titre (texte, obligatoire)
    - Description (texte, facultatif)
    - Date de début (date et heure, facultatif)
    - Date de fin (date et heure, facultatif)
    - État (enum [à faire, en cours, réalisé, abandonné, en attente], facultatif)
    - Commentaires (liste contenant le texte du connentaire et la date/heure de sa création)
- Possibilité de filtrer les tâches par état
- Possibilité de clôturer une tâche (l'interface doit demander une confirmation claire lors de la clôture)
- CRUD tâche
- CRUD commentaire

## Commandes utiles
### Lancer le projet
python main.py

### Convertir le fichier QT Designer en Python
pyside6-uic ui_main_window.ui -o ui_main_window.py

### Ouvrir QtDesigner
pyside6-designer

## Ce qui a été fait
- Affichage du formulaire de création de tâche au clic sur le bouton "Nouvelle tâche"
- Enregistrement de la nouvelle tâche au clic sur le bouton "Enregistrer"
- Affichage de la liste de tâches sur la partie gauche de l'écran 
    - Au clic sur l'une des cartes, affichage de la tâche dans le formulaire de droite

## Ce qu'il reste à faire
- Gérer les identifiants car ils sont générés en fonction du nombre de tâches dans la liste date, sauf que si on a 5 tâches et qu'on supprime la tâche 3, la prochaine tâche crée aura l'id 5 et l'id 5 sera en double
- Filtres les tâches
- Mise en place des commentaires (avec suppression)
- Clôturer une tâche
- Supprimer une tâche
- Mettre à jour une tâche
