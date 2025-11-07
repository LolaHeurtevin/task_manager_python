from controllers.task_controller import get_all_tasks
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QMainWindow
from views.task_form_view import MainWindowView
from controllers.task_controller import get_filtered_tasks
from functools import partial

class TaskView(QMainWindow):
    def setTasksView(self, filtered = False):
        if (filtered):
            data = get_filtered_tasks(self)
        else: 
            data = get_all_tasks()

        if not data:
            self.ui.scrollArea.setVisible(False)
            return
        else:
            self.ui.scrollArea.setVisible(True)

        # Delete existing task cards
        while self.ui.verticalLayout.count():
            child = self.ui.verticalLayout.takeAt(0)
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
            button.clicked.connect(partial(self.setTaskView, task))

            label = QLabel(title)
            label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")

            #layout = QVBoxLayout(card)
            layout = QVBoxLayout(button)
            layout.addWidget(label)

            #ui.verticalLayout.addWidget(card)
            self.ui.verticalLayout.addWidget(button)
            self.ui.verticalLayout.addStretch()
