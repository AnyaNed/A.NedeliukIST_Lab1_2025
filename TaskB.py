import random

def guess_word_game():
    words = ["ананас", "музика", "вазон", "кава", "чай", "борщ", "вареник", "мишка", "чашка", "сметана"]
    secret_word = random.choice(words)
    guessed_word = ["_"] * len(secret_word)
    attempts = 7
    guessed_letters = set()

    print("Загадане слово:", " ".join(guessed_word))
    print(f"У вас є {attempts} спроб.")

    while attempts > 0 and "_" in guessed_word:
        letter = input("Введіть літеру: ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Будь ласка, введіть одну літеру.")
            continue

        if letter in guessed_letters:
            print("Ви вже вводили цю літеру.")
            continue

        guessed_letters.add(letter)

        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    guessed_word[i] = letter
            print("Загадане слово:", " ".join(guessed_word))
        else:
            attempts -= 1
            print(f"Немає такої літери. Залишилось спроб: {attempts}")
            print("Загадане слово:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print(f'Вітаємо! Ви вгадали слово "{secret_word}"!')
    else:
        print(f'На жаль, ви програли. Загадане слово було: "{secret_word}".')

guess_word_game()