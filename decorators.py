# _*_ coding: utf-8 _*_

PASSWORD='12345'

def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')

    return wrapper


@password_required
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper

@upper
def say_my_name(name):
    return 'hola, {}'.format(name)


def debug(func):
    def wrapper(*args,**kwargs):
        print('La funcion ha sido llamada a pantalla!')
        return func(*args,**kwargs)
    return wrapper


@debug
def add(a,b):
    return a + b


@debug
def neg(n):
    return n*-1

if __name__ == '__main__':
#    print(say_my_name('Ramon')) imprime la llamada a la funcion say_my_name
#    needs_password() llamada a la funcion needs_password
#    print(add(2,3)) llamada a la funcion add
     print(neg(2))
