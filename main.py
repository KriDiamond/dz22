def make_user_text_usable(inputed_text):
    to_remove = '.,!?;:-()'
    result = ''
    for letter in inputed_text:
        if letter not in to_remove:
            result += letter.lower()
    return result


def count_of_words (inputed_text):
    list_of_words = inputed_text.split()
    return len(list_of_words)


def the_longest_word (inputed_text):
    list_of_words = inputed_text.split()
    longest_word = ""
    max_lenth = 0
    for i in list_of_words:
        current_word = i
        if len(current_word) > max_lenth:
            max_lenth = len(current_word)
            longest_word = current_word
    return longest_word


def counf_of_vowels(inputed_text):
    list_of_vowels = 'ёeyuoaуеыаоэяию'
    result = ''
    for letter in inputed_text:
        if letter in list_of_vowels:
            result += letter
    return len(result)


def count_of_inter(inputed_text):
    list_of_words = inputed_text.split()
    list_of_unique_words = []
    result = ""
    for word in list_of_words:
        if word not in list_of_unique_words:
            list_of_unique_words.append(word)
    for word in list_of_unique_words:
        result += word + " - x" + str(inputed_text.count(word)) + ", "
    result = result[:-2]
    return result


user_text = input("Введите текст: ")
user_text += " "

usable_text = make_user_text_usable(user_text)

print(f"""В введенном вами тексте: 
1. Количество слов: {count_of_words(usable_text)}.
2. Самое длинное слово: {the_longest_word(usable_text)}.
3. Количество гласных: {counf_of_vowels(usable_text)}.
4. Количество уникальных слов: {count_of_inter(usable_text)}.""")
