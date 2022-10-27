from io import BytesIO
import datetime
import xlsxwriter


def create_report(form=None):
#stworzenie pliku xlsx
   workbook = xlsxwriter.Workbook('Orzeczenie_Tech.xlsx')

#cell definitions
   merge_bold = workbook.add_format({'align':'center','bold': True})
   merge_general = workbook.add_format({'align':'center'})
   merge_format = workbook.add_format({'align':'left','border': True})
   merge_format.set_text_wrap()
   merge_format.set_align('top')
   merge_general_left = workbook.add_format({'align':'left'})

#stworzenie arkusza w pliku xlsx
   worksheet = workbook.add_worksheet()
   worksheet.set_landscape()


#stworzenie prezentacji danych na arkuszu
#lewa strona tytuł
   worksheet.merge_range('C1:E1', 'Wojwódzki Szpital Zespolony', merge_general)
   worksheet.merge_range('C3:E3', 'Orzeczenie Techniczne', merge_bold)

   worksheet.write('A5', 'nr')
   worksheet.write('B5', 'xx/yy')
   worksheet.write('C5', 'Wystawione dnia {0}'.format(datetime.date.today()))

#prawa strona tytuł
   worksheet.merge_range('J1:L1', 'Wojwódzki Szpital Zespolony', merge_general)
   worksheet.merge_range('J3:L3', 'Orzeczenie Techniczne', merge_bold)

   worksheet.write('H5', 'nr')
   worksheet.write('I5', 'xx/yy')
   worksheet.write('J5', 'Wystawione dnia {0}'.format(datetime.date.today()))

#lewa strona dane (1 zestaw tabel)
   worksheet.merge_range('A7:B7', 'Zleceniodawca' ,merge_format,)
   worksheet.merge_range('C7:F7', form.kom_orz.data ,merge_format)

   worksheet.merge_range('A8:B8', 'Miejsce Użytkowania' ,merge_format)
   worksheet.merge_range('C8:F8', form.komorka.data ,merge_format)

   worksheet.merge_range('A9:B9','Nazwa Urzadzenia',merge_format)
   worksheet.merge_range('C9:F9', form.nazwa_urz.data ,merge_format)

#prawa strona dane (1 zestaw tabel)
   worksheet.merge_range('H7:I7', 'Zleceniodawca',merge_format)
   worksheet.merge_range('J7:M7', form.kom_orz.data ,merge_format)

   worksheet.merge_range('H8:I8', 'Miejsce Użytkowania',merge_format)
   worksheet.merge_range('J8:M8', form.komorka.data, merge_format)

   worksheet.merge_range('H9:I9', 'Nazwa Urzadzenia' ,merge_format)
   worksheet.merge_range('J9:M9', form.nazwa_urz.data ,merge_format)

#lewa strona dane (2 zestaw tabel)
   worksheet.merge_range('A11:F11', 'Charakterystyka urządzenia',merge_format)

   worksheet.merge_range('A12:B12', 'a) typ', merge_format)
   worksheet.merge_range('A13:B13', 'c) rok produkcji', merge_format)
   worksheet.merge_range('A14:B14', 'e) czas ekslpoatacji', merge_format)
   worksheet.merge_range('A15:B15', 'g) wartość księgowa', merge_format)

   worksheet.merge_range('D12:E12', 'b) nr fab.', merge_format)
   worksheet.merge_range('D13:E13', 'd) nr inw.', merge_format)
   worksheet.merge_range('D14:E14', 'f) producent', merge_format)
   worksheet.merge_range('D15:E15', 'h) amortyzacja', merge_format)

#prawa strona dane (2 zestaw tabel)
   worksheet.merge_range('H11:M11', 'Charakterystyka urządzenia',merge_format)

   worksheet.merge_range('H12:I12', 'a) typ', merge_format)
   worksheet.merge_range('H13:I13', 'c) rok produkcji', merge_format)
   worksheet.merge_range('H14:I14', 'e) czas ekslpoatacji', merge_format)
   worksheet.merge_range('H15:I15', 'g) wartość księgowa', merge_format)

   worksheet.merge_range('K12:L12', 'b) nr fab.', merge_format)
   worksheet.merge_range('K13:L13', 'd) nr inw.', merge_format)
   worksheet.merge_range('K14:L14', 'f) producent', merge_format)
   worksheet.merge_range('K15:L15', 'h) amortyzacja', merge_format)

#opis lewa strona
   worksheet.merge_range('A17:F17', 'Opis Stanu Technicznego', merge_format)

   worksheet.merge_range('A18:F20', form.opis.data, merge_format)

#opis prawa strona
   worksheet.merge_range('H17:M17', 'Opis Stanu Technicznego', merge_format)

   worksheet.merge_range('H18:M20', form.opis.data, merge_format)

#koniec arkusza
#lewa strona
   worksheet.merge_range('A26:B26', 'Zespół Orzekający:', merge_general_left)
   worksheet.merge_range('A29:B29', '1 .........................', merge_general_left)
   worksheet.merge_range('A33:B33', '2 .........................', merge_general_left)
   worksheet.write('E26', 'Zatwierdzam')

#prawa strona
   worksheet.merge_range('H26:I26', 'Zespół Orzekający:', merge_general_left)
   worksheet.merge_range('H29:I29', '1 .........................', merge_general_left)
   worksheet.merge_range('H33:I33', '2 .........................', merge_general_left)
   worksheet.write('L26', 'Zatwierdzam')

#koniec dokumentu
   workbook.close()




