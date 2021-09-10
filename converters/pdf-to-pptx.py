import os
import sys

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
finalName = "convertedToPptx/"+splitName[0]+'.'+splitName[1]+'.pptx'

cmd = 'pdf2pptx -o '+finalName+' '+fileDir

# print(cmd)
os.system(cmd)