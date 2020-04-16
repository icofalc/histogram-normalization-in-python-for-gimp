import os
from gimpfu import *
import array
import numpy as np

def myplugin(img,layer):



 

# the procedure code starts here

white=(255, 255, 255)
black=(0,0,0)
img=gimp.image_list()[0]
print img
layer = pdb.gimp_image_get_active_layer(img)
highlights = pdb.gimp_histogram(layer, 0, 179, 255)
layer_copy=img.layers[0].copy()
reg_layer_A=layer_copy.get_pixel_rgn(0,0,img.width,img.height,False,False) #prendo la regione che mi interessa da layer che ho copiato prima


src_pixels_reg_A=array.array("B",reg_layer_A[0:img.width,0:img.height])# prendo i singoli valori dei pixel


valori_normalizzati=_create_normalized_frequencies_greyscale(src_pixels_reg_A) #normalizzao i singoli valori dei pixel
img.add_layer(layer_copy,3) #add layer in gimp posizione 3

    # the procedure code ends here

def prova():
    img=gimp.image_list()[0]
    
    #layer = pdb.gimp_image_get_active_layer(img)
    layer_copy=img.layers[0].copy()
    img.add_layer(layer_copy,3)
    print(img.layers)
    array_temp=[]
    for x in range(layer_copy.width):
        for y in range(layer_copy.height):
            r=layer_copy.get_pixel(x,y)[0]
            array_temp.append(r)
    
    massimo=max(array_temp)
    minimo=min(array_temp)
    print(minimo)
    print(massimo)
    
    costante=float(float(255) / float(massimo - minimo))
    print(costante)
    for x in range(layer_copy.width):
        for y in range(layer_copy.height):
            r=layer_copy.get_pixel(x, y)[0]
            
            if r >= minimo and r<=massimo:
                r=r-minimo
                r=r*costante
            
            layer_copy.set_pixel(x, y, (int(r),))
            
            
    pdb.gimp_drawable_update(layer_copy, 0, 0, layer_copy.width, layer_copy.height)
    


register(
         "python-fu-myplugin",
         N_("A short piece of information about the procedure."),
         "More detailed information about the procedure.",
         "The author of the procedure.",
         "The copyright holder for the procedure (usually the same as the author).",
         "The date when the procedure was written.",
         N_("_My plug in"),
         "GRAY*",
         [
          (PF_IMAGE, "image",       "Input GRAYSCALE image", None),
          (PF_DRAWABLE, "drawable", "Input drawable", None),
          ],
         [],
         myplugin,
         menu="<Image>/Filters/My plug in menu",
         domain=("gimp20-python", gimp.locale_directory)
         )
main()
