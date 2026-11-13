import random


def random_word(category="животные"):

    if category == "животные":
        word_count = 5
    elif category == "еда":
        word_count = 5
    elif category == "страны":
        word_count = 5
    else:
        return ""

    word_index = random.choice(range(word_count))

    if category == "животные":
        if word_index == 0:
            return "тигр"
        elif word_index == 1:
            return "слон"
        elif word_index == 2:
            return "кошка"
        elif word_index == 3:
            return "заяц"
        else:
            return "волк"

    elif category == "еда":
        if word_index == 0:
            return "пицца"
        elif word_index == 1:
            return "каша"
        elif word_index == 2:
            return "банан"
        elif word_index == 3:
            return "сыр"
        else:
            return "яблоко"

    elif category == "страны":
        if word_index == 0:
            return "польша"
        elif word_index == 1:
            return "италия"
        elif word_index == 2:
            return "канада"
        elif word_index == 3:
            return "япония"
        else:
            return "бразилия"
