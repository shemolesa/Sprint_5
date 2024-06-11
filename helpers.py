import random

# генерация логина пользователя
def generated_login():
    generated_login = 'NameFamili9'+str(random.randint(100,999))+'@yandex.ru'
    return generated_login