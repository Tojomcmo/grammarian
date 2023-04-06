# /Users/thomasmoriarty/PycharmProjects/untitled/mcclubbin_spells.xlsx
# provide pathname for input list excel file without quotes (example above)
# excel file saved in repo folder
import grammarian as gm
import grammarian_io as gm_io


if __name__ == '__main__':
    location = input("give me thyne spells : ")
    print("choose wisely...")

    spells = gm_io.grab_phrases_from_list(location)
    grammarized_spells = gm.generate_grammarized_phrase_map(spells)
    gm_io.print_phrases_to_csv(grammarized_spells, "grammarian_output.csv")