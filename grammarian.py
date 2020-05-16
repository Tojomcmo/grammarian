import enchant
import string

import xlrd
import xlsxwriter


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
    grammarized_phrase_set = []
    substitute = grammarize_phrase_substitute(phrase)
    delete = grammarize_phrase_delete(phrase)
    shift = grammarize_phrase_shift(phrase)
    for i in range(len(substitute)):
        grammarized_phrase_set.append(substitute[i])
    for j in range(len(delete)):
        grammarized_phrase_set.append(delete[j])
    for k in range(len(shift)):
        grammarized_phrase_set.append(shift[k])
    return grammarized_phrase_set

def grammarize_phrase_list(phrase_list):
    grammarized_phrase_list = []
    for i in range(len(phrase_list)):
        grammarized_phrase = grammarize_phrase(phrase_list[i])
        for j in range(len(grammarized_phrase)):
            grammarized_phrase_list.append(grammarized_phrase[j])
    return grammarized_phrase_list

def grammarize_phrase_set(phrase_list):
    grammarized_phrase_set = []
    for i in range(len(phrase_list)):
        kernel_phrase = phrase_list[i]
        grammarized_phrases = grammarize_phrase(phrase_list[i])
        grammarized_phrases.insert(0, kernel_phrase)
        grammarized_phrase_set.append(grammarized_phrases)
    return grammarized_phrase_set

def grab_phrases_from_list(location):
    workbook_read = xlrd.open_workbook(location)
    worksheet_read = workbook_read.sheet_by_index(0)
    spells = []
    for i in range(worksheet_read.nrows):
        spells.append(worksheet_read.cell_value(i, 0))
    return spells

def print_phrases_to_csv(phrase_set, csv_name):
    workbook_write = xlsxwriter.Workbook(csv_name)
    worksheet_write = workbook_write.add_worksheet()
    col = 0
    cell_format = workbook_write.add_format({'bold': True, 'underline': True, 'center_across': True})
    cell_format.set_bold()
    for j in range(len(phrase_set)):
        row = 0
        worksheet_write.set_column(j, j, len(phrase_set[j][0]) + 2)
        for item in (phrase_set[j]):
            if row is 0:
                worksheet_write.write(row, j, item, cell_format)
                row += 1
            else:
                worksheet_write.write(row, j, item)
                row += 1
    workbook_write.close()

# /Users/thomasmoriarty/PycharmProjects/untitled/mcclubbin_spells.xlsx
# provide pathname for input list excel file without quotes (example above)
# excel file saved in repo folder

location = input("give me thyne spells : ")
print("choose wisely...")

spells = grab_phrases_from_list(location)
grammarized_spells = grammarize_phrase_set(spells)
print_phrases_to_csv(grammarized_spells, "grammarian_output.xlsx")


