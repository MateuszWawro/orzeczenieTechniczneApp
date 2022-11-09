from io import BytesIO
import datetime
import xlsxwriter
from flask_login import current_user
from xlsxwriter import workbook


def create_awaria_rep(awaria_form=None):

    output = BytesIO()

# stworzenie pliku xlsx
    workbook = xlsxwriter.Workbook(output)

#cell definitions

    merge_general_left = workbook.add_format({'align': 'left'})
    merge_general_left.set_font_size(10)
    merge_general_left.set_font_name('Tahoma')

    merge_general = workbook.add_format({'align': 'center'})
    merge_general.set_font_size(10)
    merge_general.set_font_name('Tahoma')


#stworzenie arkusza w pliku xlsx i definicja ustawien
    worksheet = workbook.add_worksheet()
    worksheet.set_landscape()
    worksheet.set_margins(left=0.25, right=0.25)
    worksheet.set_column('G1:G1', 1)
    worksheet.print_area('A1:M33')
    worksheet.set_paper(9)
    worksheet.center_horizontally()

#lewa strona tytuł
    worksheet.merge_range('A1:D1', 'Sekcja Inormatyki Telekomunikacji', merge_general_left)
    worksheet.merge_range('A2:C2', 'Wojewódzki Szpital Zespolony', merge_general_left)
    worksheet.merge_range('D3:E3', 'Protokół Awaryjny', merge_general)
    worksheet.write('A4','data')
    worksheet.write('B4', '{0}'.format(datetime.date.today()))

#formularz własciwy
    worksheet.merge_range('A6:F6', 'Urządzenie, które uległo awarii, miejsce użytkowania', merge_general_left)

    worksheet.merge_range('A8:B8', 'Opis Awarii', merge_general_left)

    worksheet.merge_range('A12:G12','Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych', merge_general_left)

    worksheet.merge_range('A15:D15', 'Zalecenia komisji likwidacji awarii', merge_general_left)

    worksheet.merge_range('A19:C19', 'koszt szacunkowy awarii', merge_general_left)

    worksheet.write('F19', 'brutto')

    workbook.close()
    output.seek(0)
    return output
