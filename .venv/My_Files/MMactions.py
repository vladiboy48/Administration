import sys
import psycopg2
import psycopg2.extras
from ConfigDB import reqDict1, reqDictn,reqSimp

def avtorization(login,pwd):
    script = ("""select * from persons where login = '%s' and password = '%s';""") % (login, pwd)
    result = reqDict1(script)
    if type(result) == psycopg2.extras.RealDictRow:
        avtrz_status = result.get('role')
    else:
        avtrz_status = ('--Неверный лог/пасс--')
    return avtrz_status
def registration(fio,login,pwd):
    try:
        script = ("""insert into public.persons (fio,login,password) values ('%s', '%s', '%s');""" % (fio, login, pwd))
        reqSimp(script)
    except Exception as owibka:
        reg_status = ('--Задайте другой логин -, такой уже существует--')
    else:
        reg_status = ('Регистрация прошла успешно!')
    return reg_status
