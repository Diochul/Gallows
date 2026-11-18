from words import long_words, add_guessed, describe, words_upper


def test_long_words():
    words = ["тигр", "банан", "помидор", "слон"]
    assert long_words(words) == ["помидор"]


def test_add_guessed():
    guessed = set()
    result = add_guessed(guessed, "А")
    assert result == {"а"}
    assert "а" in guessed


def test_describe():
    result = describe("тигр")
    assert "тигр" in result
    assert "4" in result
    assert "6" in result


def test_words_upper():
    words = ["тигр", "слон", "кошка"]
    assert words_upper(words) == ["ТИГР", "СЛОН", "КОШКА"]
