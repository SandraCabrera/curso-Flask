from app.models import User, Post
from app import app, db

app.run()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}