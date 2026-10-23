
print("Привет! Добро пожаловать в игру «Виселица».")
print("Цель: угадать загаданное слово по буквам, пока не закончились попытки.")
print("Команды: guess <буква>, status, exit\n")

# Загаданное слово и основные переменные
word = "lerko"
guessed_bykva = ""
errors = 0
max_errors = 6

# Главный игровой цикл
while True: 
    # 1. Сборка текущего отображения слова (если буква угадана — показываем её, иначе '_')
    display_word = ""
    for bykva in word:
        if bykva in guessed_bykva:
            display_word = display_word + bykva + " "
        else:
            display_word = display_word + "_ "

    print("\nСлово:", display_word)
    print("Ошибки:", errors, "из", max_errors)

    # 2. Получение и нормализация ввода от пользователя
    command = input("Введите команду: ").strip().lower()

    # 3. Обработка команды exit (выход)
    if command == "exit":
        print("Выход из игры. До свидания!")
        break

    # 4. Обработка команды status (текущее состояние)
    elif command == "status":
        print()
        print("--- Статус игры ---")
        print("Слово:", display_word)
        print("Количество ошибок:", errors)
        print("Уже введенные буквы:", guessed_bykva)
        print("-------------------")
        continue

    # 5. Обработка команды guess <буква>
    elif command.startswith("guess "):
        # Получаем всё, что идет после слова "guess "
        bukva1 = command[6:].strip()

        # Проверяем, что пользователь ввел ровно одну букву
        if len(bukva1) != 1:
            print("Ошибка: нужно ввести ровно одну букву после команды guess!")
            continue

        # Проверяем, не вводил ли игрок эту букву раньше
        if bukva1  in guessed_bykva:
            print("Вы уже угадывали эту букву раньше. Попробуйте другую.")
            continue

        # Добавляем букву в строку угаданных букв
        guessed_bykva += bukva1 

        # Проверяем, есть ли такая буква в загаданном слове
        if bukva1  in word:
            print("Отлично! Такая буква есть в слове.")
        else:
            print("Такой буквы нет в слове! Ошибка увеличивается.")
            errors = errors + 1

        # Проверка на проигрыш (если ошибок стало 6 или больше)
        if errors >= max_errors:
            print("\nК сожалению, вы проиграли! Превышен лимит ошибок.")
            print("Загаданное слово было:", word)
            break

        # Проверка на победу (если в отображении больше нет подчеркиваний '_')
        # Проверяем каждую букву слова: все ли они есть в guessed_letters
        won = True
        for l in word:
            if l not in guessed_bykva:
                won = False
                break

        if won:
            print("\nПоздравляем! Вы полностью угадали слово:", word)
            break

    # Если команда не распознана
    else:
        print("Неизвестная команда. Попробуйте еще раз или используйте 'status'.")
        continue




