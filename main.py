def make_user_text_usable(inputed_text):
    usable_text = inputed_text.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ").replace(":", " ").replace(";", " ").replace("-", " ").replace("\(", " ").replace("\)", " ").replace("\"", " ").replace("\'", " ").lower()
    return usable_text


def count_of_words (inputed_text):
    count_of_words = 0
    for i in range(len(inputed_text) - 1):
        if inputed_text[i] != " " and inputed_text[i + 1] == " ":
            count_of_words += 1
    return count_of_words


def the_longest_word (inputed_text):
    list_of_words = inputed_text.split()
    longest_word = ""
    max_lenth = 0
    for i in list_of_words:
        current_word = i
        current_lenth = len(current_word)
        if current_lenth > max_lenth:
            max_lenth = current_lenth
            longest_word = current_word
    return longest_word


def counf_of_vowels(inputed_text):
    vowels_count = 0
    for i in inputed_text:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y" or i == "а" or i == "о" or i == "у" or i == "е" or i == "и" or i == "ы" or i == "э" or i == "я" or i == "ю":
            vowels_count +=1
    return vowels_count


def count_of_inter(inputed_text):
    list_of_words = inputed_text.split()
    list_of_unique_words = []
    list_of_unique_nums = []
    result = ""
    for word in list_of_words:
        if word not in list_of_unique_words:
            list_of_unique_words.append(word)
            list_of_unique_nums.append(1)
        else:
            list_of_unique_nums[list_of_unique_words.index(word)] += 1
    for word in list_of_unique_words:
        result += word + " - x" + str(list_of_unique_nums[list_of_unique_words.index(word)]) + ", "
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
