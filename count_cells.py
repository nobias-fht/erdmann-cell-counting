import skimage
import os
from cellpose import models
import pandas as pd
import easygui


imagepath = easygui.diropenbox('Select input data location')
output_path = easygui.diropenbox('Select output location')

print("==================================")
print("STARTING SCRIPT")
print("==================================")

files = os.listdir(imagepath)
filenames = []
counts = []
df = pd.DataFrame(columns=['file', 'count'])
model = models.CellposeModel(pretrained_model='model/erdmann')
channels = [[0,0]]

for i, file in enumerate(files):
    if file.endswith('.tif'):
        print(f'running file: {file}, (file {i+1} of {len(files)})')
        im = skimage.io.imread(imagepath + os.path.sep +  file)
        full_shape = im.shape
        #resize image to 15% of original size
        im_small = skimage.transform.resize(im, (int(im.shape[0]*0.15), int(im.shape[1]*0.15)))
        small_shape = im_small.shape
        print(f'resized image from {full_shape} to {small_shape}')
        print('starting segmentation')
        masks, flows, styles = model.eval(im_small, diameter=None, flow_threshold=None, channels=channels)
        props = skimage.measure.regionprops(masks)
        filenames.append(file)
        counts.append(len(props))
        skimage.io.imsave(output_path + os.path.sep +  'masks_' + file, masks)
        skimage.io.imsave(output_path + os.path.sep +  'raw' + file, im_small)

df['file'] = filenames
df['count'] = counts    
df.to_csv(output_path + os.path.sep + 'counts.csv', index=False)  

print("==================================")
print("SCRIPT COMPLETED")
print("==================================")