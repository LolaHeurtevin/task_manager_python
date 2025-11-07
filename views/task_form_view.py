from PySide6.QtWidgets import QMainWindow
import PySide6.QtCore as QtCore
from controllers.task_controller import filter_tasks_by_state, save_task
from PySide6.QtCore import QDateTime

class MainWindowView(QMainWindow):
    # Rendre invisible le formulaire de tâche au démarrage
    def setFormView(self, ui):
        # Widgets
        ui.label.setVisible(False)
        ui.label_2.setVisible(False)
        ui.label_3.setVisible(False)
        ui.label_4.setVisible(False)
        ui.label_5.setVisible(False)
        ui.label_6.setVisible(False)
        ui.lineEdit.setVisible(False)
        ui.dateTimeEdit.setVisible(False)
        ui.dateTimeEdit_2.setVisible(False)
        ui.pushButton_2.setVisible(False)
        ui.pushButton_4.setVisible(False)
        ui.pushButton_6.setVisible(False)
        ui.comboBox.setVisible(False)
        ui.plainTextEdit.setVisible(False)

        ui.pushButton_5.clicked.connect(lambda: self.add_new_task())
        ui.pushButton_3.clicked.connect(lambda: filter_tasks_by_state(self))
        ui.pushButton_6.clicked.connect(lambda: save_task(self))

    # Rendre visible le formulaire pour ajouter une nouvelle tâche
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

    # Afficher une tâche existante dans le formulaire
    def setTaskView(self, ui, task):
        self.add_new_task()

        if (task.get("id")):
            ui.label_5.setText(str(task.get("id")))
        
        ui.lineEdit.setText(task.get("title", ""))

        db = QDateTime.fromString(task.get("date_beginning", ""), "dd/MM/yyyy HH:mm")
        de = QDateTime.fromString(task.get("date_ending", ""), "dd/MM/yyyy HH:mm")
        ui.dateTimeEdit.setDateTime(db)
        ui.dateTimeEdit_2.setDateTime(de)

        index = ui.comboBox.findText(task.get("state", ""), QtCore.Qt.MatchFixedString)
        if index >= 0:
            ui.comboBox.setCurrentIndex(index)

        ui.plainTextEdit.setPlainText(task.get("description", ""))