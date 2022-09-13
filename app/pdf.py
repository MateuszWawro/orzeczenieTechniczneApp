from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm


#name pdf and define size of pdf
canvas = Canvas("Plik_PDF", pagesize = A5)



#save pdf file
canvas.save()

