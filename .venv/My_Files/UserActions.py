import sys
import psycopg2
import psycopg2.extras
from pprint import pprint
from ConfigDB import connect, reqDict1, reqDictn,reqSimp

def myuserFullInfo(my_login):
    script = ("""select * from public.persons where login like '%s';""" % (my_login))
    result = reqDict1(script)
    return result

def changePass(login,new_pwd):
    script = ("""update public.persons set password = '%s' where login like '%s';""" % (new_pwd, login))
    reqSimp(script)
    result = ('Пароль успешно сменен!\n')
    return result

def allUsersNames():
    script = ("""select fio from public.persons;""")
    result = reqDictn(script)
    return result

