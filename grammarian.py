import enchant
import string

d = enchant.Dict("en_US")
ALPHABET = string.ascii_lowercase

# list of phrases
# break into individual words
# Iterate each letter A to Z
# check if resultant word is english
# if true and not original - store

def grammarize_word(word):
    words = []
    for i in range(len(word)):
        for letter in ALPHABET:
            grammarized_word = word[:i] + letter + word[i + 1:]
            if d.check(grammarized_word) and grammarized_word != word:
                words.append(grammarized_word)
    return words

def grammarize_phrase(phrase):
    phrase_words = phrase.split()
    grammarized_phrases = []
    for i in range(len(phrase_words)):
        target_word = phrase_words[i]
        grammarized_word = grammarize_word(target_word)
        for j in range(len(grammarized_word)):
            grammarized_phrase = phrase.split()
            grammarized_phrase[i] = grammarized_word[j]
            space = " "
            grammarized_phrase = space.join(grammarized_phrase)
            grammarized_phrases.append(grammarized_phrase)
    return grammarized_phrases


print(grammarize_phrase("beacon of hope"))