with open('en-ru.txt', 'r', encoding="utf-8") as file:
    en = {}
    for line in file:
        en_word, ru_tr = line.split(' - ')
        ru_words = ru_tr.replace("\n", "").split(", ")
        for ru_word in ru_words:
            if ru_word not in en:
                en[ru_word] = [en_word]
            else:
                en[ru_word].append(en_word)


with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for ru_word in sorted(en.keys()):
        en_words = ', '.join(en[ru_word])
        file.write(f"{ru_word} – {en_words}\n")
