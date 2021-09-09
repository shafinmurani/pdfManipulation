from PIL import Image
import sys
fileName = sys.argv[1]
path = "uploads/"+sys.argv[1]
splitName = fileName.split('.')
finalPath = "convertedToPdf/"+splitName[0]+'.'+splitName[1]+'.pdf'
print(fileName)
print(finalPath)
image1 = Image.open(path)
im1 = image1.convert('RGB')
im1.save(finalPath)