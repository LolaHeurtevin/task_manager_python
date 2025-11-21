class Comment():
    def __init__(self, id: int, content: str, task: int, created_at: datetime):
        if not id:
            raise ValueError("L'attribut 'id' est obligatoire et ne peut pas être nul ou vide.")
        if not content:
            raise ValueError("L'attribut 'contenu' est obligatoire et ne peut pas être nul ou vide.")
        if not task:
            raise ValueError("L'attribut 'task' est obligatoire et ne peut pas être nul ou vide.")

        self.id = id
        self.content = content
        self.task = task
        self.created_at = created_at