from appscript import app, mactypes
import os
from random import choice, randint, shuffle
from time import time

t = time()

# Some auxiliary operations
momentum_backgrounds = '<path-in-the-local-machine>'
files = os.listdir(momentum_backgrounds)
shuffle(files)
num_files = len(files)
file_index = randint(0, num_files-1)
print (file_index)
reqd_file = files[file_index]
reqd_file_path = os.path.join(backgrounds_folder, reqd_file)

# Setting the background
app('Finder').desktop_picture.set(mactypes.File(reqd_file_path))

print ('\nTime taken for the background change operation :', (time()-t), 'seconds.\n')

