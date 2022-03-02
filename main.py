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


alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])


while True:
    # получение текущего времени с компьютера
    now = datetime.now()

    # получение установленного времени будильника
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second


    # Срабатывание будильника
    if (alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec):
        print("Подъем!")
        playsound('D:/Downloads/14990_flying-alarm.mp3')
        break
