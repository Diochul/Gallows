import random

# Списки слов по категориям.
WORDS_BY_CATEGORY = {
    "животные": ["тигр", "слон", "кошка", "заяц", "волк"],
    "еда": ["пицца", "каша", "банан", "сыр", "яблоко"],
    "страны": ["польша", "италия", "канада", "япония", "бразилия"],
}

# Словарь: слово -> количество попыток.
difficulty = {
    "тигр": 6, "слон": 6, "кошка": 6, "заяц": 6, "волк": 6,
    "пицца": 6, "каша": 6, "банан": 6, "сыр": 6, "яблоко": 6,
    "польша": 6, "италия": 6, "канада": 6, "япония": 6, "бразилия": 6,
}


def random_word(category="животные"):
    """Возвращает случайное слово из выбранной категории."""
    if category not in WORDS_BY_CATEGORY:
        return ""
    return random.choice(WORDS_BY_CATEGORY[category])


def long_words(words):
    """Возвращает слова длиной больше пяти букв."""
    return [word for word in words if len(word) > 5]


def add_guessed(guessed, ch):
    """Добавляет букву в множество угаданных букв."""
    guessed.add(ch.lower())
    return guessed


def describe(word):
    """Возвращает описание слова, его длину и сложность."""
    return f"Слово: {word}, букв: {len(word)}, сложность: {difficulty.get(word.lower(), 6)}"


def words_upper(words):
    """Возвращает новый список слов в верхнем регистре."""
    return [word.upper() for word in words]
