'''
VisualizationTools.py
Last Updated: 5/11/2017

'''
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab
from skimage.measure import compare_ssim
from scipy import ndimage

def display_3d_array(array_3d):
    '''
    Method displays 3d array.

    '''
    # Dislay 3D Rendering
    for i in range(len(array_3d)):
        if i == 1: c = (1, 0, 0)
        elif i == 2: c = (0, 1, 0)
        else: c = (0, 0, 1)
        xx, yy, zz = np.where(array_3d[i] >= 1)
        mlab.points3d(xx, yy, zz, mode="cube", color=c, scale_factor=1)
    mlab.show()

def display_2d_array(array_2d):
    '''
    Method displays 2-d array.

    '''
    # Display 2D Plot
    plt.figure()
    plt.imshow(array_2d, interpolation="nearest")
    plt.show()

def display_spacefilling_dim():
    '''
    Method displays dimensions of various order space filling curves.

    '''
    # Calculating Hilbert 3D to 2D Conversion Dimensions
    for i in range(64):
        x = pow(2,i)
        sq = np.sqrt(x)
        cb = np.cbrt(x)
        if sq %1.0 == 0.0 and cb %1.0 == 0.0:
            print "\nSpace Filling 2D Curve:", int(sq), 'x', int(sq), ', order-', np.log2(sq)
            print "Space Filling 3D Curve:", int(cb), 'x', int(cb), 'x', int(cb), ', order-', np.log2(cb)
            print "Total Number of Pixels:", x

def display_hist(data, title=""):
    '''
    Method displays histogram of inputed data.

    '''
    plt.hist(data)
    plt.title(title)
    plt.show()

def display_image_similarty(image_1, image_2):
    '''
    '''
    err = np.sum((image_1.astype("float") - image_2.astype("float")) ** 2)
    err /= float(image_1.shape[0] * image_2.shape[1])
    print "MSE:", err

    sim = compare_ssim(image_1, image_2, multichannel=True)
    print "Structural Simularity:", sim

if __name__ == '__main__':
    #image_1 = ndimage.imread('../data/Processed-Ras-Gene-PDB-Files/1aa9_r0.png')
    #image_2 = ndimage.imread('../data/Processed-Ras-Gene-PDB-Files/1crr_r0.png')

    #display_image_similarty(image_1, image_2)
    display_spacefilling_dim()