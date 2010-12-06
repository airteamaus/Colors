import argparse, struct

import scipy
import scipy.misc
import scipy.cluster

from PIL import Image

def get_cols(image):
    cols = image.getcolors()
    return cols

def quant256(img, depth=256, retvals=6):
    """
    Returns a list of colors wuth length retvals
    Defaults to max color depth which is 256.
    """
    image = Image.open(img)
    image.convert("P", palette=Image.ADAPTIVE)
    image.convert("RGB")
    colours = image.getcolors(depth)
    colours = sorted(colours)
    result=[]
    for count, value in colours[depth-retvals:]:
        result.append(rgb_int)
    return result


def kmeans(img, retvals=16):
    NUM_CLUSTERS = retvals
    ar=scipy.misc.fromimage(img)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)
    counts, bins = scipy.histogram(vecs, len(codes))

    index_max = scipy.argmax(counts)
    peak = codes[index_max]
    color = ''.join(chr(c) for c in peak).encode('hex')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--image')
    parser.add_argument('-d', '--depth')
    args = parser.parse_args()
    if not args.image:
        raise AttributeError('usage quant --image imgfile [--depth n]')
    quant(args.image)

