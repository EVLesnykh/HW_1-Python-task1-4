def main_menu():
    print('''Основное меню:
    1 - Найти контакт  
    2 - Добавить новый контакт 
    3 - Изменить данные о контакте
    4 - Удалить контакт 
    5 - Вывести все контакты  
    6 - Выйти из меню ''')

def search_contact():
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        search = (input('Введите любой параметр для поиска в phonebook: ' ).title())
        for line in data:
            if search in line:
                print(line)

def add_contact():
    with open('phonebook.txt', 'a', encoding = 'utf-8') as data:
        surname = (input('Введите Фамилию: ' ).title())
        name = (input('Введите Имя: ' ).title())
        middle_name = (input('Введите Отчество: ' ).title())
        telephone = (input('Введите телефон: ' ).title())
        new_line = surname +' '+ name +' '+ middle_name +' '+ telephone
        data.writelines(f'\n{new_line}')
        print(new_line)

def edit_contact():
   with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        search_edit = (input('Введите id контакта: ' ).title())
        with open ('phonebook.txt', 'w', encoding = 'utf-8') as data:
            for line in search_edit:
                if search_edit in line:
                    print(line)
                    surname = (input('Введите Фамилию: ' ).title())
                    name = (input('Введите Имя: ' ).title())
                    middle_name = (input('Введите Отчество: ' ).title())
                    telephone = (input('Введите телефон: ' ).title())
                    edit_line = surname +' '+ name +' '+ middle_name +' '+ telephone + '\n'
                    line = line.replace(line, edit_line)
                data.writelines(line)
           
def delete_contact():
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        D = input('Введите Фамилию или Имя для удаления: ')
        lines = data.readlines()
        with open('phonebook.txt', 'w', encoding = 'utf-8') as data:
            for line in lines:
                if D in line:
                    print("Контакт удален")
                else:
                    print(line)
                    data.write(line)

def show_all_contacts():
    with open('phonebook.txt', 'r', encoding = 'utf-8') as data:
        print()
        for line in data:
            print(line)  

def choose(choice):
   if choice == 6:
      print('До скорых встреч!')
   elif choice == 1:
    search_contact()
    main_menu()
    choose(int(input('Введите номер команды из меню: ')))
   elif choice == 2:
    add_contact()
    main_menu()
    choose(int(input('Введите номер команды из меню: ')))
   elif choice == 3:
    edit_contact()
    main_menu()
    choose(int(input('Введите номер команды из меню: ')))
   elif choice == 4:
    delete_contact()
    main_menu()
    choose(int(input('Введите номер команды из меню: ')))
   elif choice == 5:
    show_all_contacts()
    main_menu()
    choose(int(input('Введите номер команды из меню: ')))
   else:
      print('Ошибка. Проверьте правильность ввода')

main_menu()
choose(int(input('Введите номер команды из меню: ')))