# Import the required Module
import pandas as pd
import pdfkit
import sys

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
finalName = "convertedToExcel/"+splitName[0]+'.'+splitName[1]+'.csv'



