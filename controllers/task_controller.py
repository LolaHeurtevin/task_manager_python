import json
import os

def filter_tasks_by_state():
    pass

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

    # Récupérer l'ID s'il y en a, sinon None
    id_text = self.ui.label_5.text().strip()
    if id_text:
        task_id = int(id_text)
    else:
        # nouvel id : max(existing ids) + 1, ou 1 si liste vide
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

    # Chercher si l'ID existe déjà
    found = False
    for i, existing in enumerate(data):
        if int(existing.get("id")) == task_id:
            data[i] = new_task     # remplace l'élément existant par la nouvelle tâche
            found = True
            display_text = "mise à jour"
            break

    if not found:
        data.append(new_task)
        display_text = "créée"

    # Sauvegarde
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    with open(data_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Tâche {display_text} : {new_task}")