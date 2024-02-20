import os


def get_base_url():
    env = os.environ.get('ENV', 'test')

    if env.casefold() == 'test':
        return 'http://localhost:8888/quicksite'
    else:
        raise Exception('Unknown environment')


def get_database_cred():

    env = os.environ.get("ENV", "test")

    db_user = os.environ.get("DB_USER", "root")
    db_pwd = os.environ.get("DB_PASSWORD", "root")
    if not db_user or not db_pwd:
        raise Exception("Environment variables 'DB_USER' and 'DB_PASSWORD' should be set.")

    if env == "test":
        db_host = 'localhost'
        db_port = 8889
    elif env == "prod":
        db_host = 'demostore.supersqa.com'
        db_port = 3306
    else:
        raise Exception(f"Unknown environtment: {env}")

    db_info = {"db_host": db_host, "db_port": db_port, "db_user": db_user, "db_pwd": db_pwd}
    return db_info
