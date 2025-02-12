from fpdf import FPDF
import glob
import pathlib


filePaths = glob.glob('Text+Files/*.txt')

pdf = FPDF("P", "mm", "a4")
# pdf.set_auto_page_break(False)

for filepath in filePaths:
    with open(filepath, 'r') as file:
        content = file.readlines()

    pdf.add_page()
    filename = pathlib.Path(filepath).stem
    name = filename.title()

    pdf.set_font("Times", "I", 16)
    pdf.cell(50, 8, name, 0, 1, 'L')

pdf.output('animals.pdf')
