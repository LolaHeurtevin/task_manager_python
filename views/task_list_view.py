from controllers.task_controller import get_all_tasks
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QMainWindow
from views.task_form_view import MainWindowView
from functools import partial

class TaskView(QMainWindow):
    def setTasksView(self, ui):
        data = get_all_tasks()

        if not data:
            label = QLabel("Aucune tâche à afficher.")
            ui.verticalLayout.addWidget(label)
            return

        # Delete existing task cards
        while ui.verticalLayout.count():
            child = ui.verticalLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add the updated task cards
        for task in data:
            title = task.get("title", "Sans titre")

            #card = QFrame()
            #card.setFrameShape(QFrame.StyledPanel)
            #card.setStyleSheet("background-color: #f0f0f0; border-radius: 5px; padding: 10px;")

            button = QPushButton(title)
            button.setStyleSheet("text-align: left; padding: 10px; font-weight: bold;")
            button.clicked.connect(partial(self.setTaskView, ui, task))

            label = QLabel(title)
            label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")

            #layout = QVBoxLayout(card)
            layout = QVBoxLayout(button)
            layout.addWidget(label)

            #ui.verticalLayout.addWidget(card)
            ui.verticalLayout.addWidget(button)
            ui.verticalLayout.addStretch()
