def star_with(word):
    """Check if a word starts with a vowel."""
    for ch in 'aeiou':
        if word.startswith(ch):
            return True
    return False


def punctuation_split(word: str) -> tuple:
    """Return a word as a tuple containing the word and the punctuation
    mark."""
    new_text = ''
    punctuation = ''
    for ch in word:
        if ch.isalpha():
            new_text = new_text + ch
        else:
            punctuation = punctuation + ch
    return new_text, punctuation


def to_latin_pig(text: str):
    """Take a string as input, assumed to be an English word. Return the
    translation of this word into Pig Latin. Handle punctuation and
    capitalized words."""
    pig_string = []
    for word in text.split():
        istitle = word.istitle()
        isalpha = word.isalpha()
        if star_with(word):
            if isalpha:
                pig_string.append(word + 'way')
            else:
                word = punctuation_split(word)
                pig_string.append(word[0] + 'way' + word[1])
        else:
            if isalpha:
                pig_string.append(word[1:] + word[0] + 'ay')
            else:
                word = punctuation_split(word)
                pig_string.append(word[0][1:] + word[0][0] + 'ay' + word[1])
        if istitle:
            pig_string[-1] = pig_string[-1].capitalize()
    return ' '.join(pig_string)


if __name__ == '__main__':
    test_text = 'This is  a test   translation!'
    assert to_latin_pig(test_text) == 'Histay isway away esttay ranslationtay!'
