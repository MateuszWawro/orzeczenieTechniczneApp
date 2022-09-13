from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A5
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

buffer = BytesIO()
canvas = Canvas("Plik_PDF", pagesize = A5)
canvas.setFont("Vera", size=10)

