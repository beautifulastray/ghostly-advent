from PIL import Image
import re

#1000 строк длиной в 1000 символов - это сетка с огоньками
d1 = []

for y in range(1000):
    d2 = []
    for x in range(1000):
        d2.append(0)      
    d1.append(d2)

#Три функции для состояний:
#Функция включения:
def turn_on(start_x, stop_x, start_y, stop_y):
    for y in range(start_y, stop_y + 1):
        for x in range(start_x, stop_x + 1):
            d1[y][x] = 1

#Функция выключения:
def turn_off(start_x, stop_x, start_y, stop_y):
    for y in range(start_y, stop_y + 1):
        for x in range(start_x, stop_x + 1):
            d1[y][x] = 0

#Функция переключения:
def toggle(start_x, stop_x, start_y, stop_y):
    for y in range(start_y, stop_y + 1):
        for x in range(start_x, stop_x + 1):
            #Узнать какое значение у переменной и поменять на противоположное
            if d1[y][x] == 0:
                d1[y][x] = 1
            else:
                d1[y][x] = 0

def main():
    with open('input.txt') as file:
        for line in file:
            result = re.search(r'(^.+?) (\d+),(\d+) through (\d+),(\d+)', line)
            start_x = int(result.group(3))
            start_y = int(result.group(2))
            stop_x = int(result.group(5))
            stop_y = int(result.group(4))
            to_do = result.group(1)
            
            #Применить одну из функций переключения
            if to_do == 'turn on':
                turn_on(start_x, stop_x, start_y, stop_y)
            if to_do == 'turn off':
                turn_off(start_x, stop_x, start_y, stop_y)
            if to_do == 'toggle':
                toggle(start_x, stop_x, start_y, stop_y)

    #Считает горящие огоньки на сетке
    count = 0

    for row in d1:
        for element in row:
            if element == 1:
                count += 1
    print(count)

    #Cоздает картинку и "зажигает" лампочки: горящие ламочки - желтым, не горящие оставляет темно-синими
    img = Image.new('RGB', (1000, 1000), (0, 51, 104))

    for id, item in enumerate(d1):
        y = id
        for id, item2 in enumerate(item):
            x = id
            if item2 == 1:
                img.putpixel((y, x), (255, 223, 0))
    img.show()

if __name__ == "__main__":
    main()
