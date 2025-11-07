from Enum import Enum

class TaskState(Enum):
    TODO = "à faire"
    IN_PROGRESS = "en cours"
    DONE = "réalisé"
    ABANDONED = "abandonné"
    WAITING = "en attente"

# Définition de la classe Task
class Task():
    def __init__(self, id: int, title: str, description: str, date_begining: datetime, date_ending: datetime, comments: list, state: TaskState = TaskState.TODO):
        if not id:
            raise ValueError("L'attribut 'id' est obligatoire et ne peut pas être nul ou vide.")
        if not title:
            raise ValueError("L'attribut 'title' est obligatoire et ne peut pas être nul ou vide.")

        self.id = id
        self.title = title
        self.date_begining = date_begining
        self.date_ending = date_ending
        self.description = description
        self.state = state
        self.comments = comments