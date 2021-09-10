import os
import sys
from shutil import move

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]

stage1 = fileName.split('.')
# print(stage1)
stage1Final = stage1[0]+'.'+stage1[1]+'.pdf'
# print(stage1Final)
splitName = fileName.split('.')
finalName = "convertedToPdf/"+splitName[0]+'.'+splitName[1]+'.pdf'

cmd = 'libreoffice --headless --invisible --convert-to pdf ' + fileDir
os.system(cmd)
move(stage1Final , finalName)