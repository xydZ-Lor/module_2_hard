def gen_key(stone):
    key = ''
    for a in list_stone: # Перебираем все пары уникальных элементов list_stone
        for b in list_stone[list_stone.index(a) + 1:]: # Перебираем элементы после a
            c = a + b
            if stone % c == 0: # Проверяем можно ли делить stone на с
                key += f'{a}{b}'
    return key

list_stone = list(range(1, 21))
stone = int(input('Введите значение ребуса от 3 до 20: '))
if 3 <= stone <= 20:
    result = gen_key(stone)
    print(result)
else:
    print('Введите значение в диапазоне от 3 до 20')