i=1 #счетчик
sum=0 #итоговая сумма

#считаем числа с четным количеством цифр, максимальное - 999 999
while i <= 999:

    #собираем число - палиндром в 10 системе
    s = str(i)+str(i)[::-1]

    #проверяем что в двоичной системе оно тоже палиндром, если да, то суммируем
    if str(bin(int(s))[2:]) == str(bin(int(s))[2:])[::-1]:
        sum +=int(s)


    i+=1 #прибавляем счетчик



#работа с трехзначными числами

s = 0 #нужное число
a = 1 #первая и последняя цифры
b = 0 #вторая цифра

#максимальное число - 999
while int(s) != 999:

    #собираем строку из данных цифр
    s = str(a) + str(b) + str(a)

    # проверяем что в двоичной системе оно тоже палиндром, если да, то суммируем
    if str(bin(int(s))[2:]) == str(bin(int(s))[2:])[::-1]:
        sum +=int(s)

    #если цифра посередине равна 9, то обнуляем ее и прибавляем к крайним единицу
    if b==9:
        a+=1
        b=0

    #иначе прибавляем 1 к цифре посередине
    else:
        b+=1



#работа с пятизначными цифрами
#итоговое число и отдельно его цифры
s = 0
a = 1
b = 0
c = 0

#максимальное - 99999
while int(s) < 99999:

    # собираем строку из данных цифр
    s = str(a) + str(b) + str(c) + str(b) + str(a)

    # проверяем что в двоичной системе оно тоже палиндром, если да, то суммируем
    if str(bin(int(s))[2:]) == str(bin(int(s))[2:])[::-1]:
        sum +=int(s)

    #все палиндромы по очереди
    if b==9 and c==9:
        a+=1
        b=0
        c=0
    else:
         if c==9:
            c=0
            b+=1

         else:
            c+=1

#вывод ответа
print (sum)

