import os
import sys
from shutil import move

path = sys.argv[1]
split = path.split('/')
# print(split)
finalSplit = split[1]
finalSplit1 = finalSplit.split('.')
# print(finalSplit1)
finalName = finalSplit1[0]+'.'+finalSplit1[1]+".docx"
destination = "convertedToDocx/"+finalName
cmd = "pdf2docx convert "+path
os.system(cmd)
move("uploads/"+finalName, destination)
