import glob, os
from PIL import Image

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        width, height = im.size #getting the size
        print(width, height, im.size)
        newsize = (width//2, height//2) #dividing the size
        im2 = im.resize(newsize)
        #im2.show()
        im2.save(file + "_small" + ".jpg")



