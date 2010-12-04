import argparse
import flickr
from PIL import Image

def get_cols(image):
    cols = image.getcolors()
    return cols

def quant(img, depth=256, retvals=8):
    image = Image.open(img)
    image = image.convert('P', palette=Image.ADAPTIVE, colors=depth)
    colours = image.getcolors()
    colours = sorted(colours)
    result=[]
    for count, colour in colours[depth-retvals:]:
        colour = colour * 65536
        blue =  colour & (depth-1)
        green = (colour >> 8) & (depth-1)
        red   = (colour >> 16) & (depth-1)
        result.append((red,green,blue))
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--image')
    parser.add_argument('-d', '--depth')
    args = parser.parse_args()
    if not args.image:
        raise AttributeError('usage quant --image imgfile [--depth n]')
    eigth_cols = quant(args.image)

