import argparse
from PIL import Image

def get_cols(image):
    cols = image.getcolors()
    return cols

def quant256(img, depth=256, retvals=8):
    """
    Returns a list of colors wuth length retvals
    Defaults to max color depth which is 256.
    """
    image = Image.open(img)
    image = image.convert('P', palette=Image.ADAPTIVE, colors=depth)
    colours = image.getcolors()
    colours = sorted(colours)
    result=[]
    for count, value in colours[depth-retvals:]:
        rgb_int = value * 65536
        result.append(rgb_int)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--image')
    parser.add_argument('-d', '--depth')
    args = parser.parse_args()
    if not args.image:
        raise AttributeError('usage quant --image imgfile [--depth n]')
    quant(args.image)

