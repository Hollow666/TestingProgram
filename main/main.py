import os, sys
import linecache

cfg_filename = 'config.cfg'
admin_passwd = ''
q_list = None
a_list = None
q_list_length = ''
a_list_length = ''



def First_start():
    global cfg_filename
    global admin_passwd
    file = open(cfg_filename, 'w')
    inpt = ''
    while inpt == '':
        inpt = input('Задайте пароль администратора: ')
    file.write(inpt)
    file.close()
    with open(cfg_filename, 'r') as file:
        admin_passwd = file.readline()


def q_read():
    global q_list
    global q_list_length
    try:
        os.system('cls')
        path = input('Путь к файлу с вопросами:')
        file = open(path, 'r')
    except FileNotFoundError:
        os.system('cls')
        print ('ERROR: Введен неверный путь или файл не найден.')
    else:
        q_list = file.read().split('\n')
        q_list_length = len(q_list)
        try:
            cfg = open('config.cfg', 'a')
        except FileNotFoundError:
            os.system('cls')
            print ('ERROR: Не найден файл конфига.')
        else:
            str_to_write = q_list[0]
            for i in range(1, q_list_length - 1, 1):
                str_to_write = str_to_write + f'#&#{q_list[i]}'
            rewrite = linecache.getline('config.cfg', 3).split()
            if len(rewrite) == 0:
                cfg.write(f'\n{q_list_length}')
                cfg.write(f'\n{str_to_write}')
            else:
                content = cfg.readlines()
                temp = [f'{content[0]}', f'{q_list_length}', f'{str_to_write}']
                str_to_rewrite = f'{temp[0]}{temp[1]}\n{temp[2]}'
                content = cfg.read()
                temp_1 = content.split('\n')
                cfg_rewrite = content.replace(f'{temp_1[0]}{temp_1[1]}{temp_1[2]}', str_to_rewrite)
                cfg.close()
                try:
                    cfg = open('config.cfg', 'w')
                except FileNotFoundError:
                    os.system('cls')
                    print ('ERROR: Не найден файл конфига.')
                else:
                    cfg.write(cfg_rewrite)
                finally:
                    cfg.close()
        finally:
            cfg.close()
    finally:
        file.close()


def a_read():
    global a_list
    try:
        os.system('cls')
        path = input('Путь к файлу с ответами:')
        file = open(path, 'r')
    except FileNotFoundError:
        os.system('cls')
        print ('ERROR: Введен неверный путь или файл не найден.')
    else:
        a_list = file.readline().split('#&#')
    finally:
        file.close()


def change_passwd():
    pass

def print_menu():
    print ('\t\t\tМЕНЮ\n1. Панель администратора.\n2. Начать тестирование\n3. Выход.')


def print_admin_menu():
    print ('\t\t\tМЕНЮ АДМИНИСТРАТОРА\n1. Считать вопросы и ответы из файла.\n2. Изменить пароль.\n3. Справка.\n4. Выйти в главное меню.')


def print_info():
    print ('\t\t\tИНФОРМАЦИЯ\n\t1. ')
    os.system('pause')


def main_menu():
    global admin_passwd
    inpt = ''
    while inpt == '' and (inpt != '1' or inpt != '2' or inpt != '3'):
        os.system('cls')
        print_menu()
        inpt = input('Ввод: ')
        if not(inpt == '1' or inpt == '2' or inpt == '3'):
            inpt = ''
        else:
            break
    return inpt


def admin_menu():
    inpt = ''
    while inpt == '' and (inpt != '1' or inpt != '2' or inpt != '3'):
        os.system('cls')
        print_admin_menu()
        inpt = input('Ввод: ')
        if not(inpt == '1' or inpt == '2' or inpt == '3' or inpt == '4'):
            inpt = ''
        else:
            break
    return inpt
            
    


def app():
    #flag = True  
    while True:
        inpt = main_menu()
        if inpt == '1':
            fl = True 
            while fl:
                os.system('cls')
                print ('Введите пароль. Чтобы вернуться в меню cancel.')
                ans = input('Пароль: ')
                if ans == admin_passwd:
                    am_flag = True
                    while am_flag:
                        a_m_inpt = admin_menu()
                        if a_m_inpt == '1':
                            q_read()
                            #a_read()
                        elif a_m_inpt == '2':
                            #change_passwd()
                            pass
                        elif a_m_inpt == '3':
                            print_info()
                        elif a_m_inpt == '4':
                            am_flag = False
                    os.system('cls')                  
                    fl = False
                elif ans == 'cancel' or ans == 'Cancel' or ans == 'CANCEL':
                    os.system('cls')                 
                    fl = False
        elif inpt == '2':
            os.system('cls')
            sys.exit()
        elif inpt == '3':
            os.system('cls')
            sys.exit()    


def main():
    global cfg_filename
    global admin_passwd
    if os.path.exists(cfg_filename):
        #file = open(cfg_filename, 'r')
        #content = file.readlines()
        content = linecache.getline('config.cfg', 1).split()
        admin_passwd = content[0]
        #file.close()
        app()
    else:
        First_start()
        app()
    


if __name__ == "__main__":
    main()