from data import db_session
from data.users import User
from data.problems import Problem
from data.statuses import Status

from config import ADMIN_NAME, ADMIN_NUM, ADMIN_PASS

# файл, заполняющий необходимые начальные данные для бд


def add_problems_db():
    '''заполнение таблицы Problems'''
    db_sess = db_session.create_session()

    data_problems = ["Проблема1", "Проблема2"]
    for problem in data_problems:
        el_db = Problem()
        el_db.problem = problem
        db_sess.add(el_db)

    db_sess.commit()


def add_statuses_db():
    '''заполнение таблицы Statuses'''
    db_sess = db_session.create_session()

    data_statuses = ["В обработке", "Назначена встреча", "Выполнено"]
    for status in data_statuses:
        el_db = Status()
        el_db.status = status
        db_sess.add(el_db)

    db_sess.commit()


def add_admin_db():
    '''добавление админа в бд'''
    db_sess = db_session.create_session()

    el_user = User()
    el_user.name = ADMIN_NAME
    el_user.number = ADMIN_NUM
    el_user.set_password(ADMIN_PASS)
    el_user.type = 1
    db_sess.add(el_user)

    db_sess.commit()
