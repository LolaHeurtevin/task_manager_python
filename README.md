# Gestionnaire de tâches

Ce projet consiste en la création d'un gestionnaire de tâches sous la forme d'une application desktop avec Python, PySide6 et QtDesigner

## Contraintes techniques
- Utilisation de Python et PySide6
- Archietcture MVC

## Commandes utiles
### Lancer le projet
python main.py

### Convertir le fichier QT Designer en Python
pyside6-uic ui_main_window.ui -o ui_main_window.py

### Ouvrir QtDesigner
pyside6-designer

## Mode d'emploi
Une fois le projet lancer, vous pouvez 
- Filtrer les tâches à l'aide du bouton filtrer, 
- Ajouter une nouvelle tâche en cliquant sur le bouton "Nouvelle tâche", puis remplir au minimum le titre et cliquer sur le bouton "Enregistrer
- Ajouter un commentaire à la tâche en cliquant sue le bouton "Ajouter un commentaire", puis écrire le commentaire dans l'emplacement apparu en dessous puis en cliquant sur le bouton "Enregistrer
- Modifier une tâche en cliquant sur n'importe quelle tâche de la liste de gauche, modifiant n'importe quel champ puis en cliquant sur le bouton "Enregistrer"
- Supprimer un commentaire en cliquant sur le bouton "Supprimer" d'un commentaire
- Supprimer une tâche en cliquant sur le bouton "Supprimer" en haut du formulaire de tâche
- Clôturer une tâche en cliquant sur le bouton "Clôturer" en haut du formulaire de tâche, puis en cliquant sur "Yes"

## Contraintes fonctionnelles
- Chaque tâche possède les attributs suivants : 
    - ID (int, obligatoire)
    - Titre (texte, obligatoire)
    - Description (texte, facultatif)
    - Date de début (date et heure, facultatif)
    - Date de fin (date et heure, facultatif)
    - État (enum [à faire, en cours, réalisé, abandonné, en attente], facultatif)
    - Commentaires (liste contenant le texte du commentaire et la date/heure de sa création)
- Possibilité de filtrer les tâches par état
- Possibilité de clôturer une tâche (l'interface doit demander une confirmation claire lors de la clôture)
- CRUD tâche
- CRUD commentaire

## Fonctionnalités implémentées
- Affichage du formulaire de création de tâche au clic sur le bouton "Nouvelle tâche"
- Enregistrement de la nouvelle tâche au clic sur le bouton "Enregistrer"
- Affichage de la liste de tâches sur la partie gauche de l'écran 
    - Au clic sur l'une des cartes, affichage de la tâche dans le formulaire de droite
- Mettre à jour une tâche
- Rechargement de la liste de tâches une fois qu'une tâche a été mise à jour afin d'avoir accès aux dernières informations
- Filtres les tâches par état
- Supprimer une tâche
- Clôturer une tâche : cliquer sur le bouton "Clôturer" fait s'afficher une modale de validation afin de confirmer la clôture de la tâche

## Fonctionnalités à implémenter
- Mise en place des commentaires (avec suppression)
- Ajout de messages de confirmation lors de la réalisation d'une action
- À la clôture d'une tâche, passer automatiquement la date et heure de fin à la date/heure actuelle
