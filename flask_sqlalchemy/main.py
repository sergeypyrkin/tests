# test_app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

file_path = os.path.abspath(os.getcwd()) + "\database.db"
# создаем приложение
app = Flask(__name__)
# загружаем конфигурацию
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path

# передаем объект приложения `app` в `SQLAlchemy`
db = SQLAlchemy(app)


def init_db():
    with app.app_context():
        db.create_all()


def add_user(name, semail):
    with app.app_context():
        admin = User(username=name, email=semail)
        db.session.add(admin)
        db.session.commit()


def set_users(i):
    with app.app_context():
        for x in range(1, i):
            u = User(username="test" + str(x), email="test email" + str(x))
            db.session.add(u)
            db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# первый запуск
# init_db():
# add_user - почемуто так
# add_user("sergey2", "sdf3")


def getUser(name):
    with app.app_context():
        u = User.query.filter_by(username=name).first()
        print(u)

# getUser("sergey2")
#set_users(100)

#########################
#  пакеты лучше ставить черешь env а не pip
#
#  долго ебался но запустилось тока так:
#
#   file_path = os.path.abspath(os.getcwd()) + "\database.db"
#      with app.app_context():
#         db.create_all()
#
#
#
#  можно контект прокидывать и выполнять вот так
#  from main import app
#       app.app_context().push()
#       User.query.filter_by(username=name).first()
#
#
#
#  Согласно документации Flask существует два вида контекстов:
#
# Контекст приложения
# Контекст запроса
# Контекст приложения используется для хранения общих переменных приложения, таких как подключение к базе данных, настройки и т. д. А контекст запроса используется для хранения переменных конкретного запроса.
#
# Контекст приложения предлагает такие объекты как current_app или g.
# current_app ссылается на экземпляр, который обрабатывает запрос, а g

#
# отсюда можно скачать просмотрщик: https://sqlitebrowser.org/dl/
#
