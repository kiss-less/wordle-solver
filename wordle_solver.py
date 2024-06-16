import random, re

data = {}
counter = 1

with open('nouns.txt') as f:
    for line in f:
        if len(line.strip()) == 5:
            data[line.strip().replace("ё", "е")] = True

while True:
    word_in_progress = []
    if data:
        attempt, _ = random.choice(list(data.items()))
    else:
        print("В словаре не осталось подходящих слов!")
        exit(1)

    while True:
        if counter == 1:
            result = input(f'Введите в вордли слово "{attempt}", затем введите сюда результат в формате сжзсж, где с - серая буква, ж - жёлтая буква, з - зелёная буква: ').lower()
        elif counter == 6:
            result = input(f'Последняя попытка! Попробуйте слово "{attempt}": ').lower()
        elif counter > 6:
            print("Не осталось попыток!")
            exit(1)
        else:
            result = input(f'Попытка №{counter}. Теперь попробуйте слово "{attempt}": ').lower()

        if not re.match(r'^[сжз]{5}$', result):
            print("Неверный формат!")
        else:
            break

    if result == "ззззз":
        print(f"Слово {attempt} угадано с {counter} попыток!")
        exit(0)
        
    for i in range(0,5):
        word_in_progress.append(f"{result[i]}{attempt[i]}")
    
    data.pop(attempt)
    counter += 1

    for item in data:    
        for i in range(0,5):
            if (word_in_progress[i][0] == "с" and word_in_progress[i][1] in item and (not f"ж{word_in_progress[i][1]}" in word_in_progress and not f"з{word_in_progress[i][1]}" in word_in_progress)):
                data[item] = False
            if (word_in_progress[i][0] == "з" and word_in_progress[i][1] != item[i]):
                data[item] = False
            if (word_in_progress[i][0] == "ж" and (word_in_progress[i][1] not in item or word_in_progress[i][1] == item[i])):
                data[item] = False
    data = {key: value for key, value in data.items() if value != False}
