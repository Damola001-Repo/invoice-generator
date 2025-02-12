import pandas as pd
from fpdf import FPDF
import glob
import pathlib

filePaths = glob.glob('invoices/*.xlsx')

for filepath in filePaths:

    pdf = FPDF("P", "mm", "a4")

    pdf.add_page()

    filename = pathlib.Path(filepath).stem
    invoice_number, date = filename.split('-')

    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 8, f"Invoice nr.{invoice_number}", ln=1)

    pdf.cell(50, 8, f"Date.{date}", ln=1)

    df = pd.read_excel(filepath)

    df_columns = df.columns
    column_names = [name.replace('_', ' ').title() for name in df_columns]

    for index, name in enumerate(column_names):
        pdf.set_font('Times', 'B', 12)
        if index == 4:
            pdf.cell(38, 12, name, 1, 1)
        else:
            pdf.cell(38, 12, name, 1)

    for index, row in df.iterrows():
        for row_index, i in enumerate(row):
            pdf.set_font(family="Times", size=8)
            if row_index == 4:
                pdf.cell(w=38, h=12, txt=str(i), border=1, ln=1)
            else:
                pdf.cell(w=38, h=12, txt=str(i), border=1)

    total = sum(df['total_price'])

    for i in range(5):
        if i == 4:
            pdf.cell(w=38, h=12, txt=str(total), border=1, ln=1)
        else:
            pdf.cell(w=38, h=12, txt='', border=1)

    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 8, f"The total price is {total}", ln=1)
    pdf.cell(30, 8, "Python how")
    pdf.image('pythonhow.png', w=10)



    pdf.output(f"PDFs/{filename}.pdf")