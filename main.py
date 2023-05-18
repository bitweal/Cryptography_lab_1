from test import miller_rabin, factorize
from Pollard import pollard
from Brillhart_Morrison import brillhart_morrison

factorize_numbers = []

def task_1(n):
    print('Тест на простоту Мiллера-Рабiна')
    k = int(input('Enter k: '))
    if miller_rabin(n,k):
        print(f'Число {n} є простим')
        factorize_numbers.append(n)
    else:
        print('Число є складеним переходимо до наступного кроку')
        return task_2(n)

def task_2(n):
    print('метод пробних дiлень')
    a = factorize(n)
    if len(a) > 0:
        factorize_numbers.append(a[0])
        print('дiльник a знайдено, повертаємось до попереднього кроку з числом ', n//a[0])
        return task_1(n//a[0])
    else:
        print('дiльник не знайдено, переходимо до наступного кроку')
        return task_3(n)

def task_3(n):
    print('ρ-метод Полларда ')
    a = pollard(n)
    if a != n:
        factorize_numbers.append(a)
        print('дiльник a знайдено, переходимо до наступного кроку з числом ', n//a)
        return task_4(n//a)
    else:
        return task_5(n)

def task_4(n):
    print('Тест на простоту Мiллера-Рабiна')
    k = int(input('Enter k: '))
    if miller_rabin(n,k):
        print(f'Число {n} є простим')
        factorize_numbers.append(n)
    else:
        print('Число є складеним переходимо до наступного кроку')
        return task_5(n)

def task_5(n):
    print('метод Брiлхарта-Моррiсона')
    a = brillhart_morrison(n)
    if a == -1:
        return 'я не можу знайти канонiчний розклад числа :(.'
    else:
        factorize_numbers.append(a[0])
        return task_4(n//a[0])

n = int(input('Enter n: '))
task_1(n)
print('Канонiчний розклад числа: ', factorize_numbers)