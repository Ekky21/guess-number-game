import time
seed = int(time.time()*1000)

def attempts_word(n: int) -> str:
    n = abs(n)
    if 11 <= (n % 100) <= 14:
        return "попыток"
    last = n % 10
    if last == 1:
        return "попытка"
    elif 2 <= last <= 4:
        return "попытки"
    else:
        return "попыток"


def random_from_time_LCG (a, b):
    global seed
    #LCG (Линейный конгруэнтный метод)
    seed  = (seed * 1664525 + 1013904223) % (2**32)
    return a + seed % ( b - a + 1 )

rand = random_from_time_LCG (1, 100)
attempts = 0
total_attempts = 0
print("Угадай целое число от 1 до 100. Для отмены игры напиши '0'")

while True:
    try:
        number = int(input("Введи своё число: "))
    except ValueError:
        print("Пожалуйста, вводите только числа!")
        continue

    if number == 0:
        print("Возвращайтесь снова!")
        break

    total_attempts += 1

    if number == rand:
        print ("Вы угадали! Ваше число совпадает с тем числом, что загадал я!")
        print (f'Вам потребовалось {total_attempts} {attempts_word(total_attempts)}')
        break

    else:
        print("Неверно! Попробуй ещё")
        attempts += 1

    if attempts % 3 == 0:
        print("Вы хотите получить подсказку?")
        tip = input().strip().lower()
        if tip == "да":
            delta = random_from_time_LCG (5, 15)
            low = max(1, rand - delta)
            high = min(100, rand + delta)
            print(f'Ваше число находится между {low} и {high}')
            attempts = 0


