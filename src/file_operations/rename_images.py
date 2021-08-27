#!/usr/bin/python
import os


root = '/home/leins275/Projects/Polytech/master/big-data/report/images/ganre_predict'
images = list(os.walk(root))

for i, _ in enumerate(images[0][2]):
    old = os.path.join(root, _)
    new = os.path.join(root, f'img-{i}.png')
    os.replace(old, new)

