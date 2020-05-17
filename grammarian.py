import enchant
import string

d = enchant.Dict("en_US")
ALPHABET = string.ascii_lowercase

def grammarize_phrase_substitute(phrase):
    grammarized_phrases = []
    for i in range(len(phrase)):
        for letter in ALPHABET:
            grammarized_phrase = phrase[:i] + letter + phrase[i + 1:]
            if grammarized_phrase != phrase and all(map(lambda w: d.check(w), grammarized_phrase.split())):
                grammarized_phrases.append(grammarized_phrase)

    return grammarized_phrases

def grammarize_phrase_delete(phrase):
    grammarized_phrases = []
    for i in range(len(phrase)):
        grammarized_phrase = phrase[:i] + phrase[i + 1:]
        if grammarized_phrase != phrase and all(map(lambda w: d.check(w), grammarized_phrase.split())):
            grammarized_phrases.append(grammarized_phrase)

    return grammarized_phrases

def grammarize_phrase_shift(phrase):
    grammarized_phrases = []
    for i in range(len(phrase)):
        deleted_phrase = phrase[:i] + phrase[i + 1:]
        for j in range(len(deleted_phrase) + 1):
            grammarized_phrase = deleted_phrase[:j] + phrase[i] + deleted_phrase[j:]
            if grammarized_phrase != phrase and all(map(lambda w: d.check(w), grammarized_phrase.split())):
                grammarized_phrases.append(grammarized_phrase)

    return grammarized_phrases


def grammarize_phrase(phrase):
    return grammarize_phrase_substitute(phrase) + grammarize_phrase_delete(phrase) + grammarize_phrase_shift(phrase)
