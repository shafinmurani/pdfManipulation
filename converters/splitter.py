from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
pdfid1 = "splitted/"+str(sys.argv[3])+"part1"+'.pdf'
pdfid2 = "splitted/"+str(sys.argv[3])+"part2"+'.pdf'
def split_pdf_to_two(filename,page_number):
    pdf_reader = PdfFileReader(open(filename, "rb"))
    try:
        assert page_number < pdf_reader.numPages
        pdf_writer1 = PdfFileWriter()
        pdf_writer2 = PdfFileWriter()

        for page in range(page_number):
            pdf_writer1.addPage(pdf_reader.getPage(page))

        for page in range(page_number,pdf_reader.getNumPages()):
            pdf_writer2.addPage(pdf_reader.getPage(page))

        with open(pdfid1, 'wb') as file1:
            pdf_writer1.write(file1)

        with open(pdfid2, 'wb') as file2:
            pdf_writer2.write(file2)

    except AssertionError as e:
        print("Error: The PDF you are cutting has less pages than you want to cut!")

split_pdf_to_two("uploads/"+sys.argv[1],int(sys.argv[2]))