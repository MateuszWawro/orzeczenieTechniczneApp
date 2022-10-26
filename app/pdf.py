from io import BytesIO
import xlsxwriter


def create_report(form=None):

   workbook = xlsxwriter.Workbook('Orzeczenie_Tech.xlsx')
   worksheet = workbook.add_worksheet()
   worksheet.set_landscape()
   worksheet.write(0, 0, 'Zleceniodawca')
   worksheet.write(0, 1, form.kom_orz.data)

   worksheet.write(1, 0, 'Miejsce')
   worksheet.write(1, 1, form.komorka.data)

   worksheet.write(2, 0, 'Nazwa')
   worksheet.write(2, 1, form.nazwa_urz.data)

   #worksheet.write(0, 0, 'Total')
   #worksheet.write(0, 0, 'Total')
   #worksheet.write(0, 0, 'Total')
   #worksheet.write(0, 0, 'Total')
   #worksheet.write(0, 0, 'Total')

   workbook.close()




