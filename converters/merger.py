import PyPDF2
import sys

file1 = "uploads/"+sys.argv[1];
file2 = "uploads/"+sys.argv[2];

pdf1 = open(file1,'rb')
pdf2 = open(file2,'rb')

pdf1Read = PyPDF2.PdfFileReader(pdf1)
pdf2Read = PyPDF2.PdfFileReader(pdf2)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Read.numPages):
    pageObj = pdf1Read.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Read.numPages):
    pageObj = pdf2Read.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('merged/MergedPdfFiles'+sys.argv[1],'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf1.close()
pdf2.close()