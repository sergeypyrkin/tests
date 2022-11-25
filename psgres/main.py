import psycopg2
from psycopg2 import OperationalError


# создание соединения
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    "localdb", "postgres", "admin", "127.0.0.1", "5432"
)


# создание базы данных
def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_database_query = "CREATE DATABASE sm_app"


# create_database(connection, create_database_query)
# запросы
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def create_table():
    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts (
      id SERIAL PRIMARY KEY, 
      title TEXT NOT NULL, 
      description TEXT NOT NULL, 
      user_id INTEGER REFERENCES users(id)
    )
    """

    execute_query(connection, create_posts_table)


# вставляем записи
def insert_simple():
    create_users = """
    INSERT INTO
      users (name, age, gender, nationality)
    VALUES
      ('James', 25, 'male', 'USA'),
      ('Leila', 32, 'female', 'France'),
      ('Brigitte', 35, 'female', 'England'),
      ('Mike', 40, 'male', 'Denmark'),
      ('Elizabeth', 21, 'female', 'Canada');
    """

    execute_query(connection, create_users)

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      name TEXT NOT NULL, 
      age INTEGER,
      gender TEXT,
      nationality TEXT
    )
    """

    execute_query(connection, create_users_table)


def insert_other_way():
    users = [
        ("James1", 25, "male", "USA"),
        ("Leila1", 32, "female", "France"),
        ("Brigitte1", 35, "female", "England"),
        ("Mike1", 40, "male", "Denmark"),
        ("Elizabeth1", 21, "female", "Canada"),
    ]

    user_records = ", ".join(["%s"] * len(users))

    insert_query = (
        f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
    )

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(insert_query, users)


# тут извлечение
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def find_users():
    select_users = "SELECT * from users"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)

find_users()


# просто божественный гайд тут:
# https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27