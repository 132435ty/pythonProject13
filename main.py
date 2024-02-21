def find_word(text, separator):
    words = text.split(separator)
    for word in words:
        if "кот" in word:
            return word

text = " кот съел колбасу"
separator = " "
print(find_word(text, separator))

