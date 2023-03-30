import xlrd
import xlsxwriter

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