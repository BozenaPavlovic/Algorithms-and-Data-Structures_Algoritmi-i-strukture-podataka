def custom_word_frequency(text):
    word_freq = CustomDict()
    words = text.split()

    for word in words:
        if len(word)>0:
            if word_freq.contains(word):
                word_freq.set(word, word_freq.get(word) + 1)
            else:
                word_freq.set(word, 1)

    return word_freq