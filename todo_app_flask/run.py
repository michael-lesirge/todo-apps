from todo_app import app

DEBUG = True
HOST = "127.0.0.1"

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST)
