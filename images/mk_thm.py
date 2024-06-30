#!/bin/python

import os
from PIL import Image

def compress(file):

    if not os.path.isdir('thm'):
        os.mkdir('thm')

    with Image.open(file) as image:
        factor = 0.5
        width, height = image.size
        width = int(factor * width)
        height = int(factor * height)

        image = image.resize((width, height))


        # dealing with image orientation

        if hasattr(image, '_getexif'):
            exif = image._getexif()
            if exif:
                for tag, label in ExifTags.TAGS.items():
                    if label == 'Orientation':
                        orientation = tag
                        break
                if orientation in exif:
                    if exif[orientation] == 3:
                        image = image.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        image = image.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        image = image.rotate(90, expand=True)

        image.save(f'thm/{file}', optimize=True)



def main():

    cwd = os.getcwd()
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    
    files = [f for f in files if 'py' not in f]

    for i in files:
        compress(i)


if __name__ == '__main__':
    main()
