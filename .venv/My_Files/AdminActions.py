import sys
import psycopg2
import psycopg2.extras
from pprint import pprint
from ConfigDB import connect, reqDict1, reqDictn,reqSimp

def allusersFullInfo():
    script = ("""select * from persons order by pers_id asc;""")
    result = reqDictn(script)
    return result


def deleteUser(enter_login):
    try:
        script = ("""delete from public.persons where login like '%s';""" % (enter_login))
        reqSimp(script)
    except Exception as owibka:
        del_result = '--Задайте другой логин - такого пользователя не существует!--'
    else:
        del_result = 'Удаление прошло успешно!'
    return del_result

def changeANYadm(enter_login,enter_pole,new_value):
    script = ("""select * from persons where login = '%s';""") % (enter_login)
    result = reqDict1(script)
    if type(result) == psycopg2.extras.RealDictRow:
        try:
            script = ("""update public.persons set %s = '%s' where login like '%s' ;""" % (enter_pole, new_value, login,))
            reqSimp(script)
        except Exception as owibka:
            change_result = owibka
        else:
            change_result = 'Апдейт успешный!'
    else:
        change_result = 'Такого пользователя не существует'
    return change_result