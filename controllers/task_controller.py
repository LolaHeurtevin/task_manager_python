import json
import os

def filter_tasks_by_state():
    pass

def add_new_task(self):
    self.ui.label.setVisible(True)
    self.ui.label_2.setVisible(True)
    self.ui.label_3.setVisible(True)
    self.ui.label_4.setVisible(True)
    self.ui.label_6.setVisible(True)
    self.ui.lineEdit.setVisible(True)
    self.ui.dateTimeEdit.setVisible(True)
    self.ui.dateTimeEdit_2.setVisible(True)
    self.ui.pushButton_2.setVisible(True)
    self.ui.pushButton_4.setVisible(True)
    self.ui.pushButton_6.setVisible(True)
    self.ui.comboBox.setVisible(True)
    self.ui.plainTextEdit.setVisible(True)

def get_all_tasks():
    data_path = "data/data.json"
    try:
        with open(data_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_task(self):
    title = self.ui.lineEdit.text()
    description = self.ui.plainTextEdit.toPlainText()
    date_begining = self.ui.dateTimeEdit.text()
    date_ending = self.ui.dateTimeEdit_2.text()
    state = self.ui.comboBox.currentText()

    if title:
        data_path = "data/data.json"
        
        data = get_all_tasks()

        # Créer ou récupérer l'ID
        if (self.ui.label_5.text()):
            id = self.ui.label_5.text() 
        elif data:
            id = max(int(task.get('id', 0)) for task in data) + 1

        # Créer la nouvelle tâche
        new_task = {
            "id": id,
            "title": title,
            "description": description,
            "date_begining": date_begining,
            "date_ending": date_ending,
            "state": state
        }
        
        # Ajouter ou mettre à jour la tâche
        found = False
        for i, task in enumerate(data):
            if str(task.get('id')) == str(id):
                data[i] = new_task
                found = True
                break
        if not found:
            data.append(new_task)

        # Sauvegarder les données
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        with open(data_path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Sauvegarde effectuée : {new_task}")

