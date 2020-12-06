import imageio
import os, sys

path = "screenshots/"

filenames = os.listdir(path)
filenames.sort()
with imageio.get_writer('covid.gif', mode='I', duration = 0.15) as writer:
    for filename in filenames:
        image = imageio.imread("screenshots/%s" % filename)
        writer.append_data(image)
