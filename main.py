def make_user_text_usable(inputed_text):
    to_remove = """.,!?;:-()@"'*+-/={}[]|"""
    result = ''
    for letter in inputed_text:
        if letter not in to_remove:
            result += letter.lower()
        else:
            result += ' '
    return result


def make_list_of_usable_text(inputed_text):
    list_of_words = inputed_text.split()
    return list_of_words


def the_longest_word (inputed_list):
    longest_word = ""
    for current_word in inputed_list:
        if len(current_word) > len(longest_word):
            longest_word = current_word
    return longest_word


def counf_of_vowels(inputed_text):
    list_of_vowels = 'ёeyuoaуеыаоэяию'
    counter = 0
    for letter in inputed_text:
        if letter in list_of_vowels:
            counter += 1
    return counter


def count_of_inter(inputed_list):
    list_of_unique_words = []
    result = ""
    for word in inputed_list:
        if word not in list_of_unique_words:
            list_of_unique_words.append(word)
    return list_of_unique_words


def nice_word_counter_output(inputed_text, unique_list):
    result = ''
    for word in unique_list:
        result += word + " (x" + str(inputed_text.count(word)) + "), "
    result = result[:-2]
    return result


user_text = input("Введите текст: ")
user_text += " "

usable_text = make_user_text_usable(user_text)
usable_list = make_list_of_usable_text(usable_text)

print(f"""В введенном вами тексте: 
1. Количество слов: {len(usable_list)}.
2. Самое длинное слово: {the_longest_word(usable_list)}.
3. Количество гласных: {counf_of_vowels(usable_text)}.
4. Количество уникальных слов: {nice_word_counter_output(usable_text, count_of_inter(usable_list))}.""")
