import sys
import flet
from MMactions import registration, avtorization
from AdminActions import allusersFullInfo, deleteUser, changeANYadm
from UserActions import myuserFullInfo, changePass, allUsersNames
from pprint import pprint


def main(page1: flet.Page):
    def changeTheme(a):
        if page1.theme_mode == 'light':
            page1.theme_mode = 'dark'
        else:
            page1.theme_mode = 'light'
        page1.update()

    def navigate_bar(index):
        index = page1.navigation_bar.selected_index
        page1.clean()
        if index == 0:
            fio.value = ''
            login.value = ''
            pwd.value = ''
            page1.add(panel_MM)
        elif index == 1:
            page1.add(panel_reg)
        elif index == 2:
            page1.window.close()

    def navigate_btns(index):
        page1.clean()
        if index == 0:
            fio.value = ''
            login.value = ''
            pwd.value = ''
            page1.add(panel_MM)
        elif index == 1:
            page1.add(panel_reg)
        elif index == 2:
            page1.window.close()
        elif index == 3:
            page1.add(panel_admin)
        elif index == 4:
            page1.add(panel_user)

    # Функции главного меню
    def avtorization_here(a):
        avtrz_status = avtorization(login.value, pwd.value)
        if avtrz_status == 'admin':
            navigate_btns(3)
        elif avtrz_status == 'user':
            navigate_btns(4)
        elif avtrz_status == '--Неверный лог/пасс--':
            page1.add(
                flet.Row([
                    flet.Text(value=avtrz_status)], alignment=flet.MainAxisAlignment.CENTER
                )
            )
            page1.update()

    def registratoin_here(a):
        reg_status = registration(fio.value, login.value, pwd.value)
        page1.add(
            flet.Row([
                flet.Text(value=reg_status)], alignment=flet.MainAxisAlignment.CENTER
            )
        )
        if reg_status == 'Регистрация прошла успешно!':
            page1.update()
        elif reg_status == '--Задайте другой логин -, такой уже существует--':
            login.value = ''
            page1.update()

    def valiadtion_avtor(a):  # Проверяем заполненность полей
        if all([login.value, pwd.value]):
            btn_avtrz.disabled = False
        else:
            btn_avtrz.disabled = True
        page1.update()

    def valiadtion_reg(a):  # Проверяем заполненность полей
        if all([login.value, pwd.value, fio.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True
        page1.update()

    def allusersFullInfo_here(a):
        result = allusersFullInfo()
        page1.add(
            flet.Row(
                [
                    flet.Column(
                        [
                            flet.Text(value=('Тут пока не красиво')),
                            flet.Text(value=result)
                        ], alignment=flet.MainAxisAlignment.CENTER
                    )
                ]
            )
        )
        page1.update()

    def deletion(a):
        def delete_here(a):
            del_result = deleteUser(enter_login.value)
            page1.add(
                flet.Row([
                    flet.Text(value=del_result)], alignment=flet.MainAxisAlignment.CENTER
                )
            )
            if del_result == '--Задайте другой логин - такого пользователя не существует!--':
                login.value = ''

        enter_login = flet.TextField(label='Задай login юзера, которого необходимо удалить', value='', width=300)
        fio.value = ''
        login.value = ''
        pwd.value = ''
        page1.clean()
        page1.add(
            flet.Row(
                [flet.Column(
                    [
                        enter_login,
                        flet.ElevatedButton(text='Удалить', width=200, on_click=delete_here)
                    ]
                )
                ]
            )
        )

    def changeAny(a): #Не реализовано доделать изменение поля (админка)
        def changeAnyhere(a):
            change_res = changeANYadm(enter_login.value,enter_pole.value,new_value.value)
            page1.add(
                flet.Row([
                    flet.Text(value=change_res)], alignment=flet.MainAxisAlignment.CENTER
                )
            )
        enter_login = flet.TextField(label='Задай login юзера, которого необходимо изменить', value='', width=300)
        enter_pole = flet.TextField(label='Задай поле которое хочешь поменять', value='', width=300)
        new_value = flet.TextField(label='Задай новон значение этого поля', value='', width=300)
        fio.value = ''
        login.value = ''
        pwd.value = ''
        page1.clean()
        page1.add(
            flet.Row(
                [flet.Column(
                    [
                        enter_login,
                        enter_pole,
                        new_value,
                        flet.ElevatedButton(text='Задать!', width=200, on_click=changeAnyhere)
                    ]
                )
                ]
            )
        )

    # Функции юзера

    def myuserFullInfo_here(a):
        result = myuserFullInfo(login.value)
        page1.add(
            flet.Row(
                [
                    flet.Column(
                        [
                            flet.Text(value=('Тут пока не красиво')),
                            flet.Text(value=result)
                        ], alignment=flet.MainAxisAlignment.CENTER
                    )
                ]
            )
        )
        page1.update()

    def changePass_here(a): #Не реализовано  доделать изменение поля (админка)
        pass

    def allUsersNames_here(a):
        result = allUsersNames()
        page1.add(
            flet.Row(
                [
                    flet.Column(
                        [
                            flet.Text(value=('Тут пока не красиво')),
                            flet.Text(value=result)
                        ], alignment=flet.MainAxisAlignment.CENTER
                    )
                ]
            )
        )
        page1.update()

    # Начало самой функции MAIN
    page1.title = "Loin-dialog"
    page1.theme_mode = 'light'
    page1.vertical_alignment = flet.MainAxisAlignment.CENTER
    page1.g_alignment = flet.MainAxisAlignment.CENTER
    page1.window.height = 600
    page1.window.width = 400
    page1.window.resizable = True

    index = 0
    login = flet.TextField(label='Enter Login', value='', width=300, on_change=valiadtion_avtor)
    pwd = flet.TextField(label='Enter Password', password=True, value='', width=300, on_change=valiadtion_avtor)
    fio = flet.TextField(label='Enter fio', width=300, on_change=valiadtion_reg)

    # Кнопки главного меню
    btn_avtrz = flet.ElevatedButton(text='Авторизация', width=200, disabled=True, on_click=avtorization_here)
    btn_reg = flet.ElevatedButton(text='Регистрация', width=200, disabled=True, on_click=registratoin_here)

    # Кнопки админского меню
    adm_btn_1 = flet.ElevatedButton(text='1. Полнная инфа по всем пользователям', width=200,
                                    on_click=allusersFullInfo_here)
    adm_btn_2 = flet.ElevatedButton(text='2. Удалить пользователя', width=200, on_click=deletion)
    adm_btn_3 = flet.ElevatedButton(text='3. Апдейт данных пользоваля', width=200, on_click=changeAny)

    # Кнопки юзерского меню
    user_bnt_1 = flet.ElevatedButton(text='1. Полная инфа про мой аккаунт.', width=200, on_click=myuserFullInfo_here)
    user_bnt_2 = flet.ElevatedButton(text='2. Сменить пароль', width=200, on_click=changePass_here)
    user_bnt_3 = flet.ElevatedButton(text='3. Список всех пользователей', width=200, on_click=allUsersNames_here)

    panel_MM = flet.Row((
        [flet.Column(
            [
                flet.Row([
                    (flet.IconButton(flet.icons.SUNNY, on_click=changeTheme)),
                    (flet.Text('<--Сменить тему'))], alignment=flet.MainAxisAlignment.CENTER),
                flet.Text('Добро пожаловать в главное меню!'),
                flet.Text('Собстна летс го'),
                login,
                pwd,
                btn_avtrz
            ]
        )
        ]
    ), alignment=flet.MainAxisAlignment.CENTER)

    panel_reg = flet.Row((
        [
            flet.Column(
                [
                    flet.Row([
                        (flet.IconButton(flet.icons.SUNNY, on_click=changeTheme)),
                        (flet.Text('<--Сменить тему'))], alignment=flet.MainAxisAlignment.CENTER),
                    flet.Text('--Окно регистрации--\nЗаполни все поля и кнопка станет активна!'),
                    flet.Text('Собстна вводи'),
                    fio,
                    login,
                    pwd,
                    btn_reg
                ]
            )
        ]
    ), alignment=flet.MainAxisAlignment.CENTER)

    panel_admin = flet.Row((
        [
            flet.Column(
                [
                    flet.Row([
                        (flet.IconButton(flet.icons.SUNNY, on_click=changeTheme)),
                        (flet.Text('<--Сменить тему'))], alignment=flet.MainAxisAlignment.CENTER),
                    flet.Text('--Админская панель--\nВам,как админу, доступны следующие действия:'),
                    adm_btn_1,
                    adm_btn_2,
                    adm_btn_3
                ]
            )
        ]
    ), alignment=flet.MainAxisAlignment.CENTER)

    panel_user = flet.Row((
        [
            flet.Column(
                [
                    flet.Row([
                        (flet.IconButton(flet.icons.SUNNY, on_click=changeTheme)),
                        (flet.Text('<--Сменить тему'))], alignment=flet.MainAxisAlignment.CENTER),
                    flet.Text('-->Юзеркская панель--\nВам, как пользователю, доступны слдедующие действия'),
                    user_bnt_1,
                    user_bnt_2,
                    user_bnt_3
                ]
            )
        ]
    ), alignment=flet.MainAxisAlignment.CENTER)

    page1.navigation_bar = flet.NavigationBar(
        destinations=[
            flet.NavigationBarDestination(icon=flet.icons.HOME, label='Меню авторизации'),
            flet.NavigationBarDestination(icon=flet.icons.VERIFIED_USER_OUTLINED, label='Меню регистрации'),
            flet.NavigationBarDestination(icon=flet.icons.EXIT_TO_APP, label='Выход')
        ], on_change=navigate_bar
    )

    navigate_bar(0)  # Запуск первой страницы


flet.app(target=main, view=flet.AppView.FLET_APP)  # Сам запуск приложения и его вид
sys.exit()
