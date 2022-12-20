# MyProfile app

SEPARATOR = '-' * 42

# user profile
username = ''
age = 0
phone = ''
email = ''
postcode = ''
address = '-'
info = ''
# business data
entrepreneur_num = ''
taxpayer_num = ''
checking_account = ''
bank_name = ''
bic = ''
correspondent_account = ''


def data_check(text, amount):
    while True:
        count = 0
        data_input = input(f'Введите {text}: ')
        data = ''

        for num in data_input:
            if num.isdigit():
                data += num
                count += 1

        if count == amount:
            break

        else:
            print(f'Ошибка ввода, {text} должен содержать {amount} чисел')

    return data


def general_info_user(username, age, phone, email, postcode, adress, nfo):
    print(SEPARATOR)
    print('Имя:\t\t', username)
    if 11 <= age % 100 <= 19:
        years = 'лет'

    elif age % 10 == 1:
        years = 'год'

    elif 2 <= age % 10 <= 4:
        years = 'года'

    else:
        years = 'лет'

    print('Возраст:\t', age, years)
    print('Телефон:\t', phone)
    print('E-mail:\t\t', email)
    print('Индекс:\t\t', postcode)
    print('Адрес:\t\t', adress)

    if info:
        print('\nДополнительная информация:')
        print(info)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')
    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break
    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Ифнормация о предпринимателе')
            print('0 - Назад')
            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                username = input('Введите имя: ')
                while 1:
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')
                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for digit in user_phone:
                    if digit == '+' or ('0' <= digit <= '9'):
                        phone += digit
                email = input('Введите адрес электронной почты: ')
                postcode = data_check('Введите почтовый индекс: ', 6)
                address = input('Введите почтовый адрес (без индекса): ')
                info = input('Введите дополнительную информацию:\n')
            elif option2 == 2:
                entrepreneur_num = data_check('Введите ОГРНИП: ', 15)
                taxpayer_num = data_check('Введите ИНН: ', 12)
                checking_account = data_check('Введите Расчетный счет: ', 20)
                bank_name = input('Введите название банка: ')
                bic = data_check('Введите БИК: ', 9)
                correspondent_account = data_check('Введите корреспондентский счет:  ', 20)
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')
            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(username, age, phone, email, \
                                  postcode, address, info)
            elif option2 == 2:
                general_info_user(username, age, phone, email, \
                                  postcode, address, info)
                print('\nИнформация о предпринимателе')
                print('ОГРНИП:\t\t', entrepreneur_num)
                print('ИНН:\t\t', taxpayer_num)
                print('Банковские реквезиты')
                print('Р/с:\t\t', checking_account)
                print('Банк:\t\t', bank_name)
                print('БИК:\t\t', bic)
                print('К/с:\t\t', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')