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