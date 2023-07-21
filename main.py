import json

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

def add_password(passwords, website, username, password):
    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords)
    print(f"Пароль для {website} успешно добавлен!")

def get_password(passwords, website):
    if website in passwords:
        return passwords[website]["password"]
    else:
        return None

def list_websites(passwords):
    print("Список сохраненных сайтов:")
    for website in passwords:
        print(f"- {website}")

def main():
    print("Добро пожаловать в менеджер паролей!")
    passwords = load_passwords()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить пароль")
        print("2. Получить пароль")
        print("3. Показать список сайтов")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            website = input("Введите название веб-сайта: ")
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            add_password(passwords, website, username, password)
        elif choice == "2":
            website = input("Введите название веб-сайта: ")
            password = get_password(passwords, website)
            if password:
                print(f"Пароль для {website}: {password}")
            else:
                print("Пароль не найден.")
        elif choice == "3":
            list_websites(passwords)
        elif choice == "4":
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
