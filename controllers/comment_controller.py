import datetime
import json
import os
from controllers.task_controller import get_all_tasks
from utils.utils import display_operation_outcome

from constants import DATA_COMMENTS_PATH
from constants import DATA_TASKS_PATH

# Récupérer tous les commentaires
def get_all_comments():
    try:
        with open(DATA_COMMENTS_PATH, "r", encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_current_task_comments(self):
    id_task = int(self.ui.label_5.text())

    comments = get_all_comments()

    task_comments = []
    for comment in comments:
        if comment["task"] == id_task:
            task_comments.append(comment)

    return task_comments

def delete_comment(self, id_comment):
    from views.comments_view import CommentsViews
    data = get_all_comments()

    new_data = [comment for comment in data if int(comment.get("id", 0)) != id_comment]

    if len(new_data) == len(data):
        print(f"Aucun commentaire trouvée avec l'ID : {id_comment}")
        return

    os.makedirs(os.path.dirname(DATA_COMMENTS_PATH), exist_ok=True)
    with open(DATA_COMMENTS_PATH, "w", encoding='utf-8') as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)

    display_operation_outcome(self, "Commentaire supprimé")
    #print(f"Commentaire supprimé : {id_comment}")
    CommentsViews(self.ui).set_comments_view()

def save_comment(self, id_task):
    from views.comments_view import CommentsViews

    # Ajouter le commentaire à la liste des commentaires
    content = self.ui.plainTextEdit_2.toPlainText()
    created_at = datetime.datetime.now()

    if content == "":
        return

    data_comments = get_all_comments()

    max_comment_id = max((int(t.get("id", 0)) for t in data_comments), default=0)
    comment_id = int(max_comment_id) + 1

    new_comment = {
        "id": comment_id,
        "content": content,
        "task": id_task,
        "created_at": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    data_comments.append(new_comment)

    os.makedirs(os.path.dirname(DATA_COMMENTS_PATH), exist_ok=True)
    with open(DATA_COMMENTS_PATH, "w", encoding='utf-8') as file:
        json.dump(data_comments, file, indent=4, ensure_ascii=False)

    print(f"Commentaire créé : {new_comment}")
    
    # Attribuer le commentaire à sa tâche
    data_tasks = get_all_tasks()

    for task in data_tasks:
        if (task.get("id", 0)) == id_task:
            if "comments" not in task:
                task["comments"] = []

            task["comments"].append(comment_id)

    os.makedirs(os.path.dirname(DATA_TASKS_PATH), exist_ok=True)
    with open(DATA_TASKS_PATH, "w", encoding='utf-8') as file:
        json.dump(data_tasks, file, indent=4, ensure_ascii=False)
    print(f"Commentaire attribué")

    CommentsViews(self.ui).set_comments_view()
    display_operation_outcome(self, "Commentaire créé")
        