import json
import os
from PySide6.QtWidgets import QMessageBox
from utils.utils import display_operation_outcome

from constants import DATA_TASKS_PATH

def close_task(self):
    id_task = int(self.ui.label_5.text())
    if not id_task:
        print("Aucun ID trouvé")
        return

    reply = QMessageBox.question(
        self,
        "Confirmation",
        "Voulez-vous vraiment clôturer cette tâche ?",
        QMessageBox.Yes | QMessageBox.No
    )

    if reply == QMessageBox.Yes:
        data = get_all_tasks()

        for task in data:
            if (task.get("id", 0)) == id_task:
                task["state"] = "réalisé"
        
        os.makedirs(os.path.dirname(DATA_TASKS_PATH), exist_ok=True)
        with open(DATA_TASKS_PATH, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("Tâche clôturée")
        display_operation_outcome(self, "Tâche clôturée")
        self.set_tasks_view()
        self.set_new_task_view()
    else:
        print("Annulé")


def delete_task(self):
    id_task = int(self.ui.label_5.text())
    if not id_task:
        print("Aucun ID trouvé")
        return

    data = get_all_tasks()

    new_data = [task for task in data if int(task.get("id", 0)) != id_task]

    if len(new_data) == len(data):
        print(f"Aucune tâche trouvée avec l'ID : {id_task}")
        return

    os.makedirs(os.path.dirname(DATA_TASKS_PATH), exist_ok=True)
    with open(DATA_TASKS_PATH, "w", encoding='utf-8') as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)

    print(f"Tâche supprimée : {id_task}")

    self.set_tasks_view()
    self.set_new_task_view()
    display_operation_outcome(self, "Tâche supprimée")

def get_filtered_tasks(self):
    state = self.ui.comboBox_2.currentText().strip()
    all_tasks = get_all_tasks()

    print(f"Filtrage des tâches par statut : {state}")

    if (state == "Tous les statuts"):
        return all_tasks    

    filtered_tasks = [task for task in all_tasks if task.get("state", "") == state]

    if not filtered_tasks:
        print(f"Aucune tâche trouvée avec le statut : {state}")
        return []
    else :
        return filtered_tasks

def filter_tasks_by_state(self):
    self.set_tasks_view(filtered = True)

# Récupérer toutes les tâches
def get_all_tasks():
    try:
        with open(DATA_TASKS_PATH, "r", encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # doit renvoyer une liste ([]) si fichier inexistant

# Enregistrer une nouvelle tâche ou mettre à jour une tâche existante
def save_task(self):
    from controllers.comment_controller import save_comment

    title = self.ui.lineEdit.text().strip()
    description = self.ui.plainTextEdit.toPlainText().strip()
    date_beginning = self.ui.dateTimeEdit.text()
    date_ending = self.ui.dateTimeEdit_2.text()
    state = self.ui.comboBox.currentText().strip()

    if not title:
        print("Titre vide — rien à enregistrer.")
        return

    data = get_all_tasks() 

    id_text = self.ui.label_5.text().strip()
    if id_text:
        task_id = int(id_text)
    else:
        max_id = max((int(t.get("id", 0)) for t in data), default=0)
        task_id = int(max_id) + 1

    print(f"Utilisation de l'ID de tâche : {task_id}")

    # Construire la nouvelle / mise à jour de tâche
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "date_beginning": date_beginning,
        "date_ending": date_ending,
        "state": state
    }

    found = False
    for i, existing in enumerate(data):
        if int(existing.get("id")) == task_id:
            data[i] = new_task 
            found = True
            display_text = "mise à jour"
            break

    if not found:
        data.append(new_task)
        display_text = "créée"

    # Sauvegarde de la nouvelle liste
    os.makedirs(os.path.dirname(DATA_TASKS_PATH), exist_ok=True)
    with open(DATA_TASKS_PATH, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Tâche {display_text} : {new_task}")
    display_operation_outcome(self, "Tâche enregistrée")
    save_comment(self, task_id)
    self.set_tasks_view()