from todo_app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    message = db.Column(db.String(300))
    complete = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f"Todo(title={repr(self.title)}, complete={self.complete})"
