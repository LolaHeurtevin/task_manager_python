from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow
import sys, os, subprocess, logging, datetime
import sched
import time
logger = logging.getLogger(__name__)

from views.task_form_view import MainWindowView
from views.task_list_view import TaskView

class MainWindow(MainWindowView, TaskView):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Gestionnaire de tâches")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setTasksView(self.ui)

        self.setFormView(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())