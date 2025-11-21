from PySide6.QtWidgets import QMainWindow
import PySide6.QtCore as QtCore
from controllers.task_controller import filter_tasks_by_state, save_task, delete_task, close_task
from views.comments_view import CommentsViews

from PySide6.QtCore import QDateTime

class MainWindowView(QMainWindow):
    # Rendre invisible le formulaire de tâche au démarrage
    def set_form_view(self, ui):
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
        ui.pushButton_7.setVisible(False)
        ui.comboBox.setVisible(False)
        ui.plainTextEdit.setVisible(False)
        ui.plainTextEdit_2.setVisible(False)
        ui.scrollArea_2.setVisible(False)

        ui.pushButton_2.clicked.connect(lambda: CommentsViews(ui).add_comment_view())
        ui.pushButton_3.clicked.connect(lambda: filter_tasks_by_state(self))
        ui.pushButton_4.clicked.connect(lambda: close_task(self))
        ui.pushButton_5.clicked.connect(lambda: self.set_new_task_view())
        ui.pushButton_6.clicked.connect(lambda: save_task(self))
        ui.pushButton_7.clicked.connect(lambda: delete_task(self))


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
        self.ui.pushButton_7.setVisible(True)
        self.ui.comboBox.setVisible(True)
        self.ui.plainTextEdit.setVisible(True)
        self.ui.plainTextEdit_2.setVisible(False)
        self.ui.scrollArea_2.setVisible(True)
        self.ui.scrollArea_2.setVisible(False)

    # Afficher une tâche existante dans le formulaire
    def set_task_view(self, task):
        self.add_new_task()

        if (task.get("id")):
            self.ui.label_5.setText(str(task.get("id")))
        
        self.ui.lineEdit.setText(task.get("title", ""))

        print("Date JSON:", task.get("date_beginning", ""))
        db = QDateTime.fromString(task.get("date_beginning", ""), "dd/MM/yyyy HH:mm")
        print("QDateTime valide ?", db.isValid())


        db = QDateTime.fromString(task.get("date_beginning", ""), "dd/MM/yyyy HH:mm")
        de = QDateTime.fromString(task.get("date_ending", ""), "dd/MM/yyyy HH:mm")
        self.ui.dateTimeEdit.setDateTime(db)
        self.ui.dateTimeEdit_2.setDateTime(de)

        index = self.ui.comboBox.findText(task.get("state", ""), QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui.comboBox.setCurrentIndex(index)

        self.ui.plainTextEdit.setPlainText(task.get("description", ""))

        CommentsViews(self.ui).set_comments_view()

    def set_new_task_view(self):
        self.add_new_task()
        date = QDateTime.fromString("01/01/2000 00:00", "dd/MM/yyyy HH:mm")

        self.ui.lineEdit.setText("")
        self.ui.dateTimeEdit.setDateTime(date)
        self.ui.dateTimeEdit_2.setDateTime(date)
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.plainTextEdit.setPlainText("")
        self.ui.label_5.setText("")