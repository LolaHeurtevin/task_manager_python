from PySide6.QtCore import QTimer

def display_operation_outcome(self, message, timeout=3000):
    label = self.ui.label_7  
    label.setVisible(True)
    label.setText(message)

    label.mousePressEvent = lambda event: label.setVisible(False)

    QTimer.singleShot(timeout, lambda: label.setVisible(False))

