from flask import Flask, render_template

from data import db_session
from data.users import User
from data.problems import Problem
from data.requests import Request
from data.statuses import Status

from config import FLASK_KEY, DB_NAME

from complete_db import add_problems_db, add_statuses_db, add_admin_db

app = Flask(__name__)
app.config["SECRET_KEY"] = FLASK_KEY


def complete_initial_db():
    '''начальное заполнение дб'''
    db_session.global_init(DB_NAME)

    add_problems_db()
    add_statuses_db()
    add_admin_db()


