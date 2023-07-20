from flask import Flask, render_template

from data import db_session
from data.users import User
from data.problems import Problem
from data.requests import Request
from data.statuses import Status

from config import FLASK_KEY, DB_NAME

app = Flask(__name__)
app.config["SECRET_KEY"] = FLASK_KEY

db_session.global_init(DB_NAME)
