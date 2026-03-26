class User:

    def __init__(self, login, email, access_level=1):
        self.login = login
        self.email = email
        self.access_level = access_level

    def get_info(self):
        return f"Логин: {self.login}, Email: {self.email}, Уровень доступа: {self.access_level}"

    def __del__(self):
        print(f"Пользователь {self.login} {self.email} удален")


users = [
            User("Ваня" , "ivan@mail.com"   , 3),
            User("Маша" , "maria@gmail.com" , 1),
            User("Петя" , "petr@vk.com"     , 2)
        ]

for u in users:
    print(u.get_info())

users.remove(min(users, key=lambda u: u.access_level))

input()