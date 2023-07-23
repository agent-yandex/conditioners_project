from data import db_session
from data.admins import Admin
from data.cities import City
from data.statuses import Status

from config import ADMIN_LOGIN, ADMIN_PASS

# файл, заполняющий необходимые начальные данные для бд

def add_cities_db():
    '''заполнение таблицы Cities'''
    db_sess = db_session.create_session()

    data_cities = ["Краснодар", "Сочи", "Адлер"]
    for city in data_cities:
        el_db = City()
        el_db.city = city
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

    el_admin = Admin()
    el_admin.login = ADMIN_LOGIN
    el_admin.set_password(ADMIN_PASS)
    db_sess.add(el_admin)

    db_sess.commit()
