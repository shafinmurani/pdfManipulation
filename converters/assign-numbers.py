from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import os
from PyPDF4.pdf import PdfFileReader, PdfFileWriter
import sys

def createPagePdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1, num + 1):
        c.drawString((210 // 2) * mm, (4) * mm, str(i))
        c.showPage()
    c.save()


def add_page_numgers(pdf_path):
    """
    Add page numbers to a pdf, save the result as a new pdf
    @param pdf_path: path to pdf
    """
    tmp = "__tmp.pdf"

    output = PdfFileWriter()
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f, strict=False)
        n = pdf.getNumPages()

        # create new PDF with page numbers
        createPagePdf(n, tmp)

        with open(tmp, 'rb') as ftmp:
            numberPdf = PdfFileReader(ftmp)
            # iterarte pages
            for p in range(n):
                page = pdf.getPage(p)
                numberLayer = numberPdf.getPage(p)
                # merge number page with actual page
                page.mergePage(numberLayer)
                output.addPage(page)

            # write result
            if output.getNumPages():
                fileName = sys.argv[1]
                fileDir = "uploads/"+sys.argv[1]
                newpath = "numbered/"+sys.argv[1]
                # newpath = pdf_path[:-4] + "_numbered.pdf"
                with open(newpath, 'wb') as f:
                    output.write(f)
        os.remove(tmp)

add_page_numgers("uploads/"+sys.argv[1])