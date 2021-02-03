import imageio
import os, sys

path = "screenshots/"

def get_files(path):
    filenames = os.listdir(path)
    filenames.sort()
    return filenames

filenames = get_files(path)

with imageio.get_writer('covid.gif', mode='I', duration = 0.15) as writer:
    for filename in filenames:
        image = imageio.imread("screenshots/%s" % filename)
        writer.append_data(image)
