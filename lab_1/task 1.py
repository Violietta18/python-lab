# Робота з текстом.
# Напишіть функцію, яка приймає рядок як вхідні дані та повертає словник,
# де ключі — це унікальні слова, а значення — кількість їх появ.
# Виведіть список слів, які зустрічаються більше 3 разів.

def analyze_text(text):
    text = text.lower()
    words = text.split()

    word_counter = {}

    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    repeated_words = []
    for word, count in word_counter.items():
        if count > 3:
            repeated_words.append(word)

    print("Унікальні слова та кількість появ:")
    print(word_counter)
    print("\nСлова, що зустрічаються більше 3 разів:")
    print(repeated_words)

text_input = "apple banana apple orange banana apple grape banana apple orange grape banana apple grape grape"

analyze_text(text_input)
