
import pymysql
from ssqatest.src.helpers.config_helpers import get_database_cred
from ssqatest.src.configs.generic_configs import GenericConfigs


def read_from_db(sql):
    # Connect to DataBase
    db_creds = get_database_cred()
    connection = pymysql.connect(host=db_creds['db_host'], port=db_creds['db_port'],
                                 user=db_creds['db_user'], password=db_creds['db_pwd'])
    """connection = pymysql.connect(host='localhost', port=8889,
                                 user='root', password='root')"""
    # Execute Query to get data
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    # return the result
    return db_data


def get_order_by_order_id(order_id, post_type):
    schema = GenericConfigs.DATABASE_SCHEMA
    table_prefix = GenericConfigs.DATABASE_TABLE_PREFIX
    sql = f"SELECT * FROM {schema}.{table_prefix}posts WHERE ID = {order_id} AND post_type = '{post_type}'"
    return read_from_db(sql)
