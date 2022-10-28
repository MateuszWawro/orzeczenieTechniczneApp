from io import BytesIO
import datetime
import xlsxwriter
from flask_login import current_user


def create_report(form=None):

   output = BytesIO()

#stworzenie pliku xlsx
   workbook = xlsxwriter.Workbook(output)

#cell definitions
   footer = workbook.add_format()
   footer.set_font_size(4)
   footer.set_align('right')
   footer.set_font_name('Courier New')

   left = workbook.add_format({'align': 'left'})
   left.set_font_size(10)
   left.set_font_name('Tahoma')

   right = workbook.add_format({'align':'right'})
   right.set_font_size(11.5)
   right.set_font_name('Tahoma')

   center = workbook.add_format({'align':'center'})
   center.set_font_size(11.5)
   center.set_font_name('Tahoma')

   merge_bold_italic = workbook.add_format({'align':'center','bold': True, 'italic' : True, 'border' : True })
   merge_bold_italic.set_font_size(10)
   merge_bold_italic.set_font_name('Tahoma')

   merge_bold = workbook.add_format({'align':'center','bold': True})
   merge_bold.set_font_size(11.5)
   merge_bold.set_font_name('Tahoma')

   merge_general = workbook.add_format({'align':'center'})
   merge_general.set_font_size(11.5)
   merge_general.set_font_name('Tahoma')

   merge_format = workbook.add_format({'align':'left','border': True})
   merge_format.set_font_size(10)
   merge_format.set_font_name('Tahoma')
   merge_format.set_text_wrap()
   merge_format.set_align('top')

   merge_format_left = workbook.add_format({'align':'center', 'border' : True})
   merge_format_left.set_font_size(10)
   merge_format_left.set_font_name('Tahoma')

   merge_general_left = workbook.add_format({'align':'left'})
   merge_general_left.set_font_size(10)
   merge_general_left.set_font_name('Tahoma')

#stworzenie arkusza w pliku xlsx i definicja ustawien
   worksheet = workbook.add_worksheet()
   worksheet.set_landscape()
   worksheet.set_margins(left=0.25, right=0.25)
   worksheet.set_column('G1:G1', 1)
   worksheet.print_area('A1:M33')
   worksheet.set_paper(9)
   worksheet.center_horizontally()

#stworzenie prezentacji danych na arkuszu
#lewa strona tytuł
   worksheet.merge_range('C1:E1', 'Wojewódzki Szpital Zespolony', merge_general)
   worksheet.merge_range('C3:E3', 'ORZECZENIE TECHNICZNE', merge_bold)

   worksheet.write('A5', 'nr', right)
   worksheet.write('B5', '{0}/{1}'.format(form.numer_wniosku.data, datetime.date.today().year), center)
   worksheet.merge_range('C5:F5', 'Wystawione dnia {0}'.format(datetime.date.today()), merge_general)

#prawa strona tytuł
   worksheet.merge_range('J1:L1', 'Wojewódzki Szpital Zespolony', merge_general)
   worksheet.merge_range('J3:L3', 'ORZECZENIE TECHNICZNE', merge_bold)

   worksheet.write('H5', 'nr', right)
   worksheet.write('I5', '{0}/{1}'.format(form.numer_wniosku.data, datetime.date.today().year), center)
   worksheet.merge_range('J5:M5', 'Wystawione dnia {0}'.format(datetime.date.today()), merge_general)

#lewa strona dane (1 zestaw tabel)
   worksheet.merge_range('A7:B7', 'Zleceniodawca' ,merge_format,)
   worksheet.merge_range('C7:F7', form.kom_orz.data ,merge_bold_italic)

   worksheet.merge_range('A8:B8', 'Miejsce Użytkowania' ,merge_format)
   worksheet.merge_range('C8:F8', form.komorka.data , merge_format_left)

   worksheet.merge_range('A9:B9','Nazwa Urzadzenia',merge_format)
   worksheet.merge_range('C9:F9', form.nazwa_urz.data ,merge_bold_italic)

#prawa strona dane (1 zestaw tabel)
   worksheet.merge_range('H7:I7', 'Zleceniodawca',merge_format)
   worksheet.merge_range('J7:M7', form.kom_orz.data ,merge_bold_italic)

   worksheet.merge_range('H8:I8', 'Miejsce Użytkowania',merge_format)
   worksheet.merge_range('J8:M8', form.komorka.data, merge_format_left)

   worksheet.merge_range('H9:I9', 'Nazwa Urzadzenia' ,merge_format)
   worksheet.merge_range('J9:M9', form.nazwa_urz.data ,merge_bold_italic)

#lewa strona dane (2 zestaw tabel)
   worksheet.merge_range('A11:F11', 'Charakterystyka urządzenia',merge_format)

   worksheet.merge_range('A12:B12', 'a) typ', merge_format)
   worksheet.write('C12', form.typ.data, merge_bold_italic)
   worksheet.set_column('C12:C12',12)
   worksheet.merge_range('A13:B13', 'c) rok produkcji', merge_format)
   worksheet.write('C13', form.rok.data, merge_bold_italic)
   worksheet.merge_range('A14:B14', 'e) czas eksploatacji', merge_format)
   worksheet.write('C14', form.lata.data, merge_bold_italic)
   worksheet.merge_range('A15:B15', 'g) wartość księgowa', merge_format)
   worksheet.write('C15', form.cena.data, merge_bold_italic)

   worksheet.merge_range('D12:E12', 'b) nr fab.', merge_format)
   worksheet.set_column('D12:E12',8)
   worksheet.write('F12', form.num_fab.data, merge_bold_italic)
   worksheet.set_column('F12:F12',20)
   worksheet.merge_range('D13:E13', 'd) nr inw.', merge_format)
   worksheet.write('F13', form.num_inw.data, merge_bold_italic)
   worksheet.merge_range('D14:E14', 'f) producent', merge_format)
   worksheet.write('F14', form.producent.data, merge_bold_italic)
   worksheet.merge_range('D15:E15', 'h) amortyzacja', merge_format)
   worksheet.write('F15', form.amortyzacja.data, merge_bold_italic)

#prawa strona dane (2 zestaw tabel)
   worksheet.merge_range('H11:M11', 'Charakterystyka urządzenia',merge_format)

   worksheet.merge_range('H12:I12', 'a) typ', merge_format)
   worksheet.write('J12', form.typ.data, merge_bold_italic)
   worksheet.set_column('J12:J12',12)
   worksheet.merge_range('H13:I13', 'c) rok produkcji', merge_format)
   worksheet.write('J13', form.rok.data, merge_bold_italic)
   worksheet.merge_range('H14:I14', 'e) czas eksploatacji', merge_format)
   worksheet.write('J14', form.lata.data, merge_bold_italic)
   worksheet.merge_range('H15:I15', 'g) wartość księgowa', merge_format)
   worksheet.write('J15', form.cena.data, merge_bold_italic)
   worksheet.merge_range('K12:L12', 'b) nr fab.', merge_format)
   worksheet.set_column('K12:L12',8)
   worksheet.write('M12', form.num_fab.data, merge_bold_italic)
   worksheet.set_column('M12:M12',20)
   worksheet.merge_range('K13:L13', 'd) nr inw.', merge_format)
   worksheet.write('M13', form.num_inw.data, merge_bold_italic)
   worksheet.merge_range('K14:L14', 'f) producent', merge_format)
   worksheet.write('M14', form.producent.data, merge_bold_italic)
   worksheet.merge_range('K15:L15', 'h) amortyzacja', merge_format)
   worksheet.write('M15', form.amortyzacja.data, merge_bold_italic)

#opis lewa strona
   worksheet.merge_range('A17:F17', 'Opis Stanu Technicznego', merge_format)

   worksheet.merge_range('A18:F20', form.opis.data, merge_format)

#opis prawa strona
   worksheet.merge_range('H17:M17', 'Opis Stanu Technicznego', merge_format)

   worksheet.merge_range('H18:M20', form.opis.data, merge_format)

#uwagi i wnioski(obie strony)
   worksheet.merge_range('A22:F22','Uwagi i wnioski', merge_format )
   worksheet.merge_range('A23:F23', 'Proszę o zgodę na skasowanie ww. sprzętu', merge_format)

   worksheet.merge_range('H22:M22','Uwagi i wnioski', merge_format )
   worksheet.merge_range('H23:M23', 'Proszę o zgodę na skasowanie ww. sprzętu', merge_format)

#koniec arkusza
#lewa strona
   worksheet.merge_range('A25:B25', 'Zespół Orzekający:', merge_general_left)
   worksheet.merge_range('A29:B29', '1 ......................................', merge_general_left)
   worksheet.merge_range('A33:B33', '2 ......................................', merge_general_left)
   worksheet.write('F25', 'Zatwierdzam', left)

#prawa strona
   worksheet.merge_range('H25:I25', 'Zespół Orzekający:', merge_general_left)
   worksheet.merge_range('H29:I29', '1 ......................................', merge_general_left)
   worksheet.merge_range('H33:I33', '2 ......................................', merge_general_left)
   worksheet.write('M25', 'Zatwierdzam', left)


#a'la stopka lewa i prawa strona
   worksheet.merge_range('D33:F33', 'Wygenerowano dnia {0} przez {1} {2}'.format(datetime.date.today(),current_user.name ,
                                                                           current_user.surname), footer)
   worksheet.merge_range('K33:M33', 'Wygenerowano dnia {0} przez {1} {2}'.format(datetime.date.today(), current_user.name,
                                                                           current_user.surname), footer)
#koniec dokumentu
   workbook.close()
   output.seek(0)
   return output
