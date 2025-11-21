from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout
from PySide6.QtCore import Qt
from controllers.comment_controller import get_current_task_comments, delete_comment

class CommentsViews(QMainWindow):
    def __init__(self, ui):
        self.ui = ui
        
    def add_comment_view(self):
        self.ui.plainTextEdit_2.setVisible(True)

    def set_comments_view(self):
        self.ui.plainTextEdit_2.setPlainText('')
        comments = get_current_task_comments(self)

        if not comments:
            self.ui.scrollArea_2.setVisible(False)
            return
        else:
            self.ui.scrollArea_2.setVisible(True)

        if self.ui.scrollAreaWidgetContents_2.layout() is None:
            self.comments_layout = QVBoxLayout()
            self.ui.scrollAreaWidgetContents_2.setLayout(self.comments_layout)
        else:
            self.comments_layout = self.ui.scrollAreaWidgetContents_2.layout()

        # Supprimer commentaires existants
        while self.comments_layout.count():
            child = self.comments_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # AJouter les commentaires mis à jour
        for comment in comments:
            content = comment.get("content", "(vide)")
            comment_id = comment.get("id")

            card = QFrame()
            card.setFrameShape(QFrame.StyledPanel)
            card.setStyleSheet("background-color: #f0f0f0; border-radius: 5px; padding: 10px;")

            card.comment_id = comment_id

            card_layout = QHBoxLayout(card)

            # Texte du commentaire
            label = QLabel(content)
            label.setStyleSheet("font-size: 16px; color: #333;")

            # Bouton supprimer
            delete_btn = QPushButton("Supprimer")
            delete_btn.setStyleSheet(
                "background-color: #cc4444; color: white; border-radius: 5px; padding: 4px 8px;"
            )
            delete_btn.setCursor(Qt.PointingHandCursor)

            delete_btn.clicked.connect(lambda _, cid=comment_id: delete_comment(self, cid))

            card_layout.addWidget(label)
            card_layout.addStretch()
            card_layout.addWidget(delete_btn)

            self.comments_layout.addWidget(card)

        self.comments_layout.addStretch()




