## Тест коммита
import sys
import psycopg2
import psycopg2.extras
from pprint import pprint
from ConfigDB import connect, reqDict1, reqDictn,reqSimp

def allusersFullInfo():
    script = ("""select * from persons order by pers_id asc;""")
    result_json = reqDictn(script)
    return result_json


def deleteUser(enter_login):
    script = ("""select * from persons where login = '%s';""") % (enter_login) #Проверка наличия пользователя в системе
    result = reqDict1(script)
    if type(result) == psycopg2.extras.RealDictRow:
        script = ("""delete from public.persons where login = '%s';""" % (enter_login))
        reqSimp(script)
        del_result = 'positive'
    else:
        del_result = 'negative'
    return del_result

def changeANYadm(enter_login,enter_pole,new_value):
    script = ("""select * from persons where login = '%s';""") % (enter_login)
    result = reqDict1(script)
    if type(result) == psycopg2.extras.RealDictRow:
        script = ("""update public.persons set %s = '%s' where login like '%s' ;""" % (enter_pole, new_value, enter_login,))
        result= reqSimp(script)
        if result == 'negative':
            change_result = 'При апдейте возникла ошибка\n Скорректируйте значения и проверьте логи.'
        elif result == 'positive':
            change_result = 'Апдейт успешный!'
    else:
        change_result = 'Такого пользователя не существует'
    return change_result