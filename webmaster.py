from app import app, db
from app.models import User, Post, Reactions, Courses, Signups, Session, Responses, Prompts
import random

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Reactions': Reactions, 'Courses': Courses, 'Signups': Signups, 'random': random, 'Session': Session, 'Responses': Responses, 'Prompts': Prompts}
