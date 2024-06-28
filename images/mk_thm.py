#!/bin/python

import os
from PIL import Image

def compress(file):

    os.mkdir('thm')
    with Image.open(file) as image:
        factor = 0.5
        width, height = image.size
        width = int(factor * width)
        height = int(factor * height)

        image = image.resize((width, height))
        image.save(f'thm/{file}', optimize=True)



def main():

    cwd = os.getcwd()
    files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    
    files = [f for f in files if 'py' not in f]

    for i in files:
        compress(i)


if __name__ == '__main__':
    main()
