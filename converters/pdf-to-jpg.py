
# import module
from pdf2image import convert_from_path
import sys
import os
from shutil import move, copyfile

fileName = sys.argv[1]
fileDir = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
cmd = "mkdir convertedToJpg/"+splitName[0]+'.'+splitName[1]+"/"
os.system(cmd)
finalName = splitName[0]+'.'+splitName[1]

# Store Pdf with convert_from_path function
images = convert_from_path(fileDir)
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save("convertedToJpg/"+finalName+'page'+ str(i) +'.jpg', 'JPEG')
    move("convertedToJpg/"+finalName+'page'+str(i)+'.jpg', 'convertedToJpg/'+splitName[0]+'.'+splitName[1]+'/'+finalName+'page'+str(i)+'.jpg')
    copyfile("include/index.php","convertedToJpg/"+finalName+"/index.php")