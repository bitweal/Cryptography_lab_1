from test import miller_rabin, factorize
from Pollard import pollard
from Brillhart_Morrison import start

def task_1(n):
    k = int(input('Enter k: '))
    if miller_rabin(n,k):
        return n+n
    else:
        return task_2(n)

def task_2(n):
    a = factorize(n)
    if len(a) > 0:
        return task_1(n//a[0])
    else:
        return task_3(n)

def task_3(n):
    a = pollard(n)
    if a != n:
        return task_4(n//a)
    else:
        return task_5(n)

def task_4(n):
    if task_1(n):
        return n+n
    else:
        return n

def task_5(n):
    a = start(n, a = 0.7)
    if a == -1:
        return 'я не можу знайти канонiчний розклад числа :(.'
    else:
        return task_4(n//a[0])

n = int(input('Enter n: '))
print(task_1(n))