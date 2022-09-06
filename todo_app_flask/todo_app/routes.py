from todo_app import app, db
from flask import render_template, redirect, url_for, request
from todo_app.models import Todo


LOG_MODE = True

def log(action: str, todo: Todo):
    if LOG_MODE: print(f"{action.capitalize()}: {todo}")


@app.route('/home')
@app.route('/')
def index():
    todo_list = Todo.query.all()

    uncomplete =  Todo.query.filter_by(complete=False).count()

    return render_template("main.html", todo_list=todo_list, uncomplete=uncomplete)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    message = request.form.get("message")
    new_todo = Todo(title=title, message=message, complete=False)

    log("new", new_todo)

    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete

    log("update", todo)

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)

    log("delete", todo)

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete_all_complete")
def delete_all_complete():

    all_done = Todo.query.filter_by(complete=True)

    for todo in all_done:
        db.session.delete(todo)

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/mark_all_complete")
def mark_all_complete():

    for todo in Todo.query.all():
        todo.complete = True

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/mark_all_incomplete")
def mark_all_incomplete():

    for todo in Todo.query.all():
        todo.complete = False

    db.session.commit()
    return redirect(url_for("index"))
