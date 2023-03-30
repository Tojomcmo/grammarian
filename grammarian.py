import enchant
import string
from functools import reduce

d = enchant.Dict("en_US")
ALPHABET = string.ascii_lowercase

# ASSUMPTIONS:
#   The grammarian orb allows for the user to "change one letter" in the spell name
#   Changing is assumed to take three forms:
#       - altering the value
#       - moving the location
#       - removing
#   Adding a new letter is changing the phrase, but not changing an existing letter, and is therefore out of scope
#   from a strict reading of the action. This is an opinion. Fight me.
#   Spaces and word count are also assumed constant, though this is less fight-worthy, could be swayed to include.

#   The function grammarize_phrase receives a phrase (letters and spaces only) and returns a list of altered phrases,
#   where each returned phrase complies with one of the above forms, and each word in the phrase complies with the
#   PyEnchant english dictionary.

# FUNCTION LIST:
#   grammarize_word_substitute - returns a list of words from substituting one letter of the input word with
# another letter from the alphabet
#   grammarize_word_delete - returns a list of words from deleting one letter from the input word
#   grammarize_phrase_shift - returns a list of phrases from shifting one letter across the input phrase
#   grammarize_phrase_substitute - returns a list of phrases using the word substitute function to an input phrase
#   grammarize_phrase_deletion - returns a list of phrases using the word delete function to an input phrase
#   grammarize_phrase - employs all three phrase functions to deliver the conglomerated set of grammarized phrases
# created from the input phrase


def grammarize_word_substitute(word):
    words = []
    # this for loop targets each indexed letter of the input word
    for i in range(len(word)):
        # this for loop substitutes the target letter the alphabet
        for letter in ALPHABET:
            grammarized_word = word[:i] + letter + word[i + 1:]
            # this if statement checks the new word against the dictionary and the input word
            if d.check(grammarized_word) and grammarized_word != word:
                words.append(grammarized_word)
    return words


def grammarize_word_delete(word):
    words = []
    # this for loop targets each indexed letter of the input word and deletes the letter
    for i in range(len(word)):
        grammarized_word = word[:i] + word[i + 1:]
        # this if statement checks the new word against the dictionary and the input word
        if d.check(grammarized_word) and grammarized_word != word:
            words.append(grammarized_word)
    return words

def grammarize_phrase_shift(phrase):
    grammarized_phrases_shift_set = []
    # this for loop selects the letter to shift and creates the phrase with the target letter removed
    for i in range(len(phrase)):
        target_letter = phrase[i]
        target_phrase = phrase[:i] + phrase[i + 1:]
        # This if statement rejects a shift of spaces
        if target_letter != " ":
            # this for loop shifts the target letter through the altered phrase
            for j in range(len(target_phrase)+1):
                grammarized_phrase =target_phrase[:j] + target_letter + target_phrase[j:]
                phrase_words = grammarized_phrase.split()
                counter = 0
                # this for loop checks whether all individual words in the target configuration are in the dictionary
                for k in range(len(phrase_words)):
                    if d.check(phrase_words[k]):
                        counter += 1
                # if each word is in the dictionary, then the phrase is viable
                if counter is len(phrase_words) and grammarized_phrase != phrase:
                    grammarized_phrases_shift_set.append(grammarized_phrase)
    return grammarized_phrases_shift_set

def grammarize_phrase_substitute(phrase):
    # the split operation separates the phrase into a list of individual words
    phrase_words = phrase.split()
    grammarized_phrases_substitute_set = []
    # this for loop iterates the word targeted by the grammarize word substitute function
    for i in range(len(phrase_words)):
        target_word = phrase_words[i]
        grammarized_word = grammarize_word_substitute(target_word)
        # this for loop incorporates list of successes for the targeted word adds them to the phrase
        for j in range(len(grammarized_word)):
            target_grammarized_phrase = phrase.split()
            target_grammarized_phrase[i] = grammarized_word[j]
            space = " "
            target_grammarized_phrase = space.join(target_grammarized_phrase)
            # option added to list of successes
            grammarized_phrases_substitute_set.append(target_grammarized_phrase)
    return grammarized_phrases_substitute_set


def grammarize_phrase_delete(phrase):
    # the split operation separates the phrase into a list of individual words
    phrase_words = phrase.split()
    grammarized_phrases_delete_set = []
    # this for loop iterates the word targeted by the grammarize word substitute function
    for i in range(len(phrase_words)):
        target_word = phrase_words[i]
        grammarized_word = grammarize_word_delete(target_word)
        # this for loop incorporates list of successes for the targeted word and adds them to the phrase
        for j in range(len(grammarized_word)):
            target_grammarized_phrase = phrase.split()
            target_grammarized_phrase[i] = grammarized_word[j]
            space = " "
            target_grammarized_phrase = space.join(target_grammarized_phrase)
            # option added to list of successes
            grammarized_phrases_delete_set.append(target_grammarized_phrase)
    return grammarized_phrases_delete_set

def grammarize_phrase(phrase):
    return grammarize_phrase_substitute(phrase) + grammarize_phrase_delete(phrase) + grammarize_phrase_shift(phrase)

def generate_grammarized_phrase_map(phrase_list):
    def add_to_dict(acc, phrase):
        acc[phrase] = grammarize_phrase(phrase)
        return acc
    return reduce(add_to_dict, phrase_list, {})




