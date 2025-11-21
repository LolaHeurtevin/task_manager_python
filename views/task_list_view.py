from controllers.task_controller import get_all_tasks
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QMainWindow
from views.task_form_view import MainWindowView
from controllers.task_controller import get_filtered_tasks
from functools import partial

class TaskView(QMainWindow):
    def set_tasks_view(self, filtered=False):
        if filtered:
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

        while self.tasks_layout.count():
            child = self.tasks_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for task in data:
            title = task.get("title", "Sans titre")

            card = QFrame()
            card.setFrameShape(QFrame.StyledPanel)
            card.setStyleSheet("background-color: #f0f0f0; border-radius: 5px; padding: 5px;")
            
            card_layout = QVBoxLayout(card)

            label = QLabel(title)
            label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
            card_layout.addWidget(label)

            button = QPushButton("Accéder")
            button.clicked.connect(partial(self.set_task_view, task))
            card_layout.addWidget(button)

            self.tasks_layout.addWidget(card)

        self.tasks_layout.addStretch()
