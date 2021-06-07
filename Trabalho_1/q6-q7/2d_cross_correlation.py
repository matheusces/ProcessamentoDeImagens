from scipy import signal, misc, fft
import scipy
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

face = np.asarray(Image.open('./input/Woman.png').convert('L'))
face = face - face.mean()
eye = np.asarray(Image.open('./input/Woman_eye.png').convert('L'))
eye = eye - eye.mean()
eye_height = Image.open('./input/Woman_eye.png').height # getting the height of the eye's image
eye_width = Image.open('./input/Woman_eye.png').width # getting the width of the eye's image
#face = face + np.random.randn(*face.shape) * 50  # add noise
corr = signal.correlate2d(face, eye, boundary='symm', mode='valid') # does the 2d-correlation between face and eye's images
y, x = np.unravel_index(np.argmax(corr), corr.shape)  # find the match

fig, (ax_orig, ax_eye, ax_corr) = plt.subplots(1, 3, figsize=(15, 6)) # makes a canvas for the final output
rect = patches.Rectangle((x,y),eye_width,eye_height, edgecolor='r', facecolor="none")
ax_orig.imshow(face, cmap='gray') # add the face's image to the final output image
ax_orig.set_title('Original') # add a title above the image indicating what it is
ax_orig.set_axis_off()
ax_eye.imshow(eye, cmap='gray') # add the eye's image to the final output image
ax_eye.set_title('Eye') # add a title above the image indicating what it is
ax_eye.set_axis_off()
ax_corr.imshow(corr, cmap='gray') # add the correlation's image to the final output image
ax_corr.set_title('Cross-correlation') # add a title above the image indicating what it is
ax_corr.set_axis_off()
ax_orig.add_patch(rect) # add a rectangle onto the original coordinate ( top left eye' point )
fig.savefig('./output/question_6_output.png') # at last saves the figure

