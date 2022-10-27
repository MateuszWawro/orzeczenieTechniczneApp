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

   workbook.close()




