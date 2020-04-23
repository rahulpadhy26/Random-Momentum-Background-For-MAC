from appscript import app, mactypes
import os
from random import choice, randint, shuffle
from time import time

t = time()

# Some auxiliary operations
momentum_backgrounds_9 = '/Users/rapadhy/Library/Application Support/Google/Chrome/Default/Extensions/laookkfknpbbblfpciffpaejjkokdgca/1.15.9_0/backgrounds/'
momentum_backgrounds_10 = '/Users/rapadhy/Library/Application Support/Google/Chrome/Default/Extensions/laookkfknpbbblfpciffpaejjkokdgca/1.15.10_0/backgrounds/'
val = choice([9, 10])
if val == 9:
    backgrounds_folder = momentum_backgrounds_9
else:
    backgrounds_folder = momentum_backgrounds_10
files = os.listdir(backgrounds_folder)
shuffle(files)
num_files = len(files)
file_index = randint(0, num_files-1)
print (file_index)
reqd_file = files[file_index]
reqd_file_path = os.path.join(backgrounds_folder, reqd_file)

# Setting the background
app('Finder').desktop_picture.set(mactypes.File(reqd_file_path))

print ('\nTime taken for the background change operation :', (time()-t), 'seconds.\n')

