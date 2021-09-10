import pdfkit 
import sys

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
finalName = "convertedToPdf/"+splitName[0]+'.'+splitName[1]+'.pdf'

pdfkit.from_file(fileDir, finalName) 