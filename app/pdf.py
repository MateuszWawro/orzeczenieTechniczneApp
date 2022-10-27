from io import BytesIO
import xlsxwriter


def create_report(form=None):
#stworzenie pliku xlsx
   workbook = xlsxwriter.Workbook('Orzeczenie_Tech.xlsx')

#cell definitions
   bold = workbook.add_format({'bold': True})
   merge_format = workbook.add_format({'align':'left', 'border': True})

#stworzenie arkusza w pliku xlsx
   worksheet = workbook.add_worksheet()
   worksheet.set_landscape()


#stworzenie prezentacji danych na arkuszu
#lewa strona tytuł
   worksheet.write('C1', 'Wojwódzki Szpital Zespolony')
   worksheet.write('C3', 'Orzeczenie Techniczne', bold)

   worksheet.write('A5', 'nr')
   worksheet.write('B5', 'xx/yy')
   worksheet.write('C5', 'Wystawione dnia xx/miesiac/zzzz')

#prawa strona tytuł
   worksheet.write('J1', 'Wojwódzki Szpital Zespolony')
   worksheet.write('J3', 'Orzeczenie Techniczne', bold)

   worksheet.write('H5', 'nr')
   worksheet.write('I5', 'xx/yy')
   worksheet.write('J5', 'Wystawione dnia xx/miesiac/zzzz')

#lewa strona dane (1 zestaw tabel)
   worksheet.merge_range('A7:B7', 'Zleceniodawca', merge_format,)
   worksheet.merge_range('C7:F7', form.kom_orz.data, merge_format)

   worksheet.merge_range('A8:B8', 'Miejsce Użytkowania', merge_format)
   worksheet.merge_range('C8:F8', form.komorka.data, merge_format)

   worksheet.merge_range('A9:B9','Nazwa Urzadzenia', merge_format)
   worksheet.merge_range('C9:F9', form.nazwa_urz.data, merge_format)

#prawa strona dane (1 zestaw tabel)
   worksheet.write('H7', 'Zleceniodawca',merge_format)
   worksheet.write('J7', form.kom_orz.data)

   worksheet.write('H8', 'Miejsce Użytkowania', merge_format)
   worksheet.write('J8', form.komorka.data)

   worksheet.write('H9', 'Nazwa Urzadzenia',merge_format)
   worksheet.write('J9', form.nazwa_urz.data)

   workbook.close()




