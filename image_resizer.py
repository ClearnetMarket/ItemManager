from PIL import Image
import os
from os import path


# creates another image used as thumbnail thats 300X 300
basewidth_225 = 225
extension = ".jpg"


ext = ['.jpg', '.png', '.gif', '.png', '.jpeg']
base_path = "/mnt/md0/info/item"


def testsize(pathofimage):
    with Image.open(pathofimage) as img:
        width, height = img.size
        if width == 250:
            return 1
        else:
            return 0


def checkbadfiles():
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(tuple(ext)):
                pathofimage = (os.path.join(root, file))
                if file.endswith("_250x.jpg"):
                    getsize = os.path.getsize(pathofimage)
                    if getsize == 0:
                        os.remove(pathofimage)


def convertimage(filename, thefile):
    print("File format incorrect ...")
    img = Image.open(thefile)
    newname = filename + ".jpg"
    img.convert('RGB').save(newname, "JPEG")
    if not thefile.endswith(".jpg"):
        os.remove(thefile)


def imagespider():
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(tuple(ext)):
                pathofimage = (os.path.join(root, file))
                if not file.endswith(".jpg"):
                    convertimage(thefile=pathofimage, filename=file)
                else:
                    pass
                if file.endswith("_250x.jpg"):
                    pass
                else:
                    try:
                        # see if width greate than 250
                        y = testsize(pathofimage)
                        if y != 1:
                            # CREATE A 250 size image
                            # resize
                            # opens the image
                            img = Image.open(pathofimage)
                            # gets base name
                            thebasename = os.path.splitext(file)[0]
                            newname_250 = thebasename + "_250x"
                            renamed_file = (os.path.join(root, newname_250 + extension))

                            # test to see if already done
                            seeifexists = path.exists(renamed_file)

                            if seeifexists is True:
                                pass
                            else:
                                # creates new basename
                                print("")
                                print("")
                                print("*"*10)
                                print("name: ", pathofimage)
                                print("format:", img.format)
                                print("dimensions:",  "%dx%d" % img.size)

                                # convert
                                wpercent = (basewidth_225/float(img.size[0]))
                                hsize = int((float(img.size[1])*float(wpercent)))
                                img = img.resize((basewidth_225, hsize),
                                                 Image.ANTIALIAS)
                                imagesave = os.path.join(root, renamed_file)
                                img.save(imagesave, subsampling=0, quality=100, optimize=True)
                                os.chmod(renamed_file, 0o775)
                                print("converted")
                                print("name: ", renamed_file)
                                print("dimensions:", "%dx%d" % img.size)
                                print("*"*10)
                                print("")
                                print("")
                                getsize = os.path.getsize(imagesave)
                                if getsize == 0:
                                    print("Deleted bad convert")
                                    os.remove(imagesave)
                    except Exception as e:
                        print(str(e))


imagespider()
#checkbadfiles()