def five():
    with open('main.txt', 'r') as f:
        data = f.read()

    letters = {}
    for letter in data:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_letters:
        print(letter, count)


def six():
    with open('main.txt', 'r') as f:
        data = f.read()

    words = data.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_count = sorted(
        word_count.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_word_count:
        print(word, count)
