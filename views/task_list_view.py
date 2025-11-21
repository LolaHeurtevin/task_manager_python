from controllers.task_controller import get_all_tasks
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QMainWindow
from views.task_form_view import MainWindowView
from controllers.task_controller import get_filtered_tasks
from functools import partial

class TaskView(QMainWindow):
    def set_tasks_view(self, filtered = False):
        if (filtered):
            data = get_filtered_tasks(self)
        else: 
            data = get_all_tasks()

        if not data:
            self.ui.scrollArea.setVisible(False)
            return
        else:
            self.ui.scrollArea.setVisible(True)

        if self.ui.scrollAreaWidgetContents.layout() is None:
            self.tasks_layout = QVBoxLayout()
            self.ui.scrollAreaWidgetContents.setLayout(self.tasks_layout)
        else:
            self.tasks_layout = self.ui.scrollAreaWidgetContents.layout()

        # Delete existing comments cards
        while self.tasks_layout.count():
            child = self.tasks_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add the updated task cards
        for task in data:
            title = task.get("title", "Sans titre")

            #card = QFrame()
            #card.setFrameShape(QFrame.StyledPanel)
            #card.setStyleSheet("background-color: #f0f0f0; border-radius: 5px; padding: 10px;")

            button = QPushButton(title)
            button.setStyleSheet("text-align: left; padding: 5px; font-weight: bold;")
            button.clicked.connect(partial(self.set_task_view, task))

            label = QLabel(title)
            label.setStyleSheet("font-size: 16px; color: #333;")

            #layout = QVBoxLayout(card)
            layout = QVBoxLayout(button)
            layout.addWidget(label)

            #ui.verticalLayout.addWidget(card)
            self.tasks_layout.addWidget(button)

        self.tasks_layout.addStretch()
