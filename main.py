from datetime import *
from playsound import *

# Проверка корректности ввода пользователем времени для будильника
def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Неверный формат, попробуйте снова"
    else:
        if int(alarm_time[0:2]) > 23:
            return "Неверный формат часов, попробуйте снова"
        elif int(alarm_time[3:5]) > 59:
            return "Неверный формат минут, попробуйте снова"
        elif int(alarm_time[6:8]) > 59:
            return "Неверный формат секунд, попробуйте снова"
        else:
            return "ok"

# зациклевание ввода до момента, когда будет введены значения верные проверки def validate_time()
while True:
    alarm_time = input("Введите время будильника в следующем формате 'HH:MM:SS' \n Время будильника: ")
    validate = validate_time(alarm_time)
    if validate != "ok":
        print(validate)
    else:
        print(f"Будильник установлен на время {alarm_time}...")
        break




