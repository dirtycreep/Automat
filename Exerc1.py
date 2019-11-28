class Automat:
    change = {}  # Словарь из пар типа (начальное состояние, обрабатываемый символ) : конечное состояние
    begin = None  # Начальное состояние автомата
    end = None  # Множество допустимых конечных состояний автомата, при которых
    # можно сформировать число из уже обработанных символов


def maxString(Auto, s, pos):
    state = Auto.begin  # Автомат входит в начальное состояние
    isEnd = state in Auto.end  # Если начальное состояние входит в множество конечных
    ln = 0
    for i in range(pos, len(s)):  # Обрабатываем все символы строки с позиции pos до конца
        state = Auto.change.get((state, s[i]))  # Автомат переходит из одного состояния
        # в другое в соотвествии с таблицей переходов в Auto.change
        if state in Auto.end:  # Если теперь автомат в одном из конечных состояний, то запоминаем длину
            # сформированного на данном этапе числа (она может увеличитсься),
            # если следующие обрабатываемые символы могут быть частью числа
            isEnd = True
            ln = i - pos + 1
    return (isEnd, ln)  # Возвращаем логическую переменную, отвечающую за то, что автомат нашел число, и его длину


def input_auto(file_name):
    Auto = Automat()  # Создаем автомат
    file = open(file_name, 'r')
    Auto.begin = file.readline().rstrip('\n')  # В первой строчке - начальное состояние
    Auto.end = set(file.readline().rstrip('\n').split())  # Во второй несколько конечных, создаем их множество
    for line in file:
        st_b, char, st_e = line.rstrip('\n').split()  # В остальных переходы
        Auto.change[(st_b, char)] = st_e  # Делаем из них пары и добавляем в словарь переходов
    file.close()
    return Auto  # Возвращаем автомат с параметрами из файла

def get_max_double_digit():
    max_str = ""
    with open('output_automat_lab.txt', mode='r') as inp:
        lines = inp.read().split('\n')
        for i in range(len(lines)):
            if len(lines[i]) > len(max_str):
                max_str = lines[i]
    print('Long value:', max_str)

Auto = input_auto('automat_.txt')
inp = open('input-2.txt', 'r').read()
out = open('output_automat_lab.txt', 'w')

i = 0  # Позиция в строке, с начала которой будем пытаться сформировать число
while i <= len(inp):  # Пока не дошли до конца
    isEnd, ln = maxString(Auto, inp, i)
    if isEnd:  # Если нашли число
        out.write(inp[i:i + ln] + '\n')  # Выводим подстроку, содержащую данное число
        print(inp[i:i + ln])
        i += ln  # Позицию текущую сдвигаем на длину числа
    else:
        i += 1  # Если не нашли, то сдвигаем на один символ


out.close()
get_max_double_digit()
