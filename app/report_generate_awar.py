from io import BytesIO
import datetime
import xlsxwriter
from flask_login import current_user


def create_awaria_rep(form=None):
    output = BytesIO()

    # stworzenie pliku xlsx
    workbook = xlsxwriter.Workbook(output)