import PyPDF2 as p,os
import sys

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]

output = p.PdfFileWriter()
input_stream = p.PdfFileReader(open(fileDir, "rb"))

for i in range(0, input_stream.getNumPages()):
    output.addPage(input_stream.getPage(i))

outputstream = open("protected/"+sys.argv[1], "wb")

output.encrypt(sys.argv[2], use_128bit=True)
output.write(outputstream)
outputstream.close()
