import sys
import psycopg2
import psycopg2.extras
import json
from pprint import pprint, pformat

def connect():
    user = "postgres"
    password = "1337"
    host = "127.0.0.1"
    database = "postgres"
    port = "5432"
    connection = psycopg2.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database,
                                  port=port
                                  )
    connection.autocommit = True
    return connection

def reqDict1(script):
    connection = connect()
    cur = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute(script)
    result = cur.fetchone()
    connection.close()
    cur.close()
    return result

def reqDictn(script):
    connection = connect()
    cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(script)
    result = cur.fetchall()
    result_json = pformat(json.loads(json.dumps(result, ensure_ascii=False).encode(encoding='utf8')))
    connection.close()
    cur.close()
    return result_json


def reqSimp(script):
    try:
        connection = connect()
        cur = connection.cursor()
        cur.execute(script)
    except psycopg2.Error as e:
        print(e.pgerror)
        result = 'negative'
        connection.close()
        cur.close()
        return result
    else:
        result = 'positive'
        connection.close()
        cur.close()
        return result


