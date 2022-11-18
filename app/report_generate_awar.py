from io import BytesIO
import datetime
import xlsxwriter
from flask_login import current_user
from xlsxwriter import workbook

import app


def create_awaria_rep(awaria_form=None):

    output = BytesIO()

# stworzenie pliku xlsx
    workbook = xlsxwriter.Workbook(output)

#cell definitions



    brutto = workbook.add_format()
    brutto.set_align('right')
    brutto.set_font_size(11)
    brutto.set_font_name('Tahoma')

    koszt = workbook.add_format()
    koszt.set_align('center')
    koszt.set_font_size(11)
    koszt.set_font_name('Tahoma')

    uwagi = workbook.add_format()
    uwagi.set_align('vcenter')
    uwagi.set_font_size(6)

    wyr = workbook.add_format({'bold': True})
    wyr.set_align('center')
    wyr.set_align('bottom')
    wyr.set_font_size(8)

    dyr = workbook.add_format()
    dyr.set_align('top')
    dyr.set_align('center')
    dyr.set_font_size(8)
    dyr.set_text_wrap()

    bold = workbook.add_format({'bold' : True, 'italic' : True})
    bold.set_align('center')

    dotborder = workbook.add_format({'align':'center'})
    dotborder.set_align('center')
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

    data_v = workbook.add_format({'bold': True})
    data_v.set_align('center')
    data_v.set_font_size(9)
    data_v.set_font_name('Tahoma')

#stworzenie arkusza w pliku xlsx i definicja ustawien
    worksheet = workbook.add_worksheet()
    worksheet.set_landscape()
    worksheet.set_margins(left=0.71, right=0.71)
    worksheet.set_column('G1:G1', 4)
    worksheet.set_row(31, 9)
    worksheet.set_row(32, 25)
    worksheet.set_row(27, 8.25)
    worksheet.set_row(30, 24.75)
    worksheet.print_area('A1:M33')
    worksheet.set_paper(9)
    worksheet.center_horizontally()

#lewa strona tytuł
    worksheet.merge_range('A1:D1', 'Sekcja Informatyki i Telekomunikacji', merge_general_left_2)
    worksheet.insert_image('E1', '{0}\\{1}'.format(app.app.root_path,'szpital.png'), {'x_scale': 0.5, 'y_scale': 0.5})
    worksheet.merge_range('C3:D3', 'Protokół Awaryjny', merge_general_bold)
    worksheet.merge_range('A4:B4','Elbląg', data_v)
    worksheet.merge_range('C4:D4','dnia', data_v)
    worksheet.merge_range('E4:F4', '{0}'.format(datetime.date.today()), data_v)

#lewa strona formularz własciwy
    worksheet.merge_range('A6:F6', 'Urządzenie, które uległo awarii, miejsce użytkowania', merge_general_left)
    worksheet.merge_range('A7:F7', awaria_form.urzadz_miejsc.data, merge_all_border)

    worksheet.merge_range('A8:B8', 'Opis Awarii', merge_general_left)
    worksheet.merge_range('A9:F11', awaria_form.opis_awa.data, merge_format)

    worksheet.merge_range('A12:F12', 'Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych', merge_general_left)
    worksheet.merge_range('A13:F14', awaria_form.straty.data, merge_format)

    worksheet.merge_range('A15:D15', 'Zalecenia komisji likwidacji awarii', merge_general_left)
    worksheet.merge_range('A16:F18', awaria_form.zalecenia.data, merge_format)

    worksheet.merge_range('A20:C20', 'koszt szacunkowy naprawy', koszt)

    worksheet.merge_range('D20:E20', awaria_form.koszt_szac.data, dotborder)

    worksheet.write('F20', 'brutto', brutto)


    worksheet.merge_range('C22:D22', 'Komisja Awaryjna',merge_general_bold)

    worksheet.merge_range('A24:B24', awaria_form.czlonek_1.data, bold)
    worksheet.merge_range('C24:D24', awaria_form.stanowisko_1.data, bold)
    worksheet.merge_range('E24:F24', '...........................', bold)

    worksheet.merge_range('A26:B26', awaria_form.czlonek_2.data, bold)
    worksheet.merge_range('C26:D26', awaria_form.stanowisko_2.data, bold)
    worksheet.merge_range('E26:F26', '...........................', bold)


    worksheet.merge_range('A27:F27', 'Wyrażam zgodę/nie wyrażam zgody* na realizację zaleceń komisji awaryjnej', wyr)
    worksheet.merge_range('A29:F30','',dotborder)

    worksheet.write('A28', 'Uwagi:', uwagi)
    worksheet.merge_range('E32:F32','...........................', bold)
    worksheet.merge_range('E33:F33','Dyrektor ds. Techniczno - Eksploatacyjnych', dyr)



#prawa strona tytuł
    worksheet.merge_range('H1:K1', 'Sekcja Informatyki i Telekomunikacji', merge_general_left_2)
    #obrazek
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
