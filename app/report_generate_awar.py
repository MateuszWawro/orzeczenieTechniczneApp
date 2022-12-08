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

    footer = workbook.add_format()
    footer.set_font_size(4)
    footer.set_align('left')
    footer.set_align('bottom')
    footer.set_font_name('Courier New')

    brutto = workbook.add_format()
    brutto.set_align('left')
    brutto.set_font_size(10)
    brutto.set_font_name('Tahoma')

    koszt = workbook.add_format()
    koszt.set_align('center')
    koszt.set_font_size(10)
    koszt.set_font_name('Tahoma')

    uwagi = workbook.add_format()
    uwagi.set_align('vcenter')
    uwagi.set_font_size(6)

    wyr = workbook.add_format({'bold': True})
    wyr.set_align('center')
    wyr.set_align('bottom')
    wyr.set_font_size(10)

    dyr = workbook.add_format()
    dyr.set_align('top')
    dyr.set_align('center')
    dyr.set_font_size(9.5)
    dyr.set_text_wrap()

    bold = workbook.add_format({'bold' : True, 'italic' : True})
    bold.set_align('center')

    dotborder = workbook.add_format({'align':'center'})
    dotborder.set_align('center')
    dotborder.set_border(4)

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
    merge_general_left.set_font_size(10)
    merge_general_left.set_font_name('Tahoma')

    merge_center = workbook.add_format({'align': 'center', 'bold': True})
    merge_center.set_font_size(10)
    merge_center.set_font_name('Tahoma')

    merge_general = workbook.add_format({'align': 'center'})
    merge_general.set_font_size(10)
    merge_general.set_font_name('Tahoma')

    merge_general_bold = workbook.add_format({'align': 'center', 'bold': True})
    merge_general_bold.set_font_size(10)
    merge_general_bold.set_font_name('Tahoma')

    center = workbook.add_format({'align': 'center'})
    center.set_font_size(10)
    center.set_font_name('Tahoma')

    data_v = workbook.add_format({'italic': True , 'bold': True})
    data_v.set_align('right')
    data_v.set_font_size(8)
    data_v.set_font_name('Tahoma')

#stworzenie arkusza w pliku xlsx i definicja ustawien
    worksheet = workbook.add_worksheet()
    worksheet.set_landscape()
    worksheet.set_margins(left=0, right=0, top=0, bottom=0)
    worksheet.set_column('H1:H1', 4)
    worksheet.set_column('I1:I1', 4)
    worksheet.set_row(13, 35.25)
    worksheet.set_row(36, 9)
    worksheet.set_row(37, 26.25)
    worksheet.set_row(30, 8.25)
    worksheet.print_area('A1:P38')
    worksheet.set_paper(9)
    worksheet.center_horizontally()
    worksheet.center_vertically()

#lewa strona tytuł
    worksheet.merge_range('B1:E1', 'Sekcja Informatyki i Telekomunikacji', merge_center)
    worksheet.insert_image('A1', '{0}\\{1}'.format(app.app.root_path,'szpital.png'), {'x_scale': 0.2, 'y_scale': 0.2})
    worksheet.merge_range('C3:E3', 'Protokół Awaryjny', merge_general_bold)
    worksheet.merge_range('E2:G2', 'Elbląg, dn. {0}'.format(datetime.date.today()), data_v)

#lewa strona formularz własciwy
    worksheet.merge_range('A5:G5', 'Urządzenie, które uległo awarii, miejsce użytkowania', merge_general_left)
    worksheet.merge_range('A6:G6', awaria_form.urzadz_miejsc.data, merge_all_border)

    worksheet.merge_range('A7:B7', 'Opis Awarii', merge_general_left)
    worksheet.merge_range('A8:G11', awaria_form.opis_awa.data, merge_format)

    worksheet.merge_range('A12:G12', 'Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych', merge_general_left)
    worksheet.merge_range('A13:G14', awaria_form.straty.data, merge_format)

    worksheet.merge_range('A15:D15', 'Zalecenia komisji', merge_general_left)
    worksheet.merge_range('A16:G19', awaria_form.zalecenia.data, merge_format)

    worksheet.merge_range('A21:C21', 'koszt szacunkowy naprawy', koszt)
    worksheet.merge_range('D21:E21', awaria_form.koszt_szac.data, dotborder)

    worksheet.write('F21', 'brutto', brutto)


    worksheet.merge_range('C23:E23', 'Komisja',merge_general_bold)

    worksheet.merge_range('A25:B25', awaria_form.czlonek_1.data, bold)
    worksheet.merge_range('C25:D25', awaria_form.stanowisko_1.data, bold)
    worksheet.merge_range('E26:G26', '.............................................', bold)

    worksheet.merge_range('A28:B28', awaria_form.czlonek_2.data, bold)
    worksheet.merge_range('C28:D28', awaria_form.stanowisko_2.data, bold)
    worksheet.merge_range('E29:G29', '.............................................', bold)


    worksheet.merge_range('A30:G30', 'Wyrażam zgodę/nie wyrażam zgody* na realizację zaleceń komisji awaryjnej', wyr)
    worksheet.merge_range('A32:G34','',dotborder)

    worksheet.write('A31', 'Uwagi:', uwagi)
    worksheet.merge_range('E37:G37','..............................................', bold)
    worksheet.merge_range('E38:G38','Dyrektor ds. Techniczno - Eksploatacyjnych', dyr)



#prawa strona tytuł
    worksheet.merge_range('K1:N1', 'Sekcja Informatyki i Telekomunikacji', merge_center)
    worksheet.insert_image('J1', '{0}\\{1}'.format(app.app.root_path, 'szpital.png'), {'x_scale': 0.2, 'y_scale': 0.2})
    worksheet.merge_range('L3:N3', 'Protokół Awaryjny', merge_general_bold)
    worksheet.merge_range('N2:P2', 'Elbląg, dn. {0}'.format(datetime.date.today()), data_v)

# prawa strona formularz własciwy
    worksheet.merge_range('J5:P5', 'Urządzenie, które uległo awarii, miejsce użytkowania', merge_general_left)
    worksheet.merge_range('J6:P6', awaria_form.urzadz_miejsc.data, merge_all_border)

    worksheet.merge_range('J7:P7', 'Opis Awarii', merge_general_left)
    worksheet.merge_range('J8:P11', awaria_form.opis_awa.data, merge_format)

    worksheet.merge_range('J12:P12', 'Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych',
                          merge_general_left)
    worksheet.merge_range('J13:P14', awaria_form.straty.data, merge_format)

    worksheet.merge_range('J15:P15', 'Zalecenia komisji ', merge_general_left)
    worksheet.merge_range('J16:P19', awaria_form.zalecenia.data, merge_format)

    worksheet.merge_range('J21:L21', 'koszt szacunkowy naprawy', koszt)
    worksheet.merge_range('M21:N21', awaria_form.koszt_szac.data, dotborder)

    worksheet.write('O21', 'brutto', brutto)

    worksheet.merge_range('L23:N23', 'Komisja', merge_general_bold)

    worksheet.merge_range('J25:K25', awaria_form.czlonek_1.data, bold)
    worksheet.merge_range('L25:M25', awaria_form.stanowisko_1.data, bold)
    worksheet.merge_range('N26:P26', '.............................................', bold)

    worksheet.merge_range('J28:K28', awaria_form.czlonek_2.data, bold)
    worksheet.merge_range('L28:M28', awaria_form.stanowisko_2.data, bold)
    worksheet.merge_range('N29:P29', '.............................................', bold)

    worksheet.merge_range('J30:P30', 'Wyrażam zgodę/nie wyrażam zgody* na realizację zaleceń komisji awaryjnej', wyr)
    worksheet.merge_range('J32:P34', '', dotborder)

    worksheet.write('J31', 'Uwagi:', uwagi)
    worksheet.merge_range('N37:P37', '..............................................', bold)
    worksheet.merge_range('N38:P38', 'Dyrektor ds. Techniczno - Eksploatacyjnych', dyr)

    worksheet.merge_range('A38:D38',
                          'Wygenerowano dnia {0} przez {1} {2}'.format(datetime.date.today(), current_user.name,
                                                                       current_user.surname), footer)
    worksheet.merge_range('J38:M38',
                          'Wygenerowano dnia {0} przez {1} {2}'.format(datetime.date.today(), current_user.name,
                                                                       current_user.surname), footer)

    workbook.close()
    output.seek(0)
    return output


def generate_report_sec(lista_query_sec=None):

    output = BytesIO()

# stworzenie pliku xlsx
    workbook = xlsxwriter.Workbook(output)

#cell definitions

    footer = workbook.add_format()
    footer.set_font_size(4)
    footer.set_align('left')
    footer.set_align('bottom')
    footer.set_font_name('Courier New')

    brutto = workbook.add_format()
    brutto.set_align('left')
    brutto.set_font_size(10)
    brutto.set_font_name('Tahoma')

    koszt = workbook.add_format()
    koszt.set_align('center')
    koszt.set_font_size(10)
    koszt.set_font_name('Tahoma')

    uwagi = workbook.add_format()
    uwagi.set_align('vcenter')
    uwagi.set_font_size(6)

    wyr = workbook.add_format({'bold': True})
    wyr.set_align('center')
    wyr.set_align('bottom')
    wyr.set_font_size(10)

    dyr = workbook.add_format()
    dyr.set_align('top')
    dyr.set_align('center')
    dyr.set_font_size(9.5)
    dyr.set_text_wrap()

    bold = workbook.add_format({'bold' : True, 'italic' : True})
    bold.set_align('center')

    dotborder = workbook.add_format({'align':'center'})
    dotborder.set_align('center')
    dotborder.set_border(4)

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
    merge_general_left.set_font_size(10)
    merge_general_left.set_font_name('Tahoma')

    merge_center = workbook.add_format({'align': 'center', 'bold': True})
    merge_center.set_font_size(10)
    merge_center.set_font_name('Tahoma')

    merge_general = workbook.add_format({'align': 'center'})
    merge_general.set_font_size(10)
    merge_general.set_font_name('Tahoma')

    merge_general_bold = workbook.add_format({'align': 'center', 'bold': True})
    merge_general_bold.set_font_size(10)
    merge_general_bold.set_font_name('Tahoma')

    center = workbook.add_format({'align': 'center'})
    center.set_font_size(10)
    center.set_font_name('Tahoma')

    data_v = workbook.add_format({'italic': True , 'bold': True})
    data_v.set_align('right')
    data_v.set_font_size(8)
    data_v.set_font_name('Tahoma')
    data_v.set_num_format(14)

#stworzenie arkusza w pliku xlsx i definicja ustawien
    worksheet = workbook.add_worksheet()
    worksheet.set_landscape()
    worksheet.set_margins(left=0, right=0, top=0, bottom=0)
    worksheet.set_column('H1:H1', 4)
    worksheet.set_column('I1:I1', 4)
    worksheet.set_row(13, 35.25)
    worksheet.set_row(36, 9)
    worksheet.set_row(37, 26.25)
    worksheet.set_row(30, 8.25)
    worksheet.print_area('A1:P38')
    worksheet.set_paper(9)
    worksheet.center_horizontally()
    worksheet.center_vertically()

#lewa strona tytuł
    worksheet.merge_range('B1:E1', 'Sekcja Informatyki i Telekomunikacji', merge_center)
    worksheet.insert_image('A1', '{0}\\{1}'.format(app.app.root_path,'szpital.png'), {'x_scale': 0.2, 'y_scale': 0.2})
    worksheet.merge_range('C3:E3', 'Protokół Awaryjny', merge_general_bold)
    worksheet.merge_range('F2:G2', lista_query_sec.date, data_v)

#lewa strona formularz własciwy
    worksheet.merge_range('A5:G5', 'Urządzenie, które uległo awarii, miejsce użytkowania:', merge_general_left)
    worksheet.merge_range('A6:G6', lista_query_sec.urzadz_miejsc, merge_all_border)

    worksheet.merge_range('A7:B7', 'Opis Awarii:', merge_general_left)
    worksheet.merge_range('A8:G11', lista_query_sec.opis, merge_format)

    worksheet.merge_range('A12:G12', 'Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych:', merge_general_left)
    worksheet.merge_range('A13:G14', lista_query_sec.straty, merge_format)

    worksheet.merge_range('A15:D15', 'Zalecenia komisji:', merge_general_left)
    worksheet.merge_range('A16:G19', lista_query_sec.zalecenia, merge_format)

    worksheet.merge_range('A21:C21', 'koszt szacunkowy naprawy:', koszt)
    worksheet.merge_range('D21:E21', lista_query_sec.koszt_szac, dotborder)

    worksheet.write('F21', 'brutto', brutto)


    worksheet.merge_range('C23:E23', 'Komisja',merge_general_bold)

    worksheet.merge_range('A25:B25', lista_query_sec.cz_1_kom, bold)
    worksheet.merge_range('C25:D25', lista_query_sec.stanowisko, bold)
    worksheet.merge_range('E26:G26', '.............................................', bold)

    worksheet.merge_range('A28:B28', lista_query_sec.cz_2_kom, bold)
    worksheet.merge_range('C28:D28', lista_query_sec.stanowisko2, bold)
    worksheet.merge_range('E29:G29', '.............................................', bold)


    worksheet.merge_range('A30:G30', 'Wyrażam zgodę/nie wyrażam zgody* na realizację zaleceń komisji awaryjnej', wyr)
    worksheet.merge_range('A32:G34','',dotborder)

    worksheet.write('A31', 'Uwagi:', uwagi)
    worksheet.merge_range('E37:G37','..............................................', bold)
    worksheet.merge_range('E38:G38','Dyrektor ds. Techniczno - Eksploatacyjnych', dyr)



#prawa strona tytuł
    worksheet.merge_range('K1:N1', 'Sekcja Informatyki i Telekomunikacji', merge_center)
    worksheet.insert_image('J1', '{0}\\{1}'.format(app.app.root_path, 'szpital.png'), {'x_scale': 0.2, 'y_scale': 0.2})
    worksheet.merge_range('L3:N3', 'Protokół Awaryjny', merge_general_bold)
    worksheet.merge_range('N2:P2',  lista_query_sec.date, data_v)

# prawa strona formularz własciwy
    worksheet.merge_range('J5:P5', 'Urządzenie, które uległo awarii, miejsce użytkowania:', merge_general_left)
    worksheet.merge_range('J6:P6', lista_query_sec.urzadz_miejsc, merge_all_border)

    worksheet.merge_range('J7:P7', 'Opis Awarii', merge_general_left)
    worksheet.merge_range('J8:P11', lista_query_sec.opis, merge_format)

    worksheet.merge_range('J12:P12', 'Przewidywane zwiększenie strat w przypadku nie podjęcia dzialań naprawczych:',
                          merge_general_left)
    worksheet.merge_range('J13:P14', lista_query_sec.straty, merge_format)

    worksheet.merge_range('J15:P15', 'Zalecenia komisji:', merge_general_left)
    worksheet.merge_range('J16:P19', lista_query_sec.zalecenia, merge_format)

    worksheet.merge_range('J21:L21', 'koszt szacunkowy naprawy:', koszt)
    worksheet.merge_range('M21:N21', lista_query_sec.koszt_szac, dotborder)

    worksheet.write('O21', 'brutto', brutto)

    worksheet.merge_range('L23:N23', 'Komisja', merge_general_bold)

    worksheet.merge_range('J25:K25', lista_query_sec.cz_1_kom, bold)
    worksheet.merge_range('L25:M25', lista_query_sec.stanowisko, bold)
    worksheet.merge_range('N26:P26', '.............................................', bold)

    worksheet.merge_range('J28:K28', lista_query_sec.cz_2_kom, bold)
    worksheet.merge_range('L28:M28', lista_query_sec.stanowisko2, bold)
    worksheet.merge_range('N29:P29', '.............................................', bold)

    worksheet.merge_range('J30:P30', 'Wyrażam zgodę/nie wyrażam zgody* na realizację zaleceń komisji awaryjnej', wyr)
    worksheet.merge_range('J32:P34', '', dotborder)

    worksheet.write('J31', 'Uwagi:', uwagi)
    worksheet.merge_range('N37:P37', '..............................................', bold)
    worksheet.merge_range('N38:P38', 'Dyrektor ds. Techniczno - Eksploatacyjnych', dyr)

    worksheet.merge_range('A38:D38',
                          'Wygenerowano dnia {0} przez {1} {2}'.format(datetime.date.today(), current_user.name,
                                                                       current_user.surname), footer)
    worksheet.merge_range('J38:M38',
                          'Wygenerowano dnia {0} przez {1} {2}'.format(datetime.date.today(), current_user.name,
                                                                       current_user.surname), footer)

    workbook.close()
    output.seek(0)
    return output