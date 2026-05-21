def word_frequency(text):
    word_freq = {}
    words = text.split()

    for word in words:
        if len(word)>0:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq