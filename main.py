from test import miller_rabin, factorize
from Pollard import pollard
from Brillhart_Morrison import start

def task_1(n):
    print('Тест на простоту Мiллера-Рабiна')
    k = int(input('Enter k: '))
    if miller_rabin(n,k):
        print('Число є простим', n)
        return n+n
    else:
        print('Число є складеним переходимо до наступного кроку')
        return task_2(n)

def task_2(n):
    print('метод пробних дiлень')
    a = factorize(n)
    if len(a) > 0:
        print('дiльник a знайдено, повертаэмось до попереднього кроку з числом', n//a[0])
        return task_1(n//a[0])
    else:
        print('дiльник не знайдено, переходимо до наступного кроку')
        return task_3(n)

def task_3(n):
    print('ρ-метод Полларда')
    a = pollard(n)
    if a != n:
        print('дiльник a знайдено, переходимо до наступного кроку', n//a[0])
        return task_4(n//a)
    else:
        return task_5(n)

def task_4(n):
    print('Тест на простоту Мiллера-Рабiна')
    k = int(input('Enter k: '))
    if miller_rabin(n,k):
        print('Число є простим', n)
        return n+n
    else:
        print('Число є складеним переходимо до наступного кроку')
        return task_5(n)

def task_5(n):
    print('метод Брiлхарта-Моррiсона')
    a = start(n)
    if a == -1:
        return 'я не можу знайти канонiчний розклад числа :(.'
    else:
        return task_4(n//a[0])

n = int(input('Enter n: '))
print(task_1(n))