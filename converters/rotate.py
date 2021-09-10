import PyPDF2
import sys

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
finalName = "rotated/"+splitName[0]+'.'+splitName[1]+'.pdf'
var = sys.argv[2]

pdf_in = open(fileDir, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    print(pagenum)
    page.rotateClockwise(int(var))
    pdf_writer.addPage(page)

pdf_out = open(finalName, 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()