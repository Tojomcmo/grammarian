import pandas as pd
from functools import reduce

def grab_phrases_from_list(location):
    # csv with single column of spells required
    workbook_read  = pd.read_csv(location)
    spells         = workbook_read.values.tolist()
    # reduces structure of list reduction to single level list
    spell_flatlist = reduce(lambda a,b:a+b, spells)
    return spell_flatlist
    
def print_phrases_to_csv(phrase_set, csv_name):
    with open(csv_name, 'w') as f:
        for key in phrase_set.keys():
            f.write("%s,%s\n"%(key,phrase_set[key]))



