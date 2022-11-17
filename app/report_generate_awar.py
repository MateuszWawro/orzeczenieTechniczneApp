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
    dotborder = workbook.add_format({'align':'center'})
    dotborder.set_border(8)

    merge_format = workbook.add_format({'align': 'left', 'border': True})
    merge_format.set_font_size(10)
    merge_format.set_font_name('Tahoma')
    merge_format.set_text_wrap()
    merge_format.set_align('top')

    border = workbook.add_format({'border' : True})

    merge_all_border = workbook.add_format({'border' : True})
    merge_all_border.set_font_size(10)
    merge_all_border.set_font_name('Tahoma')

    merge_general_left = workbook.add_format({'align': 'left'})
    merge_general_left.set_font_size(8)
    merge_general_left.set_font_name('Tahoma')

    merge_general_left_2 = workbook.add_format({'align': 'left'})
    merge_general_left_2.set_font_size(10)
    merge_general_left_2.set_font_name('Tahoma')

    merge_general = workbook.add_format({'align': 'center'})
    merge_general.set_font_size(10)
    merge_general.set_font_name('Tahoma')

    merge_general_bold = workbook.add_format({'align': 'center', 'bold': True})
    merge_general_bold.set_font_size(10)
    merge_general_bold.set_font_name('Tahoma')

    center = workbook.add_format({'align': 'center'})
    center.set_font_size(10)
    center.set_font_name('Tahoma')

#stworzenie arkusza w pliku xlsx i definicja ustawien
    worksheet = workbook.add_worksheet()
    worksheet.set_landscape()
    worksheet.set_margins(left=0.71, right=0.71)
    worksheet.set_column('G1:G1', 4)
    worksheet.print_area('A1:M33')
    worksheet.set_paper(9)
    worksheet.center_horizontally()

#lewa strona tytuł
    worksheet.merge_range('A1:D1', 'Sekcja Inormatyki Telekomunikacji', merge_general_left_2)
    worksheet.merge_range('A2:C2', 'Wojewódzki Szpital Zespolony', center)
    worksheet.merge_range('C3:D3', 'Protokół Awaryjny', merge_general_bold)
    worksheet.write('A4','data', center)
    worksheet.write('B4', '{0}'.format(datetime.date.today()))

#lewa strona formularz własciwy
    worksheet.merge_range('A6:F6', 'Urządzenie, które uległo awarii, miejsce użytkowania', merge_general_left)
    worksheet.merge_range('A7:F7', awaria_form.urzadz_miejsc.data, merge_all_border)

    worksheet.merge_range('A8:B8', 'Opis Awarii', merge_general_left)
    worksheet.merge_range('A9:F11', awaria_form.opis_awa.data, merge_format)

    worksheet.merge_range('A12:F12', 'Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych', merge_general_left)
    worksheet.merge_range('A13:F14', awaria_form.straty.data, merge_format)

    worksheet.merge_range('A15:D15', 'Zalecenia komisji likwidacji awarii', merge_general_left)
    worksheet.merge_range('A16:F18', awaria_form.zalecenia.data, merge_format)

    worksheet.merge_range('A20:B20', 'koszt szacunkowy awarii', merge_general_left)

    worksheet.write('D20', awaria_form.koszt_szac.data, dotborder)

    #worksheet.set_('A22:F26', '' ,border)
    worksheet.merge_range('C22:D22', 'Komisja Awaryjna',merge_general_bold)

    worksheet.merge_range('A23:B23', awaria_form.czlonek_1.data)
    #worksheet.merge_range('D')

    worksheet.merge_range('A25:B25', awaria_form.czlonek_2.data)

    worksheet.write('E20', 'brutto', merge_general_left)

#prawa strona tytuł
    worksheet.merge_range('H1:K1', 'Sekcja Inormatyki Telekomunikacji', merge_general_left_2)
    worksheet.merge_range('H2:J2', 'Wojewódzki Szpital Zespolony', center)
    worksheet.merge_range('J3:K3', 'Protokół Awaryjny', merge_general_bold)
    worksheet.write('H4', 'data', center)
    worksheet.write('I4', '{0}'.format(datetime.date.today()))

# prawa strona formularz własciwy
    worksheet.merge_range('H6:L6', 'Urządzenie, które uległo awarii, miejsce użytkowania', merge_general_left)

    worksheet.merge_range('H8:I8', 'Opis Awarii', merge_general_left)

    worksheet.merge_range('H12:M12', 'Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych',
                          merge_general_left)

    worksheet.merge_range('H15:K15', 'Zalecenia komisji likwidacji awarii', merge_general_left)

    worksheet.merge_range('H19:J19', 'koszt szacunkowy awarii', merge_general_left)

    worksheet.write('M19', 'brutto', center)

    workbook.close()
    output.seek(0)
    return output
