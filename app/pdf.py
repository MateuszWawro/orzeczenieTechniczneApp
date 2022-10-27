from io import BytesIO
import xlsxwriter


def create_report(form=None):

   workbook = xlsxwriter.Workbook('Orzeczenie_Tech.xlsx')

   worksheet = workbook.add_worksheet()
   worksheet.set_landscape()

#cell definitions




#lewa strona tytuł
   worksheet.write('C1', 'Wojwódzki Szpital Zespolony')
   worksheet.write('C3', 'Orzeczenie Techniczne')

   worksheet.write('A5', 'nr')
   worksheet.write('B5', 'xx/yy')
   worksheet.write('C5', 'Wystawione dnia xx/miesiac/zzzz')

#prawa strona tytuł
   worksheet.write('J1', 'Wojwódzki Szpital Zespolony')
   worksheet.write('J3', 'Orzeczenie Techniczne')

   worksheet.write('H5', 'nr')
   worksheet.write('I5', 'xx/yy')
   worksheet.write('J5', 'Wystawione dnia xx/miesiac/zzzz')

#lewa strona dane (1 zestaw tabel)
   worksheet.write('A7', 'Zleceniodawca')
   worksheet.write('C7', form.kom_orz.data)

   worksheet.write('A8', 'Miejsce Użytkowania')
   worksheet.write('C8', form.komorka.data)

   worksheet.write('A9','Nazwa Urzadzenia')
   worksheet.write('C9', form.nazwa_urz.data)

#prawa strona dane (1 zestaw tabel)
   worksheet.write('H7', 'Zleceniodawca')
   worksheet.write('J7', form.kom_orz.data)

   worksheet.write('H8', 'Miejsce Użytkowania')
   worksheet.write('J8', form.komorka.data)

   worksheet.write('H9', 'Nazwa Urzadzenia')
   worksheet.write('J9', form.nazwa_urz.data)

   workbook.close()




