import json
import os

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
    self.setTasksView(filtered = True)

# Récupérer toutes les tâches
def get_all_tasks():
    data_path = "data/data.json"
    try:
        with open(data_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Enregistrer une nouvelle tâche ou mettre à jour une tâche existante
def save_task(self):
    title = self.ui.lineEdit.text().strip()
    description = self.ui.plainTextEdit.toPlainText().strip()
    date_begining = self.ui.dateTimeEdit.text()
    date_ending = self.ui.dateTimeEdit_2.text()
    state = self.ui.comboBox.currentText().strip()

    if not title:
        print("Titre vide — rien à enregistrer.")
        return

    data_path = "data/data.json"
    data = get_all_tasks()  # doit renvoyer une liste ([]) si fichier inexistant

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
        "date_begining": date_begining,
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
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    with open(data_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Tâche {display_text} : {new_task}")
    self.setTasksView()