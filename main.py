import random
from words import random_word


def show_help():
    """Показывает правила игры."""
    print("\nПравила игры:")
    print("Нужно угадать загаданное слово по одной букве.")
    print("За каждую неправильную букву отнимается одна попытка.")
    print("Иногда игра может дать случайную подсказку или дополнительную попытку.\n")


def show_word(word, guessed):
    """Показывает открытые буквы, а неизвестные заменяет подчёркиваниями."""
    displayed_word = ""

    for letter in word:
        if letter.lower() in guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    print("Слово:", displayed_word)


def check_letter(word, letter):
    """Проверяет, есть ли буква в загаданном слове."""
    return letter.lower() in word.lower()


def play_game():
    """Запускает один раунд игры."""
    print("Игра «Виселица»")

    category = input("Выберите категорию (животные, еда, страны): ").strip().lower()
    word = random_word(category)

    if word == "":
        print("Такой категории нет. Будет выбрана категория «животные».")
        word = random_word("животные")

    guessed = ""
    attempts = 6
    extra_attempt_used = False

    print(f"В слове {len(word)} букв.")
    show_word(word, guessed)

    while attempts > 0:
        # Случайное событие: дополнительная попытка (не более одного раза).
        if not extra_attempt_used and random.random() < 0.15:
            attempts += 1
            extra_attempt_used = True
            print("Случайное событие: вы получили дополнительную попытку!")

        # Случайное событие: подсказка — открывается одна буква слова.
        if random.random() < 0.10:
            hint_index = random.choice(range(len(word)))
            hint_letter = word[hint_index].lower()

            if hint_letter not in guessed:
                guessed += hint_letter
                print(f"Подсказка: открыта буква «{hint_letter}».")

        letter = input("\nВведите одну букву: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Введите, пожалуйста, одну букву.")
            continue

        if letter in guessed:
            print("Вы уже называли эту букву.")
            continue

        guessed += letter

        if check_letter(word, letter):
            print("Верно! Такая буква есть.")
        else:
            attempts -= 1
            print("Такой буквы нет.")

        show_word(word, guessed)
        print(f"Осталось попыток: {attempts}")

        # Проверяем, открыты ли все буквы слова.
        all_letters_guessed = True
        for symbol in word:
            if symbol.lower() not in guessed:
                all_letters_guessed = False

        if all_letters_guessed:
            print(f"Поздравляем! Вы угадали слово: {word}")
            return

    print(f"Попытки закончились. Загаданное слово: {word}")


def main():
    # Фиксированное начальное значение для воспроизводимости случайных событий.
    random.seed(42)

    show_help()
    play_game()


if __name__ == "__main__":
    main()





