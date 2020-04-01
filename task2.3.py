"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
# list solution
#мне кажется, должно быть посимпатичнее решение, но не нашла возвращение названия списка,
#т.е. если создавать список year с вложенными списками - yeartime, то при проверке month in yeartime,
#выводит содержимое каждого списка yeartime, а не его название: [12, 1, 2] вместо "зима"

try:
    month = int(input("введите номер месяца: "))
    winter = [12, 1, 2]
    summer = [6, 7, 8]
    spring = [3, 4, 5]
    autumn = [9, 10, 11]
    if month in winter:
        print('месяц относится к зиме')
    elif month in summer:
        print('месяц относится к лету')
    elif month in spring:
        print('месяц относится к весне')
    elif month in autumn:
        print('месяц относится к осени')
    else:
        print('вы ввели неверный номер месяца нужно число от 1 до 12')
except ValueError:
    print('вы ввели неверный номер месяца, нужно число от 1 до 12')

#dict solution
# try:
#     range(12)
#     month = int(input("введите номер месяца: "))
#     winter = [12, 1, 2]
#     summer = [6, 7, 8]
#     spring = [3, 4, 5]
#     autumn = [9, 10, 11]
#     year = {'лету': summer,
#             'осени': autumn,
#             'зиме': winter,
#             'весне': spring,
#             }
#     if month in range(1,13):
#         for yeartime in year.keys():
#             if month in year[yeartime]:
#                 print(f'месяц относится к {yeartime}')
#     else: print('вы ввели неверный номер месяца, нужно число от 1 до 12')
# except ValueError:
#     print('вы ввели неверный номер месяца, нужно число от 1 до 12')