from PySide6.QtWidgets import QMainWindow
import PySide6.QtCore as QtCore
from controllers.task_controller import add_new_task, filter_tasks_by_state, save_task
from PySide6.QtCore import QDateTime

class MainWindowView(QMainWindow):
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

        ui.pushButton_5.clicked.connect(lambda: add_new_task(self))
        ui.pushButton_3.clicked.connect(lambda: filter_tasks_by_state(self))
        ui.pushButton_6.clicked.connect(lambda: save_task(self))

    def setTaskView(self, ui, task):
        add_new_task(self)
        
        ui.lineEdit.setText(task.get("title", ""))

        db = QDateTime.fromString(task.get("date_beginning", ""), "dd/MM/yyyy HH:mm")
        de = QDateTime.fromString(task.get("date_ending", ""), "dd/MM/yyyy HH:mm")
        ui.dateTimeEdit.setDateTime(db)
        ui.dateTimeEdit_2.setDateTime(de)

        index = ui.comboBox.findText(task.get("state", ""), QtCore.Qt.MatchFixedString)
        if index >= 0:
            ui.comboBox.setCurrentIndex(index)

        ui.plainTextEdit.setPlainText(task.get("description", ""))