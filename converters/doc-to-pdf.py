from subprocess import  Popen
import sys
from shutil import copyfile

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
finalName = "convertedToPdf/"+splitName[0]+'.'+splitName[1]+'.pdf'

LIBRE_OFFICE = r"/usr/bin/soffice"


def convert_to_pdf(input_docx, out_folder):
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    print([LIBRE_OFFICE, '--convert-to', 'pdf', input_docx])
    p.communicate()


sample_doc = fileDir
out_folder = finalName
convert_to_pdf(sample_doc, out_folder)
copyfile('include/index.php', "convertedToPdf/"+splitName[0]+'.'+splitName[1]+".pdf"+'/'+'index.php')