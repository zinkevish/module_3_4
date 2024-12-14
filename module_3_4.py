def singl_root_words(root_words, *other_words):
    same_words = []
    root_words_lower = root_words.lower()
    for i in other_words:
        if root_words_lower in i.lower() or i.lower() in root_words_lower:
            same_words.append(i)
    return same_words


# other_words_ = other_words.upper()
# root_words_ = root_words.upper()

result1 = singl_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = singl_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

