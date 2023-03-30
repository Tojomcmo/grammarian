# /Users/thomasmoriarty/PycharmProjects/untitled/mcclubbin_spells.xlsx
# provide pathname for input list excel file without quotes (example above)
# excel file saved in repo folder




if __name__ == '__main__':
    location = input("give me thyne spells : ")
    print("choose wisely...")

    spells = grab_phrases_from_list(location)
    grammarized_spells = grammarize_phrase_set(spells)
    print_phrases_to_csv(grammarized_spells, "grammarian_output.xlsx")