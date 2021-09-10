import pandas as pd
import pdfkit
import sys
import os
fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
finalName = "convertedToPdf/"+splitName[0]+'.'+splitName[1]+'.pdf'

df = pd.read_excel(fileDir)
df.to_html(splitName[0]+'.'+splitName[1]+'.html')
pdfkit.from_file(splitName[0]+'.'+splitName[1]+'.html', finalName)

cmd = 'rm '+splitName[0]+'.'+splitName[1]+'.html'

os.system(cmd)